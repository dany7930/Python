fhand = open('D:\\Cyber security\\pyip\\mbox-short.txt.txt')
for line in fhand:
     line = line.rstrip()
     if not line.startswith('From ') : continue
     words = line.split()
     print(words[2])


#double split
#words = line.split()
#email = words[1]
#pieces = email.split('@')
#print(pieces[1])

