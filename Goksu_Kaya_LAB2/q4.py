import random

name=input("Enter a name:")
part1=name[3:7]
num=random.randint(1,900)
print("Random numbber is",num)
password=part1+str(num) #we made type conversion: int to str
print("Generated password:", password)