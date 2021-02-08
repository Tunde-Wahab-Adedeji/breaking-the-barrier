import string,time

#print(help(string))
print('The list is empty now')
x=int(input('Enter your number:'))
#x=string.capwords(x)
z=[]
while x not in z:
	z.append(x)
	print(time.asctime())
	print(z)
while x in z:
	d =int(input('Enter your number:'))
	#d=string.capwords(d)
	if d not in z and d!=x:
		z.append(d)
		print(time.asctime())
		print('%d is not in the list yet and therefore is added to the list' %(d,))
		print(z)
	else:
		print('%d already exists in the list' %(d,))
		print(z)		