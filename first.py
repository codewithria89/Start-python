import pyjokes
print("""
A Module is a file containing code written by someone else which can be imported and used in our programs.

Pip is the package manager for Python. We can use pip to install a module on our system.

There are two types of modules:
[1] Built-in Modules — already preinstalled in Python (like os, random, etc.)
[2] External Modules — need to install via pip (like TensorFlow, Flask, etc.)
""")
print(""" We can use Python as calculator by cmd.....this open Read Evaluate Print Loop , where REPL let us run code line by line and seee result instantly.
      A python error is a code mistake that stops prgms.""")



# importing pyjokes to get random jokes...and for disabling this line we use single line comments

joke = pyjokes.get_joke()
print(joke)
"""now it will print random joke generated by that module...it is under multiline comments..which is another types of comments. """