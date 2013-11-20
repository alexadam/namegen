import sys, random

cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
vow = ['a', 'e', 'i', 'o', 'u', 'y']

pattern = str(sys.argv[1])
output = ''

for c in pattern:
	if c == 'c':
		output += cons[random.randint(0, len(cons) - 1)]
	elif c == 'v':
		output += vow[random.randint(0, len(vow) - 1)]
		
print output
