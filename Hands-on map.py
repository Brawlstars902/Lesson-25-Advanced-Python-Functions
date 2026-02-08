f=[3,4,7]
g=[6,5,1]

result= map(lambda x,y: x+y, f,g)
print('\nAddition of 2 lists:  ')
print(list(result))

nums=[1,2,3,4,5]
def sq(n):
    return n*n

square=list(map(sq,nums))
print('\nSquare of numbers in list:')
print(square,'\n\n\n')