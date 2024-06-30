'''
Multiline Comment

#single line comment
sum=0
arr=[]
for i in range(0,5):
    num=int(input("Enter a number:"))
    sum+=num
    arr.append(num)

avg=sum/5
print("Average is", avg)
print("Original format of array:",arr)
arr.sort()
print("Sorted format",arr)
arr.reverse()
print("Reverse format",arr)
'''

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") 
print(thistuple[2:5])

x = ("apple", "banana", "cherry") 
y = list(x) 
y[1] = "kiwi"
x = tuple(y) 
print(x)