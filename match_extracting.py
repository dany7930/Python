import re
x = 'My 2 favotate number are 19 and42'
y = re.findall('[0-9]+',x)
print(y)
