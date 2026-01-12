5678
'''1.
a=3
b=5
if ((a%2==1) and (b<3)):
       print('TRUE')
else:
       print('FALSE') 
if ((a!=7) or (b>=2)):
        print('TRUE')
else:
       print('FALSE') 
if ((a<10)) or (b>5):
       print('TRUE')
else:
       print('FALSE') 
if ((a>5) and (not(b==2))):
       print('TRUE')
else:
       print('FALSE') 
2.

for i in range(1, 11):
    print(i*'*')



3
right=5678
#print('password should be 5678')
for i in range(1,4):
    
    password=int(input('Enter a pasword:'))
    if password==right:
            print('access granted')
            exit()
    else:
        print('try again')
    print('you have been locked out')
    break'''
4.
for i in range(1, 15):
    if i%2==0:
        print(i, end='')
    else:
        continue 
    break
5.
def area(radius):
    pi=3.14
    area_circle=pi*(radius**2)
    return area_circle
circle_area=area(14)
print(f' the area is {circle_area}')


def diff(num1, num2):
        absolute_difference=(abs(num1-num2))
        return absolute_difference
        
the_difference=diff(4, 9)
print(f'absolute difference is {the_difference}')
6.
i=5
while i>0:
    print(i, end='')
    i-=1
i=2
while True:
    print(i, end='')
    i+=2
    if i>10:
        break
sum=0
for i in range(1, 6):
    sum+=i
print('Total=', sum)

for i in range(1, 11):
    if i%2==0:
        continue
    print(i, end='')
i=10
while i>=0:
    if i==5:
        break
    print(i, end='')
i=3
while True:
    print(f'Step {i}')
    i+=1
    if i>6:
        break
for x in range(1, 3):
    for y in range(1, 4):
        print(f'({x}, {y})', end='')
    print()
num=1
sum=0
while num <=10:
    if num % 4==0:
        sum +=num
    num +=1 
print('sum=', sum)

7.
list=[4, 3, 6, 7, 8]
print(list[2])

print('x')

