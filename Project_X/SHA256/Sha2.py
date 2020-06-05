from os import system
import preprocessing as pr

def SHA256(password):
	password = password.encode('utf-8')
	password = pr.Pre_processing(password)
	password = pr.cut(password)
	length = len(password)

	data = str(length)
	for _ in range(length):
		password[_]  = pr.cut(password[_], 32)
		for i in range(len(password[_])):
			password[_][i] = int(password[_][i], base=2)
			data += ' ' + str(password[_][i])

	#os.system('C:\\Users\\admin\\Documents\\XXX\\python\\Project X\\SHA256\\main_loop.exe '
	#		 + data)
	system('"C:\\Users\\admin\\Documents\\XXX\\python\\Project_X\\SHA256\\main_loop.exe ' + data + '"')

	with open('C:\\Users\\admin\\Documents\\XXX\\python\\Project_X\\SHA256\\bits\\result.txt', 'r') as dg:
		digest = dg.read()
		digest = digest.split()
	for _ in range(8):
		if len(digest[_]) < 8:
			while len(digest[_]) < 8:
				digest[_] = '0' + digest[_]

	return ''.join(digest)

# file = open('input_data/text.txt', 'rb')
# text = file.read()
# file.close()
# print(type(text))
if __name__ == '__main__':
	text = input('input: ').encode('utf-8')

	text = pr.Pre_processing(text)
	text = pr.cut(text)
	length = len(text)

	data = str(length)
	for _ in range(length):
		text[_]  = pr.cut(text[_], 32)
		for i in range(len(text[_])):
			text[_][i] = int(text[_][i], base=2)
			data += ' ' + str(text[_][i])

	system('main_loop.exe ' + data)

	with open('bits/result.txt', 'r') as dg:
		digest = dg.read()
		digest = digest.split()
	for _ in range(8):
		if len(digest[_]) < 8:
			while len(digest[_]) < 8:
				digest[_] = '0' + digest[_]

	print(''.join(digest))

if __name__ == '__main__':
	print(SHA256(input()))