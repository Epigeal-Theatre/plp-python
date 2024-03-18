
Python function is a modular piece of code that can be used repeatedly. Generally a function is a block of code which is executed when it is called from somewhere in the program. A function has a return value.



Functions are perfect for abstraction. They allow us to write blocks of code which can be reused in different ways and in different programs.

Creating a Function
Lets create a function add_nums that adds two numbers.

In Python a function is defined using the def keyword:

Calling a Function
To get the function (add_nums) output, you must call it. To call a function, use the function name followed by parenthesis:

Function Arguments/ Parameters
Information can be passed into functions as arguments. Arguments make our functions more dynamic and reusables.



Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.


*args and **kwargs

Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

﻿

This way the function will receive a tuple of arguments, and can access the items accordingly:

Lets see our above example, when number of arguments is unknown

Arbitrary Keyword Arguments, **kwargs
If the keyword arguments to be passed in a function are not known, you should add ** before the parameter name in the function definition. Example: **age

