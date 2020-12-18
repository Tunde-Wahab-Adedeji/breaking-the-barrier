a=str(input('enter your name:'))
if (a.islower()) or(a.isupper())==True:
	b =a.capitalize()
	print(b)
elif not (a.islower())or(a.isupper()):
	c=a.capitalize()
	print(c)
else:
	print(a)
