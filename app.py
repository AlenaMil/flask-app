import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb6e58bc-f822-479a-a694-0f402141a14d'
app.config["CLIENT_MP3"] = "sound"


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user


def get_results(user_id):
    conn = get_db_connection()
    result = conn.execute('SELECT r.id, r.art, r.mark1, r.mark2, r.mark3, f.name, f.artificial FROM results r LEFT JOIN files f on r.file = f.id WHERE r.user = ?',
                        (user_id,)).fetchall()
    conn.close()
    if user is None:
        abort(404)
    print(result)
    return result


def get_sounds():
    conn = get_db_connection()
    files = conn.execute('SELECT * FROM files').fetchall()
    conn.close()
    return files


def get_user_by_username(username):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?',
                        (username,)).fetchone()
    conn.close()
    if user:
        return True
    else:
        return False


def get_full_results():
    conn = get_db_connection()
    results = conn.execute('SELECT r.id, r.art, r.mark1, r.mark2, r.mark3, f.name, f.artificial FROM results r LEFT JOIN files f on r.file = f.id').fetchall()
    conn.close()
    return results


@app.route('/<int:user_id>')
def user(user_id):
    user = get_user(user_id)
    result = get_results(user_id)
    conn = get_db_connection()
    dept_name = conn.execute('SELECT * FROM department WHERE id = ?',
                        (user['depid'],)).fetchone()['name']
    conn.close()
    # название пола по его id
    if user['gender'] == 1:
        gender = "Женский"
    else:
        gender = "Мужской"

    # название курса по его id
    courses = {1: "Первый", 2: "Второй", 3: "Третий", 4: "Четвертый", 5: "Первый (магистратура", 6: "Второй (магистратура)", 7: "Выпускник"}
    course_name = courses[user['course']]
    return render_template('user.html', user=user, result=result, dept=dept_name, gender=gender, course=course_name)


@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)


@app.route('/create', methods=('GET', 'POST'))
def create():
    conn = get_db_connection()
    # массив файлов и кафедр для заполнения шаблона create.html
    files = conn.execute('SELECT * FROM files').fetchall()
    deps = conn.execute('SELECT * FROM department').fetchall()
    facu = conn.execute('SELECT * FROM faculty').fetchall()
    #courses = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()

    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        gender = request.form['gender']
        department = request.form['dep']
        course = request.form['course']

        if not username:
            flash('Не указано имя пользователя!')
        #elif not get_user_by_username(username):
            #flash('Укажите другое имя!')
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            # создаем запись о тестируемом
            cursor.execute('INSERT INTO users (username, age, gender, depid, course) VALUES (?, ?, ?, ?, ?)',
                         (username, age, gender, department, course))
            #cursor.commit()

            # получаем id тестируемого
            # user_id = conn.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()['id']
            user_id = cursor.lastrowid

            # для каждого файла сохраняем результаты
            files = conn.execute('SELECT * FROM files').fetchall()
            for f in files:
                m1 = request.form['m1_' + str(f['id'])]  # первый признак
                m2 = request.form['m2_' + str(f['id'])]  # второй признак
                m3 = request.form['m3_' + str(f['id'])]  # третий признак
                artif = request.form['art_' + str(f['id'])]  # искусственный или натуральный
                conn.execute('INSERT INTO results (user, file, art, mark1, mark2, mark3) VALUES (?, ?, ?, ?, ?, ?)',
                             (int(user_id), f['id'], int(artif), m1, m2, m3))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html', files=files, deps=deps, facu=facu)

# удалено из меню ToDo: доработать формирование таблицы
@app.route('/full')
def full_results():
    results = get_full_results()
    return render_template('full.html', results=results)
