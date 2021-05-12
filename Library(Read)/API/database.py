import psycopg2
import json

hostname = ""
username = ""
password = ""
port = ""
db_name = ""
    
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
