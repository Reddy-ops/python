#bubble sort
'''L=[1,2,4,6,7,8,22,44,24,10]
for ind1 in range(len(L)-1,0,-1):
    for ind2 in range(ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)'''
#Patterns
#1.4X4
'''var=4
for i in range(var):
    print('*'*var)'''
#2.triangle
'''var=5
for i in range(1,var+1):
    print('*'*i)
print()'''
#2
'''var=5
for i in range(var,0,-1):
    print('*'*i)
print()'''

#3
'''var=5
sp=var-1
st=1
for i in range(1,var+1):
    print(' '*sp+'*'*st)
    sp-=1
    st+=1
print()'''
#4
'''var=5
sp=0
st=var
for i in range(1,var+1):
    print(' '*sp+'*'*st)
    sp+=1
    st-=1
print()'''
#5
'''var=5
sp=0
st=var
for i in range(1,var+1):
    print(' '*sp+'*'*st)
    sp+=1
    st-=2
print()'''
#6
'''var=7
sp=var-1
st=1
for i in range(1,var+1):
    print(' '*sp+'*'*st)
    sp-=1
    st+=2
print()'''
#7
S = 'abcdefghijklmnopqrstuvwxyz'
col = 4
for ind in range(0,len(S),col):
    print(S[ind:ind + col])







            
