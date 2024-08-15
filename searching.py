'''#linear search
#1.procerder method 
l=[5,7,11,33,222,44,56,83,99,111,111,111,11]
target=111
for ind in range(0,len(l)-1):
    if l[ind]==target:
        print(f'{target} available in {ind}')
        break
    
else:
    print(-1)'''
'''1.sequentialbsearch:- checks each element in
the list or arry in order.
2.comparson process:- cimpares each element with
the target until it finds a match or reaches the
end
3.time complexity:-6

