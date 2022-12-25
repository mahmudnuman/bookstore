import psycopg2

from os.path import realpath




conn ="dbname = 'library' user='postgres' password='7161' host='localhost' port='5432'"


def create_table():
    con = psycopg2.connect(conn)
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS INTO store (item TEXT,quantity INTEGER,price REAL)")
    con.commit()
    con.close() 

    
def insert(item,quantity,price):
    con = psycopg2.connect(conn)
    cur=con.cursor()
    cur.execute("INSERT INTO store (item,quantity,price) VALUES(%s,%s,%s)",(item,quantity,price))
    con.commit()
    con.close()
    
    
insert("Whisky Bottle",10,15)

def delete(id):
    con = psycopg2.connect(conn)
    cur=con.cursor()
    cur.execute("DELETE FROM store WHERE id = '%s'" % id)
    con.commit()
    con.close()
    

def update(id,item,quantity,price):
    con = psycopg2.connect(conn)
    cur=con.cursor()
    query="Update store set item = %s,quantity = %s,price = %s where id = %s"
    data=(item,quantity,price,id)
    cur.execute(query,data) 
    con.commit()
    con.close()
    
delete(1)    
update(2,"Ganja",25,11)
    
def view():
    con = psycopg2.connect(conn)
    cur=con.cursor()
    cur.execute("Select * from store")
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows

print(view())