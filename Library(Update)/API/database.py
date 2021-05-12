import psycopg2
import json

hostname = ""
username = ""
password = ""
port = ""
db_name = ""
    
def update(num, ids, title, texts):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "UPDATE board SET no='"+num+"', id='"+ids+"', title='"+title+"', content='"+texts+"' WHERE no='"+num+"';"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Update)"

def datas(num):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "SELECT * FROM board WHERE no = '"+num+"';"
        cur.execute(sql)
        a = cur.fetchall()
        a = json.dumps(a)
        a = json.loads(a)
        conn.commit()
        conn.close()
        return a
    except:
        return "Error (Read)"