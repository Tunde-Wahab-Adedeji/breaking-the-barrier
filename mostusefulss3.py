from sqlite3 import dbapi2 as sqlite3
import re,time
c=time.asctime()   
x= int(input('enter your regno:'))
y= str(input('enter your name:'))
k=int(input('enter the no to search for:'))
a,d=(int,re.findall(r'\d+',c))
u=(c[4:7])
l=(c[0:3])
#print(l)
#print(c)
p=('%s%s%s%s%s' %(d[0],'/',u,'/',d[4]))
#print(p)
h=('%s%s%s%s%s'%(d[1],':',d[2],':',d[3]))
#print(h)
sqliteconn = sqlite3.connect('tunde_db')
cursor = sqliteconn.cursor()
creat_table="""CREATE TABLE IF NOT EXISTS my_table(reg integer primary key unique,name text not null,my_time text not null,my_date text not null);"""
cursor.execute(creat_table)
print("table created sucessfully")
insert_table=""" insert into my_table(reg,name,my_time,my_date)
values(?,?,?,?);"""
data_value=(x,y,h,p)  
cursor.execute(insert_table,data_value)
sqliteconn.commit()
print("student added success")
selectme ="""select * from my_table where reg='{}' """.format(k)
cursor.execute(selectme)
c= cursor.fetchall()
for i in c:
	print(i)
#	for r in i:
				#print(r)
	#	print('Name:%s:RegNo:%d TimeArrive:%sDate:%s'%(r[0],r[1],r[2],r[3]))
	

