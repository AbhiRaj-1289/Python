with open("Intro.txt","r") as reader:
	lines = reader.read()
	lines = lines[::-1]
with open("Intro_copy.txt","w") as writer:
	writer.write(lines)
	for lines in writer:
		print(reversed(lines))