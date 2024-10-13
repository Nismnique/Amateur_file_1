# Make a python program which will take take n number 
# and then take n number of inputs 
# and show them in a list

list= []
serial = 1
n = int(input("Enter Serial Number: "))
while(serial <= n):
    list.append(int(input("Serial Number " + str(serial) + ": " )))
    serial = serial + 1
list.sort()
maximum_num= list.sort()
print(list)
print(max(maximum_num))



# serial < n
# 1 < 55
# 4
# 2 < 55
# 3 < 5
# 4 < 5
# 5 < 5