import re

hand = open ('D:\\Cyber security\\pyip\\mbox-short.txt.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^From:', line):
        print(line) 