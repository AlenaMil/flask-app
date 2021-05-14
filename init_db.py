import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра английского языка',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра археологии и этнографии',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра востоковедения',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра всеобщей истории',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра истории и теории литературы',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра истории, культуры и искусств',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра источниковедения литературы и древних языков',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра массовых коммуникаций',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра межкультурной коммуникации',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра общего и русского языкознания',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра отечественной истории',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра романо-германской филологии',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра теории и истории журналистики',)
            )
cur.execute("INSERT INTO faculty (name) VALUES (?)",
            ('Кафедра фундаментальной и прикладной лингвистики',)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Нулевой', 'r_24 (1).mp3', 2)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Первый', 'ru_24.mp3', 2)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Второй', 'nuance.com.katya.mp3', 1)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Третий', 'google.mp3', 1)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Четвертый', 'acapela.mp3', 1)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Пятый', 'rus_24.mp3', 2)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Шестой', 'nuance.Milena.mp3', 1)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Седьмой', '1_channel.mp3', 2)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Восьмой', 'D_W.mp3', 2)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Девятый', 'nuance.Yuri.mp3', 1)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Десятый', 'russia_24.mp3', 2)
            )
cur.execute("INSERT INTO files (name, filename, artificial) VALUES (?, ?, ?)",
            ('Одиннадцатый', 'readspeaker.mp3', 1)
            )
# cur.execute("INSERT INTO users (username, gender, age, depid, course) VALUES (?, ?, ?, ?, ?)",
#             ('user1', 1, 18, 1, 1)
#             )
# cur.execute("INSERT INTO users (username, gender, age, depid, course) VALUES (?, ?, ?, ?, ?)",
#             ('user2', 0, 28, 1, 0)
#             )
connection.commit()
connection.close()

connection = sqlite3.connect('database.db')
cur = connection.cursor()
cur.execute("INSERT INTO department (name, facultyid) VALUES (?, ?)",
            ('Филология', 1)
            )
cur.execute("INSERT INTO department (name, facultyid) VALUES (?, ?)",
            ('Фундаментальная и прикладная лингвистика ', 1)
            )
cur.execute("INSERT INTO department (name, facultyid) VALUES (?, ?)",
            ('История', 1)
            )
cur.execute("INSERT INTO department (name, facultyid) VALUES (?, ?)",
            ('Востоковедение и африканистика ', 1)
            )
cur.execute("INSERT INTO department (name, facultyid) VALUES (?, ?)",
            ('Лингвистика (иностранные языки) ', 1)
            )
cur.execute("INSERT INTO department (name, facultyid) VALUES (?, ?)",
            ('Журналистика ', 1)
            )

# cur.execute("INSERT INTO results (user, file, art, mark1, mark2, mark3) VALUES (?, ?, ?, ?, ?, ?)",
#             (1, 1, 1, '', '', '')
#             )
# cur.execute("INSERT INTO results (user, file, art, mark1, mark2, mark3) VALUES (?, ?, ?, ?, ?, ?)",
#             (1, 2, 0, '', '', '')
#             )
# cur.execute("INSERT INTO results (user, file, art, mark1, mark2, mark3) VALUES (?, ?, ?, ?, ?, ?)",
#             (1, 3, 0, '', '', '')
#             )
# cur.execute("INSERT INTO results (user, file, art, mark1, mark2, mark3) VALUES (?, ?, ?, ?, ?, ?)",
#             (2, 1, 0, '', '', '')
#             )
# cur.execute("INSERT INTO results (user, file, art, mark1, mark2, mark3) VALUES (?, ?, ?, ?, ?, ?)",
#             (2, 2, 1, '', '', '')
#             )
# cur.execute("INSERT INTO results (user, file, art, mark1, mark2, mark3) VALUES (?, ?, ?, ?, ?, ?)",
#             (2, 3, 0, '', '', '')
#             )
connection.commit()
connection.close()