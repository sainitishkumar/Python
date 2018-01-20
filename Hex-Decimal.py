#/usr/bin/python

def convert(data):
	if data=='A':
		return 10
	if data=='B':
		return 11
	if data=='C':
		return 12
	if data=='D':
		return 13
	if data=='E':
		return 14
	if data=='F':
		return 15					

def pow(x, y):
    powered = x
    if y == 0:
        return 1
    while y > 1:
        powered *= x
        y -= 1
    return powered


c=input()
ptext=0

for i in range(len(c)):
	if c[-i-1]=='A' or c[-i-1]=='B' or c[-i-1]=='C' or c[-i-1]=='D' or c[-i-1]=='E' or c[-i-1]=='F':
		ptext+=convert(c[-i-1])*pow(16,i)
		
	else:
		ptext+=int(c[-i-1])*pow(16,i)
print(ptext)

		
	

