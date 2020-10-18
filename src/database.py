import sqlite3
def create():
    connect=sqlite3.connect("Data.db")
    connect.execute("CREATE TABLE if not exists customer(name text not null,current_balance integer)")
    connect.execute("INSERT INTO customer VALUES(?,?)",("RUCHIRA",15000))
    connect.commit()
    res=connect.execute("select * from customer")
    for data in res:
        print("Name:",data[0])
        print("pin:", data[1])
    connect.close()
create()