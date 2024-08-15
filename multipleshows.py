def singletonclass(arg):
    l=[]
    def inner():
        if len(l)==0:
            l.append(arg())
        return l[0]
    return inner
@singletonclass
class movie1():
    def __init__(self):
        self.maxtick=100
    def booking(self):
        tick=int(input('enter the no of tickets:'))
        if tick<=self.maxtick:
            self.maxtick -= tick
            print('tickets bookes successflly')
            print(f'{self.maxtick} tickets are available')
        else:
            print('Tickets not available')
@singletonclass
class movie2():
    def __init__(self):
        self.maxtick=100
    def booking(self):
        tick=int(input('enter the no of tickets:'))
        if tick<=self.maxtick:
            self.maxtick -=tick
            print('tickets bookes successflly')
            print(f'{self.maxtick} tickets are available')
        else:
            print('Tickets not available')
@singletonclass
class movie3():
    def __init__(self):
        self.maxtick=100
    def booking(self):
        tick=int(input('enter the no of tickets:'))
        if tick<=self.maxtick:
            self.maxtick -=tick
            print('tickets bookes successflly')
            print(f'{self.maxtick} tickets are available')
        else:
            print('Tickets not available')
def paytm():
    print('the movies available are \n1)Movie1 \n2)Movie2 \n3)Movie3')
    option =int(input('Enter the movie option:'))
    if option==1:
        obj=movie1()
        obj.booking
    elif option==2:
        obj=movie2()
        obj.booking
    elif option==3:
        obj=movie3()
        obj.booking
    else:
        print('enter the valid movie option')
def BMS():
    print('the movies available are \n1)Movie1 \n2)Movie2 \n3)Movie3')
    option =int(input('Enter the movie option:'))
    if option==1:
        obj=movie1()
        obj.booking
    elif option==2:
        obj=movie2()
        obj.booking
    elif option==3:
        obj=movie3()
        obj.booking
    else:
        print('enter the valid movie option')
BMS()
paytm()








        



    
    
