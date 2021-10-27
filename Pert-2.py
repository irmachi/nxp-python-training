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

nama = "Irma"
alamat = "Jakarta"

my_profile = "Nama saya {} dan saat ini sayang bekerja di {}.".format(nama, alamat)

print (my_profile)

#boolean
a = 10
b = 9

if b > a:
    print ("b is greater than a")
else:
    print ("b is less than a")

# #list
# my_list = {}
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append("my string")
# my_list.append(10>9)

# print(my_list)

# print (true and false)

# experience = 3
# level = 1

