li = ['1','2','3','4','5']
li1 = []
for i in li:
    li1.append(2*i)
    print(li1)
#________________________________________
    
li = ['a','b','c','d','e','f','g']
li.reverse()
li.insert(7,'h')
li.remove('h')
li.pop()
li2=li[2]
li1=li.pop(5)
a=li2+li1
for i in (li):
   print(i,end='')

#_____________
   
a = {1,2,3,4,5}
b = { 2,3,4}
#c = a & b
c = a | b
print(c)


#_______________

marks = {'a':10,'ab':20,'ac':30,'ad':40}
print(marks['ab'])