# creart a new file and write some data to it
with open("python7/ending.py", "w") as f:
    f.write("hi wveryon i am learning python \n and python programming language")













with open("python7/ending.py", "r") as f:
    data =f.read()

newdata =data.replace("python","java")
print(newdata)

with open("python7/ending.py","w") as f:
    f.write(newdata)



# find the word 
def check ():
    word=input("enter the word you want to search:")
    with open("python7/ending.py", "r") as f:
        data =f.read()
        if (data.find(word) !=-1) :
            print("yes")
        else:
            print("no")

check()








# waf  to find which line of the file dose the word "learning "accur first
#print -1 if word no found 