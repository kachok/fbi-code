import operator

f=open("message.txt","r")
message=f.read().strip()
f.close()

print "message: "
print message

output=list(message)

f=open("code.txt","r")
original=f.readline().strip()
target=f.readline().strip()
f.close()

print "original: ", original
print "target: ", target

freq={}

for i,char in enumerate(message):
	#print char
	pos=original.find(char)
	#print pos
	if pos>-1:
		output[i]=target[pos]

	if char in freq.keys():
		freq[char]=freq[char]+1
	else:
		freq[char]=1

print ""
print "decrypted message: "
print "".join(output)

sorted_freq = sorted(freq.iteritems(), key=operator.itemgetter(1))
print sorted_freq


