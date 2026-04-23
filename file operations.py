#File Operations
#open - read | write | append - close

try:
    file = open('students.txt','r')
except FileNotFoundError:
    print("file is not present")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
'''
with open('students.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
  
with open('students.txt','w+') as file:
    file.write('names')
    file.write('names')
    file.seek(0)
    print(file.readlines())
'''
