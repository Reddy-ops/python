#division
'''def Outer(arg):
    pass
    def Inner(a,b):
        if a==0 and b==0:
            print('division is not possible')
        elif b==0:
            arg(b,a)
        else:
            arg(a,b)
    return Inner
@Outer
def rem(v1,v2):
    print(v1%v2)
rem(0,3)
rem(4,5)
rem(2,0)
rem(0,0)'''
#multi
def Outer(arg):
    pass
    def Inner(a,b):
        if a<0 and b<0:
            arg(a,b)
        elif b<0:
            arg(a,(-1)*b)
        elif a<0 :
            arg(a*(-1),b)
        else:
            arg(a,b)
    return Inner
        
    
@Outer
def rem(v1,v2):
    print(v1*v2)
rem(8,2)
rem(4,-5)
rem(-2,-7)
rem(-7,0)
#multi

'''def Outer(arg):
    pass
    def Inner(a,b):
        arg(abs(a),abs(b))
    return Inner
        
    
@Outer
def rem(v1,v2):
    print(v1*v2)
rem(8,2)
rem(4,-5)
rem(-2,-7)
rem(-7,0)'''






