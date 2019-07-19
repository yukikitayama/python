# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:01:56 2019

@author: yukic
"""

# Study about class object, self and init argument.

class Snake:
    pass

Snake()
snake = Snake()
snake
print(snake)

class Snake:
    name = "python"
    # name is "attribute"
    
snake = Snake()
print(snake)
print(snake.name)

# Once I make attribute to the class, I can define methods which access the attribute.

class Snake:
    name = "python"
    
    def change_name(self, new_name):
        self.name = new_name
        # without self argument, I can't access the attribute of this class
        
snake = Snake()
print(snake)
print(snake.name)
print(snake.change_name)

snake.change_name("anaconda")
print(snake)
print(snake.name)

class Snake:
    
    def __init__(self, name): # If I use __init__, I don't have to pre-prepare initial value for attribute. But if I do not put a value for attribute when I use this class object, it will cause error.
        self.name = name
        
    def change_name(self, new_name):
        self.name = new_name

print(Snake)

print(__name__)

snake = Snake()
# Now this Snake class object sets the init method, so the above does not specify the value for attribute, so it cause error like below.
# TypeError: __init__() missing 1 required positional argument: 'name'

snake = Snake("python")
print(snake)
print(snake.name)
# python

snake = Snake("anaconda")
print(snake.name)

# Note
# Class: So class is a way to create object 
# self: By using self, we can access the attribute of the class object
# __init__: Use this when you don't want to set initial value for attribute. Instead, you are meant to set when you run. But If you specify __init__ and do not put value for the attribute when you run, it will make an error.







