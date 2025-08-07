#xfile = open ('mbox.txt')
#for cheese in xfile:
 #   print(cheese)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print(f"File '{fname}' not found. Please check the path and try again.")
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):  # Count only lines starting with 'Subject:'
        count += 1
print('There were', count, 'subject lines in', fname)
