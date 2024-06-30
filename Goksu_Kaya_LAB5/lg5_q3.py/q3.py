import time

def searchPattern(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n-m+1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

with open('shark.txt', 'r') as file:
    text = file.read()

pattern = input("Enter a search word: ")

start=time.time()
index = searchPattern(text, pattern)
end=time.time()


if index == -1:
    print("Pattern not found")
else:
    print("First index of {pattern} in the text is: ", index)
    print("Execution time is ", end-start)
