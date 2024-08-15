                              #number programs


#1.prime number
'''l=int(input())
f_count=0
for i in range(1,l+1):
    if l%i==0:
        f_count+=1
if f_count==2:
    print('yes')
else:
    print('no')'''
#prime number
l=int(input())
f_count=1
for i in range(1,l+1):
    f_count=f_count*i
print(f'{f_count } is the factorial of {l}')
