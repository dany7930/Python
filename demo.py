fh = open(r"D:\Cyber security\pyip\mbox-short.txt.txt", 'r')
print(fh)

for lx in fh:
    print(lx.strip())  # Remove extra newlines
fh.close()  # Close the file after use
