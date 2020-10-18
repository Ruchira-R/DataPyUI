import sqlite3
def create():
    connect=sqlite3.connect("Data.db")
    connect.execute("CREATE TABLE account(name text,email_id text,pin integer not null,current_balance real)")
    connect.execute("INSERT INTO account VALUES(?,?,?,?)",("ROSHAN","roshandaivagna@gmail.com",4567,200000))
    connect.commit()
    res=connect.execute("select * from accounts")
    for data in res:
        print("Email:",data[1])
        print("Name:",data[0])
        print("pin:", data[2])
        print("Current:",data[3])
    connect.close()
create()