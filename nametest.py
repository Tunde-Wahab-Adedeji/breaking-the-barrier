x=str(input('please enter your name:'))
#y=str(input('please enter your name again:'))
z=['tunde','wale']
def fit(x):
	if x not in z:
		z.append(x)
		return z
d=fit(x)
if x in z:
	print('your name already exist')
else:
	d.append(x)
print(d)
	