# Python - More Classes

This project focuses on Object-Oriented Programming (OOP) in Python.
It introduces classes, private attributes, properties, methods,
special methods, static methods, and class methods.

## Tasks

### 0. Simple rectangle
Create an empty Rectangle class without importing any modules.

### 1. Real definition of a rectangle
Define a Rectangle class with private width and height attributes.
Use properties and setters to retrieve and validate their values.
Both dimensions must be integers greater than or equal to zero.

### 2. Area and Perimeter
Add public methods to calculate the rectangle's area and perimeter.
The perimeter is zero if either width or height is zero.

### 3. String representation
Implement __str__ to display the rectangle using the # character.
Return an empty string if either dimension is zero.

### 4. Eval is magic
Implement __repr__ to return a string that can recreate a Rectangle
instance using eval().

### 5. Detect instance deletion
Implement __del__ to print "Bye rectangle..." when an instance is deleted.

### 6. How many instances
Create the class attribute number_of_instances.
Increase it when an instance is created and decrease it when an
instance is deleted.

### 7. Change representation
Create the class attribute print_symbol, initialized to #.
Use it as the character or object for the rectangle's string
representation. It can be any type.

### 8. Compare rectangles
Implement the static method bigger_or_equal(rect_1, rect_2).
It returns the rectangle with the larger area, or rect_1 if
both rectangles have the same area.

### 9. A square is a rectangle
Implement the class method square(cls, size=0).
It returns a new Rectangle instance with width and height equal
to the given size.

## Requirements

- All files must start with #!/usr/bin/python3.
- No modules should be imported.
- Classes and modules must be documented.
- Code must follow PEP8 guidelines.
