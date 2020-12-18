import os
c=os.getcwd()
x=str(input('Enter the word to find in %s'':' %c))
#print(c)
if x in c:
	print('Yes there is the word %s'  'in'  '%s' %(x,c))
else:
	print('No there is no  word %s'  'in'  '%s'  %(x,c))