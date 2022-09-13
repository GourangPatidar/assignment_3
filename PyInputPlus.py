import pyinputplus as pyip

# this is for input integers
inp=pyip.inputInt(prompt="enter a integer" , limit=3 , default=0 , allowRegexes="true")
print(inp)

# this is for input str
#inp=pyip.inputStr(prompt="enter a str........" , blank=False , allowRegexes="aeiou"  , limit=3)
#print(inp)

# menu item input
#inp = pyip.inputMenu(['apple', 'banana', 'mango'])
#print(inp)

# date and time input
#inp = pyip.inputDatetime('Enter date and time... ',
                         #formats=('%m/%d/%y %H:%M:%S','%m.%d.%Y %H:%M:%S'))

# print(inp)


