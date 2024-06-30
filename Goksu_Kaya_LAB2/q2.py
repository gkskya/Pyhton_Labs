courses=[('CS 125',3),('HIST 200',4),('PHIL 243',6),('POLS 304',3), ('ENG 101',3)]

total=0
print("First year courses:")
for i in courses: #i is ('CS 125', 3)
    level=i[0][-3] #first element(CS 125) last 3 number
    if level=='1':
        print(i[0])
        total+=[i]
print("Total credit is", total)
