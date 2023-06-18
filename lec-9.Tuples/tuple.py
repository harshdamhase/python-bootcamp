myBasket = ("Apple","Banana","Grapes","Orange","Apple")
listmyBasket = list(myBasket)
listmyBasket[0] = "cherry"
myBasket = tuple(listmyBasket)
print(myBasket)


# ('cherry', 'Banana', 'Grapes', 'Orange', 'Apple')
