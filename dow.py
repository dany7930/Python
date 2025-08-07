han = open("D:\Cyber security\pyip\mbox-short.txt.txt")

for line in han:
    line = line.rstrip()
    wds  = line.split()
  #  print('Words:', wds)
   #guardian in a compound statement
   
    if len(wds) < 3 or wds[0]  != 'From' :
     
        continue
    print(wds[2])
    
