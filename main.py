import sqlite3


def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn)
    )

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book order by id desc")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM book where title=? or author=? or year=? or isbn=?", (
            title, author, year, isbn)
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("Delete FROM book where id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "Update book set title=?, author=?, year=?, isbn=? where id=?", (
            title, author, year, isbn, id)
    )
    conn.commit()
    conn.close()


connect()
