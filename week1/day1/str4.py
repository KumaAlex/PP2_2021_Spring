a = "Hello"
b = "World"
c = a + b
print(c)
#HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Hello World

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#I want 3 pieces of item 567 for 49.95 dollars.
#format позволяет принимать инт как строка

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
#I want to pay 49.95 dollars for 3 pieces of item 567
#можно использовать индексы

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#We are the so-called "Vikings" from the north.
#чтобы кавычки выводились без ошибок

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""