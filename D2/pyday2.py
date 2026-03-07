Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
python
name
'python'
type(name)
<class 'str'>
name = input("enter the name:")
enter the name:veeresh
name
'veeresh'
age = int(input("enter the age:"))
enter the age:22
>>> type(age)
<class 'int'>
>>> price = input("enter the price:")
enter the price: 99.99
>>> type(price)
<class 'str'>
>>> price = float(input("enter the price:"))
enter the price:99.99
>>> price
99.99
>>> type(price)
<class 'float'>
>>> "vijay govind srikanth"
'vijay govind srikanth'
>>> "vijay,govind,srikanth".split(',')
['vijay', 'govind', 'srikanth']
>>> names = input("enter the name:")
enter the name:vijay
>>> numbers = input(enter the numbers:").split()
...                 
SyntaxError: unterminated string literal (detected at line 1)
>>> numbers = input ("enter the numbers:").split()
...                 
enter the numbers:1 2 3 4 5 64
>>> numbers
...                 
['1', '2', '3', '4', '5', '64']
>>> numbers = list(map(float,input("enter the numbers:").split()))
...                 
enter the numbers:7 6 4 8 5
>>> numbers
...                 
[7.0, 6.0, 4.0, 8.0, 5.0]
>>> numbers = tuple(map(int,input("enter the numbers:").split()))
...                 
enter the numbers:1 2 3 4 5
>>> numbers
...                 
(1, 2, 3, 4, 5)
>>> numbers = tuple(map(float,input("enter the numbers:").split()))
...                 
enter the numbers:
>>> numbers = set(map(int,input("enter the numbers:").split()))
...                 
enter the numbers:
