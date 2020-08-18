a = 5
print(a, "is of type", type(a))

x=[0]*10005;              #inisialisasi array 0 sebanyak 10005; x[0]=0
x[1]=1;                   #x[1]=1
 
for j in range(2,10001):
      x[j]=x[j-1]+x[j-2]  # Fibonacci
print(x[10000]," ")

x = [5,10,15,20,25,30,35,40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])
x = [1,2,3]
x[2]=4
x
print(x)
x.append(5)
x
print(x)
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
print("Hello World"); print("Welcome to Python")
s = "Hello World!"
print(s[4])
print(s[6:11])
t = (5,'program', 1+3j)
t[1]
t[0:3]
a = 5
print('The value of a is', a)
name = "John"
print("Hello, %s!" % name)
print('hello {}'.format('kakak'))
name = "John"
age = 15
print("%s is %d years old." % (name, age))
mylist = [1,2,3]
print("A list: %s" % mylist)
# Ketika kita memberikan nilai 6 pada variabel x
x = 6  
print(type(x))
# Kemudian Berikan string “hello” pada variabel x di baris selanjutnya
x = 'hello'
print(type(x))
x=5
str(x).zfill(5)
print(x)
p = 'Hello world!'
p = p.upper()
print(p)
p = p.lower()
print(p)
print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())
l = [1,2,3,3,4,4,4,4,5,6]
s = set(l)
x = "Hello, World"
 
print(l)
print(len(l))
 
print(s)
print(len(s))
 
print(x)
print(len(x))
for i in range(9):
    print(i)
for i in range(3, 9):
    print(i)
x = [2, 5, 3.14, 1, -7]
x.sort()
print(x)
var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)
var2 = 0
if var2:
   print ("2 - Got a true expression value")
   print (var2)
# =============================================================================
# amount = int(input("Enter amount: "))
# if amount<1000:
#    discount = amount*0.05
#    print ("Discount",discount)
# else:
#    discount = amount*0.10
#    print ("Discount",discount)
#    
# print ("Net payable:",amount-discount)
# a = 8
# if a % 2 == 0:
#     print('bilangan {} adalah genap'.format(a))
# else:
#     print('bilangan {} adalah ganjil'.format(a))
# amount = int(input("Enter amount: "))
# if amount<1000:
#    discount = amount*0.05
#    print ("Discount",discount)
# elif amount<5000:
#    discount = amount*0.10
#    print ("Discount",discount)
# else:
#    discount = amount*0.15
#    print ("Discount",discount)
# print ("Net payable:",amount-discount)
# =============================================================================
a = 0
if a > 0:
    print('bilangan {} adalah positif'.format(a))
elif a < 0:
    print('bilangan {} adalah negatif'.format(a))
else:
    print('bilangan {} adalah nol'.format(a))
for letter in 'Python':  # First Example
    print('Current Letter: {}'.format(letter))
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # Second Example
    print('Current fruit: {}'.format(fruit))
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('Current fruit: {}'.format(fruits[index]))
count = 0
while (count < 5):
    print('The count is: {}'.format(count))
    count = count + 1
# =============================================================================
# var = 1
# while var == 1:  # This constructs an infinite loop
#     num = input('Enter a number: ')
#     print('You entered: {}'.format(num))
#  
#  
# while True:  # This constructs an infinite loop
#     num = input('Enter a number: ')
#     print('You entered: {}'.format(num))
# =============================================================================
for i in range(0, 5):
    for j in range(0, 5 - i):
        print('*', end='')
    print()
for letter in 'Python':     # First Example
    if letter == 'h':
        break
    print('Current letter: {}'.format(letter))
var = 10                    # Second Example
while var > 0:             
    print('Current variable value: {}'.format(var))
    var = var - 1
    if var == 5:
        break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a) # Output: ['hello', 'world', 'in', 'python']
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num) # Output: [2, 3, 4]
def sum(arg1, arg2):
    # Add both the parameters and return them.
    total = arg1 + arg2
    print('Inside the function: {}'.format(total))
    return total
# Panggil sum
total = sum(10, 20);
print('Outside the function: {}'.format(total))
def kuadrat(x):
    return x*x
a = 10
k = kuadrat(a)
print('nilai kuadrat dari {} adalah {}'.format(a, k))
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(mylist))
 
# Panggil changeme
mylist = [10, 20, 30]
changeme(mylist)
print('Nilai di luar fungsi: {}'.format(mylist))
def changeme(mylist):
    "Variabel mylist berikut hanya dikenali (berlaku) di dalam fungsi"
    mylist = [1, 2, 3, 4]  # This would assign new reference in mylist
    print ('Nilai di dalam fungsi: {}'.format(mylist))
 
# Panggil fungsi changeme
mylist = [10, 20, 30]
changeme(mylist)
print('Nilai di luar fungsi: {}'.format(mylist))
def printinfo(name, age):
   "This prints a passed info into this function"
   print('Name: ', name)
   print('Age: ', age)
 
# Now you can call printinfo function (with age argument first)
printinfo(age=5, name="Dicoding")
def printinfo(name, age=35):
   "This prints a passed info into this function"
   print('Name: ', name)
   print ('Age: ', age)
 
# Now you can call printinfo function (with optional argument age)
printinfo(age=5, name='Dicoding')
printinfo(name='Data')