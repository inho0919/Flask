import psycopg2
import json

hostname = ""
username = ""
password = ""
port = ""
db_name = ""
    
def create(ids, title, texts):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "INSERT INTO table_name(id, title, content) VALUES('"+ids+"', '"+title+"','"+texts+"');"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Create)"

def read():
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "SELECT * FROM table_name;"
        cur.execute(sql)
        a = cur.fetchall()
        a = json.dumps(a)
        a = json.loads(a)
        conn.commit()
        conn.close()
        return a
    except:
        return "Error (Read)"

def update(num, ids, title, texts):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "UPDATE table_name SET no='"+num+"', id='"+ids+"', title='"+title+"', content='"+texts+"' WHERE no='"+num+"';"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Update)"

def delete(no):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "DELETE FROM table_name WHERE no = '"+no+"';"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Delete)"

def datas(num):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "SELECT * FROM table_name WHERE no = '"+num+"';"
        cur.execute(sql)
        a = cur.fetchall()
        a = json.dumps(a)
        a = json.loads(a)
        conn.commit()
        conn.close()
        return a
    except:
        return "Error (Read)"

