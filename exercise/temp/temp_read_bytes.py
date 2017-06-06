

file = open('bytes.txt')
L = []
while True:
	line = file.readline()
	if not line:
		break
	s = line.index('=')
	L.append(int(line[s+2:len(line)]))

byte_json = bytes(L)
print(byte_json.decode('utf-8'))
