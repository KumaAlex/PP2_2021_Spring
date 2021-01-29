a = "Hello, World!"
print(a.upper())
#HELLO, WORLD!

a = "Hello, World!"
print(a.lower())
#hello, world!

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#удаляет пробелы в начале и в конце

a = "Hello, World!"
print(a.replace("H", "J"))
#Jello, World!
#Меняет местами

a = "Hello, World!"
b = a.split(",")
print(b)
#['Hello', ' World!']
#разбивает на слова