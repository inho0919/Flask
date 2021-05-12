# Flask-Python3
Flask Web Framework Source

This is Flask Web Framework library.


## Install Sollution
### <Linux - Ubuntu>
  - sudo apt install python3-venv
  - sudo pip3 install Flask


## Flask Execute
  - python app.py     -> Python2.x
  - python3 app.py    -> Python3.x


## Chapter
- Basic 1,2
- Render Template
- REST API (GET, POST)
- DB Connection (PostgreSQL)
- CRUD for Board


## Database (Install PostgreSQL)
  - sudo apt-get install postgresql

### PostgreSQL Access
  - su - postgres
  - psql
  - \l (Lists of Database)
  - \q (Quit)
  - \? (Help)
  - \d (Check the table)

### Change the Password and Create Database
  - ALTER USER postgres with encrypted password '[Input the Password]';
  - sudo /etc/init.d/postgresql restart (restart)
  - psql -U postgres -h localhost (Check the psql)
  - sudo -u postgres createdb [DB_name]
  - sudo -u postgres psql [DB_name]

### Create table for CRUD Board (Example)
  - CREATE TABLE board(id VARCHAR2(20) PRIMARY KEY, text TEXT);


