# OPERASI TERHADAP TIPE DATA (STRING)
my_string = "Hello world!"

print (len(my_string))
print (my_string [0:6]) # 0-5
print (my_string [0:8]) # 0-7
print (my_string [0])

my_string = my_string.replace ("world", "friend")
print (my_string)

a = "Hello"
b = "world!"
c = a + b
print (c)

a = "Siap"
b = 86
c = a + " " + str(b)
print (c)