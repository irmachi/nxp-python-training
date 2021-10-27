# i = 1
# while i<6:
#     print(i)

# for i in range (5):
#     if i % 2 == 0:
#         continue
#     print (i)

# for i in range (10):
#     if i == 2 or i ==3 :
#         continue
#     print (i)

# for i in range (10):
#     print ("i: {}". format(i))
#     for j in range(3):
#         print("j: {}". format (j))

# for baris in range (5):
#     for kolom in range(5):
#         print("{}.{}". format(baris+1, kolom+1), end=" ")
#     print()

x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x:
    for j in y:
        if i == j:
            z = z+1

print(z)



