
"""
Writing Functions in Python - Closures
"""

# nonlocal variables: variables defined in the parent function that are used by the child function 

def parent(arg_1, arg_2):
    
    # From child()'s point of view, 
    # 'value' and 'my_dict' are nonlocal variables, 
    # as are 'arg_1' and 'arg_2' 
    
    value = 22
    my_dict = {'chocolate': 'yummy'} 
    
    def child():
        print(2 * value)
        print(my_dict['chocolate']) 
        print(arg_1 + arg_2)
        
    return child 

new_function = parent(3, 4) 

print([cell.cell_contents for cell in new_function.__closure__]) 

# a closure is the way of nonlocal variables attached to a return function so that the function can operate, even when called outside of
# it's parent scope 

# Why does all this matter?
#
# It's because Decorators use them:
#
# > Functions as objects 
# > Nested Functions 
# > Nonlocal Scope
# > Closures 

"""
Exercise Output 

You're teaching your niece how to program in Python, and she is working on returning nested functions. She thinks she has 
written the code correctly, but she is worried that the returned function won't have the necessary information when called. 
Show her that all of the nonlocal variables she needs are in the new function's closure.
"""

# Use an attribute of the my_func() function to show that it has a closure that is not None. 
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)


# show that there are two variables in the closure 
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure so you can show that they are equal to [2, 17], the arguments passed to return_a_func().
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])


#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
"""
Exercise Output 2 

You are still helping your niece understand closures. You have written the function get_new_func() that returns a nested function. 
The nested function call_func() calls whatever function was passed to get_new_func(). You've also written my_special_function() which 
simply prints a message that states that you are executing my_special_function().

You want to show your niece that no matter what you do to my_special_function() after passing it to get_new_func(), the new function 
still mimics the behavior of the original my_special_function() because it is in the new function's closure.
"""

# Show that you still get the original message even if you redefine my_special_function() to only print "hello". 
def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"
def my_special_function():
  print("hello")

new_func()


# Show that even if you delete my_special_function(), you can still call new_func() without any problems.
def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Delete my_special_function()
del(my_special_function)

new_func()


# Show that you still get the original message even if you overwrite my_special_function() with the new function.
def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()

