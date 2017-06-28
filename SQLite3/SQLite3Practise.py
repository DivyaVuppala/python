import sqlite3
from StdSuites.Table_Suite import row
db=sqlite3.connect("test.db")

db.execute('drop table if exists test')
db.execute('create table test (x int,y int)')

db.execute('insert into test values (?,?)',(1,1))
db.execute('insert into test values (?,?)',(2,3))
db.execute('insert into test values (?,?)',(4,5))
db.execute('insert into test values (?,?)',(6,6))



cursor = db.execute('select * from test order by x')
for row in cursor:
    print(row)

print("-----------------------")
db.execute('update test set y = ? where x = ?',(1,2))

db.execute('delete from test where x = ?',(6,))
cursor = db.execute('select * from test order by x')
for row in cursor:
    print(row)   
print("-----------------------")

print("creating a new table")
db.execute('drop table if exists anothertest')    
db.execute('create table anothertest (id int,name string)')
db.execute('insert into anothertest values (?,?)',(1,"Divya"))
db.execute('insert into anothertest values (?,?)',(2,"Sravan"))
cursor = db.execute('select * from anothertest order by name')
for row in cursor:
    print(row)
    
