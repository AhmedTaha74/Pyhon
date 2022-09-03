#  -------------------------------
#  Information About File
#  License
#  Who Created The File
#  When The File Created
#  Why The File Created
#  Write Beside The Programming Line
#  Write Before The Programming Line
#  Prevent Code From Run
#  -------------------------------


print("I Love Python")  #  This is Inline Comment
print("Programming")  #  I Used This Method Because of Bla Bla Bla
print("Programming")  #  If You Used Test Method Will Through Error


# this is not comment 
"""
This is
Not
Multiple
Line
Comments
"""

#  ----------------------------
#  type()
#  All Data in Python is Object
#  ----------------------------

print(type(10))  #  int => Integer
print(type(100))  #  int => Integer
print(type(-50))  #  int => Integer

print(type(100.9))  #  float => Floating Point Number
print(type(1.0950950))  #  float => Floating Point Number
print(type(-100.9595))  #  float => Floating Point Number

print(type("Hello Python"))  #  str => String

print(type([1, 2, 3, 4, 5]))  #  list => List

print(type((1, 2, 3, 4, 5)))  #  tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  #  dict => Dictionary

print(type(2 == 20))  #  bool => Boolean


#  --------------------------------------
#  -- Variables --
#  ---------------
#  Syntax => [Variable Name] [Assignment Operator] [Value]
# 
#  Name Convention and Rules
#  [1] Can Start With (a-z A-Z) Or Underscore
#  [2] You Cannot With Num Or Special Characters
#  [3] Can Include (0-9) Or Underscore
#  [4] Cannot Include Special Characters
#  [5] Name is Not Like name [ Case Sensitive ]
#  --------------------------------------

name = "Osama Elzero"  #  Single Word => Normal
myName = "Osama Elzero"  #  Two Words => camelCase
my_name = "Osama Elzero"  #  Two Words => snake_case

print(name)
print(myName)
print(my_name)

# variable
x = 5
y = "test"
z = 4

print(x)
print(y)
print(z)
print(x+z)

x = 4       #  x is of type int
x = "Sally" #  x is now of type str
print(x)




# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"

#  Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"


# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
# Example
# x, y, z = "Orange", "Banana", "Cherry"

#  print(x)
#  print(y)
#  print(z)


x = "Python "
y = "is "
z = "awesome"
print(x , y ,z)




#  Declare a variable and initialize it
f = 101
print (f)


#  ---------------
#  -- Variables --
#  ---------------
#  Source Code : Original Code You Write it in Computer
#  Translation : Converting Source Code Into Machine Language
#  Compilation : Translate Code Before Run Time
#  Run-Time : Period App Take To Executing Commands
#  Interpreted : Code Translated On The Fly During Execution
#  --------------------------------------------------------

#  Reserved Words
help("keywords")

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

print("Hello\ttest")

print("123\r321")
print("\x41\x48\x4D\x45\x44 \x54\x41\x48\x41")

savings = 100
result = 100 * 1.10 ** 7
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

#  -------------------
#  -- Concatenation --
#  -------------------

First_Name = "Ahmed "
Last_Name  = "Taha"
Name = First_Name  + "\n" + Last_Name
print(Name)
print(First_Name + " " + Last_Name)
#  print("Hello " + 1)  #  Error

#  -------------
#  -- Strings --
#  -------------
First_string  = "Test_1"
Second_string = 'Test_2'
print(First_string)
print(Second_string)


First_string  = "Test 'one' "
Second_string = 'Test "two" '

print(First_string)
print(Second_string)

print('''First
Second 'Test' "Test"
Third''')

print("""First
Second "Test" \\\ 'Test'
Third""")


#  ---------------------------------
#  Strings Indexing & Slicing
#  [1] All Data in Python is Object
#  [2] Object Contain Elements
#  [3] Every Element Has Its Own Index
#  [4] Python Use Zero Based Indexing ( Index Start From Zero )
#  [5] Use Square Brackets To Access Element
#  [6] Enable Accessing Parts Of Strings, Tuples or Lists
#  ---------------------------------

#  Indexing ( Access Single Item )

myString = "Access Single Item"
print(myString[::4])


# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

#  ---------------------
#  -- Strings Methods --
#  ---------------------

#  strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "# # # # # I Love Python# # # # "
print(a.strip("# "))
print(a.rstrip("# "))
print(a.lstrip("# "))

a = "@# @# @# I Love Python@# @# @# "
print(a.strip("@# "))
print(a.rstrip("@# "))
print(a.lstrip("@# "))

#  title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

#  capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

#  zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

#  upper()

g = "osama"

print(g.upper())

#  lower()

h = "OSama"

print(h.lower())

#  ---------------------
#  -- Strings Methods --
#  ---------------------

#  split() =>  separator and step و بتستقبل حاجه اسمها list بتفصل الكلام و ترجعه في    
#  rsplit()

#  default
a = "I Love Python and PHP and MySQL"
print(a.split())

#  separator
a = "I_Love_Python_and_PHP_and_MySQL"
print(a.split("_"))

#  separator and step  
a = "I_Love_Python_and_PHP_and_MySQL"
print(a.split("_" , 3) )

#  separator and step  
a = "I_Love_Python_and_PHP_and_MySQL"
print(a.rsplit("_" , 3) )


#  center() بتضيف قبل و بعد الكلام اي حاجه انت عايزها 
#  لازم تحدد عدد الحروف اللي هضيفها و عدد حروف الكلمه نفسها 
#  وبعدين الحرف اللي عايز تضيفه 

v = "Ahmed"
print(v.center(11 ,"*"))
print(v.center(15, "@"))  #  @


#  count() بتعد الكلمه موجوده كام مره في النص 
#  لازم تحدد الكلمه اللي هيدور عليها 
#  count(word, start, end)) 

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))
print(f.count("PHP" , 0 , 10))

#  swapcase() small => capital بتبدل الحرف 
g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())


#  startswith("char, start , end") بتحقق من اول حرف لو طلع هو بيرجع ترو مكنش فولس
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

#  endswith("char, start , end") بتحقق من اخر حرف لو طلع هو بيرجع ترو مكنش فولس
print("\n")
print(i.endswith("n"))
print(i.endswith("S"))
print(i.endswith("n", 7,-1))


#  ---------------------
#  -- Strings Methods --
#  ---------------------

#  index(SubString, Start, End) return the index  

a = "I Love Python"
print(a.index("n"))
print(a.index("o" , 0 ,15 ))

#  find() =>  index() بس الاختلاف لو الحرف اللي بتبحث عنه مش موجود بيرجع -1
b = "I Love Python"
print(b.find("lo"))

#  rjust("width, fill char")   ||   ljust("width, fill char")   ||   center("width, fill char")  =>  بيضيفوا قبل الكلمه

c = "Ahmed"
print(c.center(15,"!"))

#  rjust() add fill char from right
print(c.rjust(10,"!"))

#  ljust() add fill char from left
print(c.ljust(10,"!"))

 #  splitlines() list  بقدر اقسم السطور اللي عندي و اخزمهم في 

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

d = "Ahmed \n Taha \n Ahmed"
print(d.splitlines())

# expandtabs("number spaces")  add tab betweens the words 
f = " I\t  Love\t Python\t  And \t 3G "
print(f.expandtabs(5))

# islower() check the text is lower 
g = "my name Ahmed"
print(g.islower())

# islower() check the text is upper 
g = "MY NAME AHMED TAHA"
print(g.isupper())

# istitle() check the text is title
h = "Ahmed Taha 89Fci"
print(h.istitle())

# isspace() is checking there the space  
print("\n")
s = " " 
print(s.isspace())
 
print("\n")
s = "" 
print(s.isspace())

# isidentifier()  check the text can used to a variable 

v  = "_ahmed_taha"
b  = "Ahmed89taha"
n  = "#ahmed-taha"
m  = "89ahmedtaha"

print("\n")
print(v.isidentifier())
print(b.isidentifier())
print(n.isidentifier())
print(m.isidentifier())

print("\n")
x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())


print("\n")
u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())

# replace("old word" , "new word" , count ) replace the old word to new word 
name = "ahmed taha ahmed"
print(name.replace("ahmed", "taha"))
print(name.replace("ahmed", "taha" , 1))


# join(Iterable) => split  دي عكس 
name = ["ahmed" , "taha" , "ahmed"]
print("_".join(name))

# ------------------------------------
# -- Strings Formatting (Old Way)-----
# ------------------------------------

name = "Ahmed"
age = 20
gpa = 3

print("My Name is: " + name)
# print("My Name is: " + name + " " + age) # type error


# %s  => String
# %d  => Number 
# %f  => Float

print("My Name is: %s"  %"ahmed")
print("My Name is: %s"  %name)
print("My Name is: %d"  %age)
print("My Name is: %f"  %gpa)
print("my name is  %s and my age %d and my gpa  is : (%f) " %(name,age,gpa))


Name = "Ahmed Taha"
Age  = 20
Job  = "Data Analyst" 
Salary = 5000
print("My Name is %s and Iam %d years and my job %s" %(Name,Age,Job))

# Control Floating Point Number
print("my name is  %s and my age %d and my gpa  is : (%.2f) " %(name,age,gpa))
print("My Name is %s and Iam %d years and my salary  %.3f" %(Name,Age,Salary))


# Truncate String
Name = "Ahmed Taha"
print("My name is %.5s" %Name)


# ------------------------------------
# -- Strings Formatting (New Way)-----
# ------------------------------------

# {:s}  => String
# {:d}   => Number 
# {:f}   => Float
print("\n")
print("My Name is: {:s}"  .format("ahmed"))
print("\n")
print("My Name is: {:s}"  .format(name))
print("\n")
print("My Name is: {:d}"  .format(age))
print("\n")
print("My Name is: {:f}"  .format(gpa))
print("\n")
print("my name is   {:s} and my age {:d} and my gpa  is : ({:f}) " .format(name,age,gpa))
print("\n")

Name = "Ahmed Taha"
Age  = 20
Job  = "Data Analyst" 
Salary = 5000
print("\n")
print("My Name is {:s} and Iam {:d} years and my job {:s}" .format(Name,Age,Job))
print(f"My Name is {Name} and Iam {Age} years and my job {Job}")
print("\n")

# Control Floating Point Number
print("\n")
print("my name is  {:s} and my age {:d} and my gpa  is : {:f} " .format(name,age,gpa))
print("\n")
print("My Name is {:s} and Iam {:d} years and my salary  {:.2f}" .format(Name,Age,Salary))


# Truncate String
Name = "Ahmed Taha"
print("\n")
print("My name is {:.5s} " .format(Name))
print("\n")


# Money Format
myMoney = 500162350198
print("My Money in Bank Is: {:d}"  .format(myMoney))
print("My Money in Bank Is: {:,d}"  .format(myMoney))
print("My Money in Bank Is: {:_d}"  .format(myMoney))

# ReArrange Items
a = 1
b = 2
c = 3
print("one: {2} , \t Two : {0} , \t Three {1}" .format(a,b,c))



a = 1000
b = 2000
c = 3000
print("one: {2:f} , \t Two : {0:f} , \t Three {1:f}" .format(a,b,c))
print("one: {0:.3f}  \t Two : {1:.3f}  \t Three {2:.3f}" .format(a,b,c))

# List

test = "test " * 8
print(test )


print([1,2,3] * 3)


# -------------
# -- Numbers --
# -------------

# Integer =>  رقم صحيح سواء موجب أو سالب 

print(type(1))
print(type(-1))
print(type(1111))

print("\n")

# Float (Floating point number)  =>  رقم غير صحيح يعني يحتوي علي كسور سواء موجب او سالب 

print(type(1.006))
print(type(-1.549))
print(type(1454.123456789))
print(type(-1454.123456789))
print("\n")
 
# Complex  (Real Number + imaginary Number)

print(10+5j)
print(type(10+5j))

Complex = 5+9j
print(f"Real Num is :{Complex.real}")
print(f"imaginary Num is :{Complex.imag}")
print("\n")


# [1] You Can Convert From Int To Float or Complex

print(100)
print(float(100))
print("\n")


# [2] You Can Convert From Float To Int or Complex

print(10.0)
print(int(10.0))

# [3] You Can Convert From Float To Int or Complex

print(10.05)
print(complex(10.05))

# [4] You Cannot Convert Complex To Any Type


print(5+5j)
# print(int(5+5j))



# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# [+] Addition

print(9 + 9)
print(9.5 + 9)
print(-91 + 900)


# [-] Subtraction

print(9 - 9)
print(9.5 - 9)
print(91 - 900)

# [*] Multiplication

print(9 * 9)
print(9.5 * 9)
print(-12 * 9)

# [/] Division

print(-9 / 9)
print(9.5 / 9.5)
print(12 / 2)

# [%] Modulus

print(3 % 2)
print(4 % 2)
print(9 % 2)

# [**] Exponent

print(3 ** 2)
print(-4 ** 2)
print(9.5 ** 2)

# [//] Floor Division  => بتاخد  الرقم الصحيح بعد  القسمه 

print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7
print([1,2,3] * 3)


# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------


List = ["ahmed",89 , "taha", True ,True, 89.63]
print(List)
print(type(List))
print(List[0])
print(List[-1])
# slicing 
print(List[-3:-1])
print(List[0:3])
print(List[0:])
print(List[:-1])
# indexing
print(List[::3])
print(List[::-2])
List[3] = "Ahmed"
print(List[3])
List[0] = "Ahmed"
print(List[0:4])
List[1:4] = ["Test"] 
print(List)

# -------------------
# -- Lists Methods --
# -------------------

# append()  list بتضيف عنصر في نهايه  

name = ["Ahmed","Taha", "Ahmed"]
name.append("El bastawesy")
print(name)
name.append(89.6)
print(name)
name.append(True)
print(name)

name = ["Ahmed","Taha", "Ahmed"]
bro  = ["mostafa", "Taha", "Ahmed"]
name.append(bro)
print(name)
print(name[3][0])



# extend()  =>  list بتعمل دمج ل  
name  = ["Ahmed","Taha", "Ahmed"]
bro   = ["mostafa", "Taha", "Ahmed"]
bro_2 = ["mohmed" ,"taha", "ahmed"] 
name.extend(bro)
name.extend(bro_2)
print(name)

# remove() list بتزيل اول كلمه من 
bro  = ["mostafa", "Taha", "Ahmed"]
bro.remove("Ahmed")
print(bro)

# sort()   من حيث الاكبر او الاصغر  list بتعمل فرز 

y = [1, 2, 100, 120, -10, 17, 29]
y.sort()
print(y)
 
 # sort(reverse = True || False)
 
y.sort(reverse=True)  # Sort اللي اتعملها  list بتعكس 
print(y)


# reverse() =>  list بتعكس 

y = [1, 2, 100, 120, -10, 17, 29]
y.reverse()
print(y)


# -------------------
# -- Lists Methods --
# -------------------

# clear()  =>  list من items بتفضي كل 

a = [1,2,8,"fd",True]
a.clear()
print(a)

# copy()  =>  تانيه list ل list اللي في items بتنسخ كل  

b = [1,2,3,4,5,6,7]
c = b.copy()
b.append(8)
print(b) # Main List 
print(c) # Copied List 



# count() => كام مره items بتعد  
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))


# index()  => Return index  item

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ahmed"))

# insert("index","value") add before Item  that you selected
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0,0)
print(f)

# pop(index) remove item from list and return the list 
g = [1, 2, 3, 4, 5, "A", "B"] 
g.pop(0)
print(g)