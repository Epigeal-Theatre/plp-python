name = input("What is your name?")
age = input("How old are you?")
location = input("Wherae are you located?")
txt = "Hello {}, you are {} years old and live in {}"
print(txt.format(name,age,location))