#file io operations
#1

print("1")
f = open("python6\ending.py", "r")
data =f.read()
print(data)

# read only one line 
# when data is read then line not read
line1=f.readline()
print(line1)
f.close()


# weitin to a file 
# its do overwrite the enture file 
f = open("python6\ending.py", 'w')
f.write("my name is pradip sonagara ")


# apend 
# apend its do add new writing whith a privers note  
f = open("python6\ending.py", 'a')
f.write("\n my father name is ganshyam bhai sonagara ")
f.close()



#r+
# writing and reading 
f =open("python6\ending.py","r+")
print(f.read())
print(f.write("guehfirjfuebrhifjreggj"))




# file io with syntex
with open("python6\ending.py","r") as f:
    data = f.read()
    print(data)


with open ("python6\ending.py","w") as f:
    f.write("new data")
    





# deleting a file 
# modual ( like a code library)
import os 
os.remove("python6\ending.py")





    




























































