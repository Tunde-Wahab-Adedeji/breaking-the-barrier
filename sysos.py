import os,tempfile,string
#print(help(os))
#print(help(tempfile))
h=os.listdir()
z=[]
for i in h:
	z.append(i)
	for t in z:
		if 'tunde'not in i:
			y=str(i +'/tunde')
			print(string.capwords(y))
		
			
			
			
	
	
	
#print(h[3])
g=os.times()
for i in g:
	i=i+10
#	print(is
	''
	os.setpgrp()
	d=os.getcwd()
	print(d)
	if 'storage' in d:
		z=[]
		for i in d:
			z.append('storage')
		#	print(z)

	
	else:
		print('No')
#	for root in d:
	
	

	
w,z=os.pipe()
print(w)
#print(help(g))

k=tempfile.gettempdir()
d,e=tempfile.mkstemp()
u=os.read(d,5)
print(u)
8
c=os.write(d,str.encode(""))
if c!=0:
	print('ok')
else:
	print('not ok'),5