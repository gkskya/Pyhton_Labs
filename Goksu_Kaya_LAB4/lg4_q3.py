'''
def longWords(lst):
    words=[]
    for i in lst:
        if len(i)>5:
            words.append(i)
    return words
    
#main part
arr=[]
str=input("Enter a word:")
while str != 'STOP' :
    arr.append(str)
    str=input("Enter a word:")

print("Words size greater than 5", longWords(arr))
'''

def longWords(lst):
    return [word for word in lst if len(word)>5]
    
#main part
arr=[]
str=input("Enter a word:")
while str != 'STOP' :
    arr.append(str)
    str=input("Enter a word:")

print("Words size greater than 5", longWords(arr))

