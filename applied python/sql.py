import sqllite3 as SQ
db1 = SQ.connect('test.db')
db2 = SQ.connect(':memory:')
c = db1.cursor()
c.execute (create table a (id int, name varchar(20)))
c.close()
for index, name in enumerate (('Bill', 'John', 'Mary', 'Rob', 'Tom'))
    c = db1.cursor()
    c.execute('insert into a (id, name) values (?,?)', (index, name))
    c.close()
    db.commit()
c = db1.cursor()
c1 = c.execute('select * from a')
c1.fetchone()
c1.fetchmany(2)
c1.fetchall()
c.close()
c1.close()

c = db1.cursor()
c1 = c.execute('select * from a')
for row in c1:
    print (row)
c.close()
c1.close()

c = db1.cursor()
name = "John"
print (c.execute('select * from a where name =? (?,?)', (name,)))
db1.close()
db2.close()