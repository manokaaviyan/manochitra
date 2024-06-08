#def()
def my_fun():
    print("welcome to sysway")
my_fun()

#Arguments
def my_function(fname):
  print(fname + " technologies")
my_function("sysway")
my_function("S-cad")
my_function("IELTS")

#no of arguments

def my_funtion(fname,lname):
    print(fname + " " + lname)
my_funtion("sysway","technologies")
    
#arbitary argument
def my_fun(*tech):
    print("name is "+ tech[2])
my_fun("sysway","s-cad","ielts")

#keyword argument
def my_function(child1, child2, child3):
  print("The youngest child is " + child1)

my_function(child1 = "IELTS", child2 = "S-CAD", child3 = "Sysway")

#default argument
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#passing a list of argument (any datatype)
def my_function(food):
    for x in food:
        print(x)
food = ["apple", "banana", "cherry"]
my_function(food)


#return value
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#pass
def myfunction():
  pass





















