#This code is used in automated time book for
  





import re,time
c=time.asctime()   
a,d=(int,re.findall(r'\d+',c))
u=(c[4:7])
l=(c[0:3])
print(l)
#print(c)
p=('%s%s%s%s%s' %(d[0],'/',u,'/',d[4]))
print(p)
h=('%s%s%s%s%s'%(d[1],':',d[2],':',d[3]   ))
if(int(d[1])>7 or int(d[2])>30):
	g=int(d[1])-7
	k=int(d[2])-30
	print('you are late to school by %d %s%s %d %s'%(g,'hrs','|',k,'min'))
else:
	print('you are early to school')
if(int(d[1])<=11):
	go='AM'
	print(h+go)
else:
	go='PM'
	print(h+go)
	
	

