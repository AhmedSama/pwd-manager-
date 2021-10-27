import sqlite3

def create_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        f''' CREATE TABLE IF NOT EXISTS  data(
                id INTEGER PRIMARY KEY,
                title VARCHAR(50) NOT NULL,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL,
                pwd VARCHAR(50) NOT NULL,
                cdate VARCHAR(50)  NOT NULL )''')
    conn.commit()
    conn.close()


def add_to_table(title, username, email, pwd,cdate):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO data(title,username,email,pwd,cdate) VALUES(?,?,?,?,?)",(title, username, email, pwd,cdate))
    conn.commit()
    conn.close()


def get_data():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    data = c.fetchall()
    conn.commit()
    conn.close()
    return data
def get_data_where(id_):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE id = ?",(id_,))
    data = c.fetchall()
    conn.commit()
    conn.close()
    return data

def delet_from_table(id_):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("DELETE FROM data WHERE id=?", (id_,))
    conn.commit()
    conn.close()


def edit_from_table(title, username, email, pwd, cdate, id_):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("""UPDATE data SET title = ?, username = ?, email = ?, pwd = ?, cdate = ?  WHERE id = ?;""", (title, username, email, pwd,cdate,id_))
    conn.commit()
    conn.close()
