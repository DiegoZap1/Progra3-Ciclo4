from random import randrange,randint,choice,shuffle,sample

num1 = randrange(0,100)
num2 = randint(0,100)

print(num1)
print(num2)

lista = ["coca","agua","te helado","cafe"]
print(choice(lista))

lista2 = [23,5,8,9,1,2,9,6]
shuffle(lista2)
print(lista2)

lista3 = ["zanahoria","lechuga","pepino","repollo"]
print(sample(lista3,2))