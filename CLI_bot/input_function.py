import re



def add_function(command):
	if command == 'add':
		with open('phone_book.txt', 'a') as file:
			name = input("Enter abonent's name: ")
			while True:
				phone_number = input(f"Enter {name}'s phone number: ")
				clean_phone_number = sanitize_phone_number(phone_number)
				if clean_phone_number:
					file.write(f'{name} {clean_phone_number}\n')
					print('Record created!')
					break



def change_function(command):
	if command == 'change':
		while True:
			phone_book = []
			contact = prepare_new_contact_function(command)
			if not contact:
				continue
			else:
				break
		current_contact = contact[0]
		new_contact = contact[1]
		with open('phone_book.txt', 'r') as file:
			lines = file.readlines()
			for i in lines:
				phone_book.append(i.removesuffix('\n').strip())
		if current_contact in phone_book:
			index_current_contact = phone_book.index(current_contact)
			phone_book[index_current_contact] = new_contact
			with open('phone_book.txt', 'w') as file:
				for abonent in phone_book:
					file.write(f'{abonent}\n')
		else:
			print('Wrong current contact')



def hello_function(command):
	if command == 'hello':
		print('Hello! How can I help you?')



def input_command(input_data):
	commands = ['hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', 'exit']
	for command in commands:
		if re.findall(command, input_data, re.IGNORECASE):
			result = command
			break
		else:
			result = f'{input_data} is unknown. Please enter one of commands: {", ".join(commands)}'
	return result



def phone_function(command):
	if command == 'phone':
		name = input("Enter abonent's name: ")
		abonent = []
		with open('phone_book.txt', 'r') as file:
			lines = file.readlines()
			for i in lines:
				if re.findall(name, i, re.IGNORECASE):
					abonent.append(i.removesuffix('\n').strip())
				else:
					abonent_list = abonent
			abonent_list = '\n'.join(abonent)
			if not abonent_list:
				print('No such abonent in phone book')
			elif len(abonent_list) == 1:
				print(abonent_list[0])
			else:
				print(abonent_list)



def prepare_new_contact_function(command):
	if command == 'change':
		clean_phone_number = None
		new_contact = []
		while not clean_phone_number:
			name = (input("Enter abonent's name: ")).capitalize()
			phone_number = input(f"Enter current {name}'s phone number: ")
			clean_phone_number = sanitize_phone_number(phone_number)
			if not clean_phone_number:
				continue
			else:
				break
		current_contact = f'{name} {clean_phone_number}'
		with open('phone_book.txt', 'r') as file:
			lines = file.readlines()
			for i in lines:
				if re.findall(current_contact, i, re.IGNORECASE):
					new_phone = input(f"Enter new {name}'s phone number: ")
					clean_new_phone_number = sanitize_phone_number(new_phone)
					new_contact = f'{name} {clean_new_phone_number}'
				else:
					new_contact
			if not new_contact:
				print('No such contact in phone book')
			else:
				return [current_contact, new_contact]



def sanitize_phone_number(phone_number):

		phone_number = (
			phone_number.strip()
			.removeprefix("+")
			.replace("(", "")
			.replace(")", "")
			.replace("-", "")
			.replace(" ", ""))

		if phone_number.isdigit() and len(phone_number) == 12:
			return phone_number
		else:
			print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')



def show_all_function(command):
	if command == 'show all':
		phone_book = []
		with open('phone_book.txt', 'r') as file:
			lines = file.readlines()
			for i in lines:
				phone_book.append(i.removesuffix('\n').strip())
				book = '\n'.join(phone_book)
			print(book)
