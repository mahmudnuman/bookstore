import sqlite3
import mysql.connector
from os.path import realpath




con = mysql.connector.connect(
    user="root", 
    password = "", 
    host="127.0.0.1",
    database = "library"
)


    
def insert(item,quantity,price):
    cur=con.cursor()
    cur.execute("INSERT INTO store (item,quantity,price) VALUES(%s,%s,%s)",(item,quantity,price))
    con.commit()
    con.close()
    
    
#insert("Whisky Glass",10,15)

def delete(id):
    con.reconnect()
    cur=con.cursor()
    cur.execute("DELETE FROM store WHERE id = '%s'" % id)
    con.commit()
    con.close()
    

def update(id,item,quantity,price):
    con.reconnect()
    cur=con.cursor()
    query="Update store set item = %s,quantity = %s,price = %s where id = %s"
    data=(item,quantity,price,id)
    cur.execute(query,data) 
    con.commit()
    con.close()
    
#delete(1)    
#update(2,"Ganja",25,11)
    
def view():
    con.reconnect()
    cur=con.cursor()
    cur.execute("Select * from store")
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows

print(view())