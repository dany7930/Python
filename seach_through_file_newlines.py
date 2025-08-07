fhand = open ('D:\\Cyber security\\pyip\\mbox-short.txt.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
