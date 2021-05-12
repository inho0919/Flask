import psycopg2

hostname = ""   # Your Hostname
username = ""   # Your Username
password = ""   # Your Password
port = ""       # Your Port
db_name = ""    # Your DB_Name

def dbconnect():
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "SELECT * FROM table_name;"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Connect Success"
    except:
        return "Connect Error"