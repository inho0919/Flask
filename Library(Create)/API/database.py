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
        sql = "INSERT INTO board(id, title, content) VALUES('"+ids+"', '"+title+"','"+texts+"');"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Create)"
