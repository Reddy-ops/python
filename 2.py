#factorial
'''def Fact(num):
    if num==0 or num==1:
        return 1
    return num*Fact(num-1)
num=5
print(Fact(num))

#if we do reverse
def ram(sv,num):
    if sv==num:
        return 1
    return sv*ram(sv+1,num)
sv=1
rint(ram(sv,num))'''
'''#Harshad number
def d_sum(var):
    if var==0:
        return 0
    return (var%10)+d_sum(var//10)
var=156
print('Harshad number'if var%d_sum (var)==0 else ('not Harshad number'))
'print(complex(8))'''
'''for i in range(5,0,-1):
    for j in range (i,-1):
        print(j,end='')

    print()'''
'''def prime(num):
    lv=int(num**(0.5)+1)
    for fa in range (2,lv):
        if num%fa==0:
            return('not a prime ')
        
    return print('prime')
print(prime(51))'''
'''#factorial
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
num=7
print(f'the factorial of num{fact(num)}')'''
#happy number
'''def squre(num,dsum=0):
    while num!=0:
        dsum+=(num%10)**2
        num=num//10
    return dsum
def check(num):
    while num>9:
        num=squre(num)
    return num==1 or num==7
num=123
check(num)
print('happy number'if check(num)else 'not  a happy number')
