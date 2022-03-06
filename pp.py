Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = "Hello World"
>>> print(x)
Hello World
>>> print(type(x))
<class 'str'>
>>> x = 20
>>> print(type(x))
<class 'int'>
>>> print(x)

20
>>> x = 20.5
>>> print(x)
20.5
>>> print(type(x))
<class 'float'>
>>> x = 1j
>>> print(x)
1j
>>> print(type(x))
<class 'complex'>
>>> x = ["apple", "banana", "cherry"]
>>>  print(x)
SyntaxError: unexpected indent
>>> print(x)
['apple', 'banana', 'cherry']
>>> print(type(x))
<class 'list'>
>>> x = ("apple", "banana", "cherry")
>>> print(x)
('apple', 'banana', 'cherry')
>>> print(type(x))
<class 'tuple'>
>>> x = range(6)
>>> print(x)
range(0, 6)
>>> print(type(x))
<class 'range'>
>>> x = {"name" : "John", "age" : 36}
>>> print(x)
{'name': 'John', 'age': 36}
>>> print(type(x))
<class 'dict'>
>>> x = {"apple", "banana", "cherry"}
>>> print(x)
{'banana', 'cherry', 'apple'}
>>> print(type(x))
<class 'set'>
>>> x = frozenset({"apple", "banana", "cherry"})
>>> print(x)
frozenset({'banana', 'cherry', 'apple'})
>>> print(type(x))
<class 'frozenset'>
>>> x = True
>>> print(x)
True
>>> print(type(x))
<class 'bool'>
>>> x = b"Hello"
>>> print(x)
b'Hello'
>>> print(type(x))
<class 'bytes'>
>>> x = bytearray(5)
>>> print(x)
bytearray(b'\x00\x00\x00\x00\x00')
>>> print(type(x))
<class 'bytearray'>
>>> x = memoryview(bytes(5))
>>> print(x)
<memory at 0x023158B8>
>>> print(type(x))
<class 'memoryview'>
>>> x = str("Hello World")
>>> print(x)
Hello World
>>> print(type(x))
<class 'str'>
>>> x = int(20)
>>> print(x)
20
>>> print(type(x))
<class 'int'>
>>> x = float(20.5)
>>> print(x)
20.5
>>> print(type(x))
<class 'float'>
>>> x = complex(1j)
>>> print(x)
1j
>>> print(type(x))
<class 'complex'>
>>> x = list(("apple", "banana", "cherry"))
>>> print(x)
['apple', 'banana', 'cherry']
>>> print(type(x))
<class 'list'>
>>> x = tuple(("apple", "banana", "cherry"))
>>> print(x)
('apple', 'banana', 'cherry')
>>> print(type(x))
<class 'tuple'>
>>> x = range(6)
>>> print(x)
range(0, 6)
>>> print(type(x))
<class 'range'>
>>> x = dict(name="John", age=36)
>>> print(x)
{'name': 'John', 'age': 36}
>>> print(type(x))
<class 'dict'>
>>> x = set(("apple", "banana", "cherry"))
>>> print(x)
{'banana', 'cherry', 'apple'}
>>> print(type(x))
<class 'set'>
>>> x = frozenset(("apple", "banana", "cherry"))
>>> print(x)
frozenset({'banana', 'cherry', 'apple'})
>>> print(type(x))
<class 'frozenset'>
>>> x = bool(5)
>>> print(x)
True
>>> print(type(x))
<class 'bool'>
>>> x = bytes(5)
>>> print(x)
b'\x00\x00\x00\x00\x00'
>>> print(type(x))
<class 'bytes'>
>>> x = bytearray(5)
>>> print(x)
bytearray(b'\x00\x00\x00\x00\x00')
>>> print(type(x))
<class 'bytearray'>
>>> x = memoryview(bytes(5))
>>> print(x)
<memory at 0x023158B8>
>>> print(type(x))
<class 'memoryview'>
>>> x = 1
>>> y = 2.8

>>> z = 1j
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> x = 1
>>> y = 35656222554887711
>>> z = -3255522
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> x = 1.10
>>> y = 1.0
>>> z = -35.59
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x = 35e3
>>> y = 12E4
>>> z = -87.7e100
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x = 1    # int
>>> y = 2.8  # float
>>> z = 1j   # complex
>>> a = float(x)
>>> b = int(y)
>>> c = complex(x)
>>> print(a)
1.0
>>> print(b)
2
>>> print(c)
(1+0j)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> import random
>>> print(random.randrange(1, 10))
7
>>> x = int(1)   # x will be 1
>>> y = int(2.8)
>>> z = int("3")
>>> print(x)
1
>>> print(y)
2
>>> print(z)
3
>>> x = float(1)
>>> y = float(2.8)
>>> z = float("3")
>>> w = float("4.2")
>>> print(x)
1.0
>>> print(y)
2.8
>>> print(z)
3.0
>>> print(w)
4.2
>>> x = str("s1")
>>> y = str(2)
>>> z = str(3.0)
>>> print(x)
s1
>>> print(y)
2
>>> print(z)
3.0
>>> print("Hello")
Hello
>>> print('Hello')
Hello
>>> a = "Hello"
>>> print(a)
Hello
>>> a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
>>> print(a)
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
>>> a = "Hello, World!"
>>> print(a[1])
e
>>> for x in "banana":
	print(x)

	
b
a
n
a
n
a
>>> a = "Hello, World!"
>>> print(len(a))
13
>>> txt = "The best things in life are free!"
>>> print("free" in txt)
True
>>> txt = "The best things in life are free!"
if "free" in txt:
	
SyntaxError: multiple statements found while compiling a single statement
>>> txt = "The best things in life are free!"
>>> if "free" in txt:
	print("Yes, 'free' is present.")

	
Yes, 'free' is present.
>>> b = "Hello, World!"
>>> print(b[2:5])
llo
>>> b = "Hello, World!"
>>> print(b[:5])
Hello
>>> b = "Hello, World!"
>>> print(b[2:])
llo, World!
>>> b = "Hello, World!"
>>> print(b[-5:-2])
orl
>>> a = "Hello, World!"
>>> print(a.upper())
HELLO, WORLD!
>>> a = "Hello, World!"
>>> print(a.lower())
hello, world!
>>> a = " Hello, World! "
>>> print(a.strip())
Hello, World!
>>> a = "Hello, World!"
>>> print(a.replace("H", "J"))
Jello, World!
>>> a = "Hello, World!"
>>> print(a.split(","))
['Hello', ' World!']
>>> a = "Hello"
>>> b = "World"
>>> c = a + b
>>> print(c)
HelloWorld
>>> a = "Hello"
>>> b = "World"
>>> c = a + " " + b
>>> print(c)
Hello World
>>> quantity = 3
>>> itemno = 567
>>> price = 49.95
>>> myorder = "I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity, itemno, price))
I want 3 pieces of item 567 for 49.95 dollars.
>>> quantity = 3
>>> itemno = 567
>>> price = 49.95
>>> myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
>>> print(myorder.format(quantity, itemno, price))
I want to pay 49.95 dollars for 3 pieces of item 567.
>>> \'
SyntaxError: unexpected character after line continuation character
>>> txt = 'It\'s alright.'
>>> print(txt)
It's alright.
>>> txt = "This will insert one \\ (backslash)."
>>> print(txt)
This will insert one \ (backslash).
>>> txt = "Hello\nWorld!"
>>> print(txt)
Hello
World!
>>> txt = "Hello\nWorld!"
>>> print(txt)
Hello
World!
>>> txt = "Hello\rWorld!"
print(txt)
SyntaxError: multiple statements found while compiling a single statement
>>> print(txt)
Hello
World!
>>> txt = "\110\145\154\154\157"
>>> print(txt)
Hello
>>> txt = "\x48\x65\x6c\x6c\x6f"
>>> print(txt)
Hello
>>> print(10 > 9)
True
>>> print(10 == 9)
False
>>> print(10 < 9)
False
>>> a = 200
>>> b = 33
>>> if b > a:
	  print("b is greater than a")
	  else:
		  
SyntaxError: invalid syntax
>>>   print("b is not greater than a")
SyntaxError: unexpected indent
>>> print("b is not greater than a")
b is not greater than a
>>> print(bool("Hello"))
True
>>> print(bool(15))
True
>>> x = "Hello"
>>> y = 15
>>> print(bool(x))
True
>>> print(bool(y))
True
>>> bool("abc")
True
>>> bool(123)
True
>>> bool(["apple", "cherry", "banana"])
True
>>> bool(False)
False
>>> bool(None)
False
>>> bool(0)
False
>>> bool("")
False
>>> bool(())
False
>>> bool([])
False
>>> bool({})
False
>>> class myclass():
	  def __len__(self):
	       return 0
	myobj = myclass()
	
SyntaxError: unindent does not match any outer indentation level
>>> print(bool(myobj))

Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    print(bool(myobj))
NameError: name 'myobj' is not defined
>>> myobj = myclass()
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    myobj = myclass()
NameError: name 'myclass' is not defined
>>> def myFunction() :
	  return True
	print(myFunction())
	
SyntaxError: unindent does not match any outer indentation level
>>> def myFunction() :
	  return True

	
>>> print(myFunction())

True
>>> class myclass():
	  def __len__(self):
		      return 0

		
>>> myobj = myclass()
>>> print(bool(myobj))
False
>>> def myFunction() :
	  return True

	
>>> if myFunction():
	  print("YES!")

	  
YES!
>>> else:
	
SyntaxError: invalid syntax
>>>   print("NO!")
SyntaxError: unexpected indent
>>>  print("NO!")
SyntaxError: unexpected indent
>>> x = 200
>>> print(isinstance(x, int))
True
>>> x = 5
>>> y = 3
>>> print(x + y)
8
>>> x = 5
>>> y = 3
>>> print(x - y)
2
>>> x = 5
>>> y = 3
>>> print(x * y)
15
>>> x = 5
>>> y = 3
>>> print(x * y)
15
>>> x = 12
>>> y = 3
>>> print(x / y)
4.0
>>> x = 5
>>> y = 2
>>> print(x % y)
1
>>> x = 2
>>> y = 5
>>> print(x ** y)
32
>>> x = 15
>>> y = 2
>>> print(x // y)
7
>>> x = 5
>>> print(x)
5
>>> x = 5
>>> x += 3
>>> print(x)
8
>>> x = 5
>>> x -= 3
>>> print(x)
2
>>> x = 5
>>> x *= 3
>>> print(x)
15
>>> x = 5
>>> x /= 3
>>> print(x)
1.6666666666666667
SyntaxError: invalid syntax
>>> x = 5
>>> x%=3

>>> print(x)
2
>>> x = 5
>>> x//=3
>>> print(x)
1
>>> x = 5
>>> x **= 3
>>> print(x)
125
>>> x = 5
>>> x &= 3
>>> print(x)
1
>>> x = 5
>>> x |= 3
>>> print(x)
7
>>> x = 5
>>> print(x > 3 and x < 10)
True
>>> x = 5
>>> print(x > 3 or x < 4)
True
>>> x = 5
>>> print(not(x > 3 and x < 10))
False
>>> x = ["apple", "banana"]
>>> y = ["apple", "banana"]
>>> z = x
>>> print(x is z)
True
>>> print(x is y)
False
>>> print(x == y)
True
>>> x = ["apple", "banana"]
>>> print("banana" in x)
True
>>> x = ["apple", "banana"]
>>> print("pineapple" not in x)
True
>>> thislist = ["apple", "banana", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist = ["apple", "banana", "cherry", "apple", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry', 'apple', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
>>> print(len(thislist))
3
>>> list1 = ["apple", "banana", "cherry"]
>>> list2 = [1, 5, 7, 9, 3]
>>> list3 = [True, False, False]
>>> print(list1)
['apple', 'banana', 'cherry']
>>> print(list2)
[1, 5, 7, 9, 3]
>>> print(list3)
[True, False, False]
>>> list1 = ["abc", 34, True, 40, "male"]
>>> print(list1)
['abc', 34, True, 40, 'male']
>>> mylist = ["apple", "banana", "cherry"]
>>> print(type(mylist))
<class 'list'>
>>> thislist = list(("apple", "banana", "cherry"))
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
>>> print(thislist[2:5])
['cherry', 'orange', 'kiwi']
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist[1] = "blackcurrant"
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
>>> thistuple = ("kiwi", "orange")
>>> thislist.extend(thistuple)
>>> print(thislist)
['apple', 'banana', 'cherry', 'kiwi', 'orange']
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist = ["apple", "banana", "cherry"]
>>> i = 0
>>> while i < len(thislist):
	  print(thislist[i])
	    i = i + 1
	    
SyntaxError: unexpected indent
>>> 
>>> thislist = ["apple", "banana", "cherry"]
>>> for x in thislist:
	  print(x)

	  
apple
banana
cherry
>>> fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
>>> newlist = []
>>> for x in fruits:
	  if "a" in x:
	 newlist.append(x)
	 
SyntaxError: unindent does not match any outer indentation level
>>> fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
>>> newlist = []

>>> for x in fruits:
	  if "a" in x:
		    newlist.append(x)

>>> 
>>> print(newlist)

['apple', 'banana', 'mango']
>>> def myfunc(n):
	  return abs(n - 50)

	
>>> thislist = [100, 50, 65, 82, 23]
>>> thislist.sort(key = myfunc)
>>> print(thislist)
[50, 65, 23, 82, 100]
>>> thislist = ["apple", "banana", "cherry"]
>>> mylist = list(thislist)
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> list1 = ["a", "b" , "c"]
>>> list2 = [1, 2, 3]
>>> 
>>> for x in list2:
	  list1.append(x)

	  
>>> print(list1)
['a', 'b', 'c', 1, 2, 3]
>>> 
