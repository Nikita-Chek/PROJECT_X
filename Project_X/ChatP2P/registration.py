import csv
import sys
import os
sys.path.append(os.path.abspath('../SHA256'))
import Sha2

def log_reg():
	while True:
		choice = input('login/register--( log/reg )? : ')
		if (choice == 'log') or (choice == 'reg'):
			break
		print('( log/reg )? ')
	return choice

def main():
	data = []
	with open('clients.csv', 'r') as File:
	    reader = csv.reader(File, delimiter=',', quotechar=',')
	    for row in reader:
        	data.append(row)

	print('Login or create account:')

	choice = log_reg()

	if choice == 'reg':
		while True:
			name = input('Name: ')
			for _ in data:
				if _[0] == name:
					print('this name is used')
					name = ''
					break
			if name:
				break

		password = input('password: ')
		password = Sha2.SHA256(password)
		data.append([name, password])

		with open('clients.csv', 'a') as File:
			File.write('\n'+str(name)+','+str(password))
			# registr = csv.write(File, delimiter=',')
			# for _ in data:
			# 	registr.writer(_)

	else:
		while True:
			name = input('Name: ')
			for _ in data:
				if _[0] == name:
					password = input('password: ')
					password = Sha2.SHA256(password)
					if _[1] == password:
						password = ''
						break
					else:
						print('wrong password')
						break
			if not password:
				break
	return name