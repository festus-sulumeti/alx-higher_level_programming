0x06. Python - Classes and Objects
This project is about learning the basics of classes and objects in Python.

Tasks
My first square
Write an empty class Square that defines a square.
Square with size
Write a class Square that defines a square by:
Private instance attribute: size
Instantiation with size (no type/value verification)
Size validation
Write a class Square that defines a square by:
Private instance attribute: size
Instantiation with optional size: def init(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Area of a square
Write a class Square that defines a square by:
Private instance attribute: size
Instantiation with optional size: def init(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Public instance method: def area(self): that returns the current square area
Access and update private attribute
Write a class Square that defines a square by:
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def init(self, size=0):
Public instance method: def area(self): that returns the current square area
Printing a square
Write a class Square that defines a square by:
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def init(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
Coordinates of a square
Write a class Square that defines a square by:
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position: def init(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space - Don’t fill lines by spaces when position[1] > 0
