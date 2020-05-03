import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

# query = """
# DROP TABLE answer
# """

# query = """
# CREATE TABLE answer(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     msg TEXT,
#     answ TEXT
# )
# """
# cur.execute(query)
# conn.commit()

query = """
INSERT INTO answer(msg, answ) VALUES
("commands", "Вот мои команды: Привет, Админ, Как дела?, commands"),
("Привет", "Здраствуйте, хозяин!"),
("привет", "Здраствуйте, хозяин!"),
("Админ", "Гл. Администратор, ня - https://vk.com/manestorm"),
("админ", "Гл. Администратор, ня - https://vk.com/manestorm"),
("Как дела?", "Всё было ужасно, пока не пришли Вы, хозяин!"),
("Как дела", "Всё было ужасно, пока не пришли Вы, хозяин!"),
("как дела?", "Всё было ужасно, пока не пришли Вы, хозяин!"),
("как дела", "Всё было ужасно, пока не пришли Вы, хозяин!")
"""

cur.execute(query)
conn.commit()

def get(table_name, cols = "*"):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    query = """
        SELECT {1} from {0}
    """.format(table_name, cols if cols=="*" else "({0})".format(",".join(cols)) )

    cur.execute(query)
    colNames = list(map(lambda x: x[0], cur.description))

    result = []

    for i in cur.fetchall():
        result.append(dict(zip(colNames, i)))
    db.close()

    return result

def insert(table_name, cols, data):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    query = """
        INSERT INTO {0}({1})
        VALUES('{2}');
    """.format(table_name, ",".join(cols), "','".join(data))

    cur.execute(query)

    db.commit
    db.close
print(get("answer"))

# conn.close()