'''#BUBBLE SORT
#1.Bubble sort is used to sort the list of elements in lower value to higher value
L=[12,13,53,62,77,69,111]
for i1 in range (len(L)-1,0,-1):
    for i2 in range(i1):
        if L[i2]>L[i2+1]:
            L[i2],L[i2+1]=L[i2+1],L[i2]
print(L)
#A,B=B,A(L[i2],L[i2+1]=L[i2+1],L[i2])'''
#-----------------------------------------------------------------
'''Selection Sort
Selection sort repeatedly selects the smallest element from the unsorted
portion of the list and swaps it with the first unsorted element until
the entire list is sorted.'''
'''#Program
L=[12,13,53,62,77,69,111]
for ind1 in range(len(L)-1):
    imag=ind1
    for ind2 in range (ind1+1,len(L)):
        if L[imag]>L[ind2]:
            imag=ind2
    L[ind1],L[ind2]=L[ind2],L[ind1]
print(L)'''
