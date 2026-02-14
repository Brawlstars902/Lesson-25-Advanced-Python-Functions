x=int(input('\nEnter a number:  '))
list1=[]
list2=[]
for i in range (0,x):
    if i%2!=0:
        list1.append(i)
for s in range ((x+1),(x+x)):
    if s%2!=0:
        list2.append(s)
print('\nOdd numbers under your number: ',list1)
print('Odd numbers above your number: ',list2)

fruits=['apple','banana','pear','orange','tomato']
print('\nOriginal fruits:  ',fruits)
fruits=list(map(str.capitalize,fruits))
print('Updated fruits:  ',fruits,'\n')
