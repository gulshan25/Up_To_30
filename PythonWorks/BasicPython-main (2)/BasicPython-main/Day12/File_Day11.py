"""
The syntax to open a file object in Python is: 
file_object  = open(“filename”, “mode”) 

where file_object is the variable to add the file object. 

The second argument you see – mode – tells the interpreter and developer which way the file will be used.
Mode


Including a mode argument is optional because a default value of ‘r’ will be assumed if it is omitted. The ‘r’ value stands for read mode, which is just one of many. 

The modes are: 

    ‘r’ – Read mode which is used when the file is only being read 
    ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
    ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
    ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file 

So, let’s take a look at a quick example. 
"""

#open a file for write mode
file = open("pybatch6.txt","w") 

file.write("Hello World") 
file.write("This is our new text file") 
file.write("and this is another line.") 
file.write("Why? Because we can.") 

file.write("\nHello World\n") 
file.write("This is our new text file\n") 
file.write("and this is another line.\n") 
file.write("Why? Because we can.\n") 
file.write("End of file in write mode.\n") 

file.close()

#open a file for read mode
file = open("pybatch6.txt", "r") 

#read entire file
print(file.read())

#Read first 8 character
print(file.read(8))

#Read first line
print(file.readline()) 

#Read first 3 character of first line
print(file.readline(3)) 

#read entire file as a list
print(file.readlines()) 
file.close() 


#open a file for read mode
file = open("pybatch6.txt", "r") 

s=file.readlines()
for line in s: 
	print(line) 

file.close() 


#open a file for read mode
file = open("pybatch6.txt", "r")  
for line in file: 
	print(line)
	
file.close() 

#open a file for append mode
file = open("pybatch6.txt", "a")  
file.write("We Meet Again World") 	
file.close() 

#open a file for append mode
with open("pybatch6.txt", "a") as file:
	file.write("We Meet Again World 2") 	
	file.close() 

#open a file for read mode and split array
with open("pybatch6.txt", "r") as f:
    data = f.readlines()
    f.close()
 
for line in data:
	words = line.split()
	print(words)    


#open a file for read mode and split array
file = open("pybatch6.txt", "r") 

l=1
for i in file:
	print(l,'.',i)
	l=l+1
file.close() 



