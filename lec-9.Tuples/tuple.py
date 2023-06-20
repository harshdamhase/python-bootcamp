myBasket = ("Apple","Banana","Grapes","Orange","Apple")
listmyBasket = list(myBasket)
listmyBasket[0] = "cherry"
myBasket = tuple(listmyBasket)
print(myBasket)


# ('cherry', 'Banana', 'Grapes', 'Orange', 'Apple')


pythonStudent = ("Saurabh","pooja","saurabh","Tushar","Harshal")
print(pythonStudent.count('Tushar'))


pythonStudent = ("Saurabh","pooja","saurabh","Tushar","Harshal")
print(pythonStudent.index('Tushar'))