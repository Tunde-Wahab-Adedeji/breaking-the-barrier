import random
print(help(random))
maxn = 10
n = random.randint(1, maxn)
c=random.uniform(1,maxn)
#d=random.getstate()
e=random.random()
#print(e)
d=random.seed(a=None,version=2)
print(d)
print('Welcome to guess the number game!')
print('Guess the number from 1 to %d' % maxn)
guess = None
while guess != n and n<c and e>1:
    guess = int(input('Your try: '))
    if guess > n:
        print('Too high')
    if guess < n:
        print('Too low')

print('Congratulations, you won!')
