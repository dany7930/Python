fname = input ('enter file:' )
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many = dict()
for line in fhand:
 line = line.rstrip()
# print(line)

 wds =line.split()
 #print(wds)
 for w in wds:
   print('====>')
   print('before',many)
   oldvalue = 0
   print(w)
   print(many)
   oldvalue = 0
   if w in many : oldvalue = many(w)
   many(w) = many(w) + 1
   print('after', many)

 print(many)  


