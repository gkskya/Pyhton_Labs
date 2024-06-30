cars= {'Honda CR-V': 520000, 'Volkswagen Passat': 750000, 'Toyota Yaris': 500000, 
       'Volkswagen Toureg': 2500000, 'Honda Civic': 650000}

print("First Format", cars)
print("Prices over 800000")
for i in cars:
    if cars[i]>=800000:
        print(i,cars[i])
    else:
        cars[i]=800000
print("Final Format", cars)


thisdict = { 
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964 } 


print(thisdict)
thisdict["year"]=2018
print(thisdict)

'''
for x in thisdict: 
    print(thisdict[x])
'''

for x, y in thisdict.items(): 
    print(x, y)


myfamily = { "child1" : { 
    "name" : "Emil", 
    "year" : 2004 }, 
    "child2" : { 
    "name" : "Tobias", 
    "year" : 2007 },
      "child3" : { 
    "name" : "Linus", 
    "year" : 2011 } }