a=input ('A ჩაწერე აქ ')
b=input ('B ჩაწერე აქ ')

if int(a)==int(b):
        print("A ტოლია B")
        print('A =', a)
        print('B =', b)
        print('A-B =', int(a)-int(b))
if int(a)-int(b)>0:
        print('A მეტია B ზე')
        print('A =',a)
        print('B =',b)
        print('A-B =',int(a)-int(b))
if int(b)-int(a)>0:
        print('B მეტია A ზე')
        print('A =',a)
        print('B =',b)
        print('B-A =',int(b)-int(a))
print('done')
