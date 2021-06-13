from AddressBook import *

# Commands:

#- "add" - add the contact to the phone book
#- "append" - append the phone to existing contact
#- "change" - change the contact's phone
#- "days to birthday" - calculate how many days to abonent's birthday (only for abonents with date of birth)
#- "hello" - greet the assistant
#- "phone" - show the contact by his/her name or find all abonent's matches   
#- "remove" - remove abonent's phone
#- "save" - save address book
#- "show all" - show all contacts

#- "exit", "close", "good bye" - the assistent finishes the work without saving 

def main():
	# Loading an address book from a file 'save.bin'. If the file is missing, a new address book is created.
	path = pathlib.Path('save.bin')
	if path.exists():
		with open('save.bin', 'rb') as file:
			Address_book = pickle.load(file)
	else:
		Address_book = Address_Book_Classes.AddressBook()

	while True:
		input_data = input('Enter the command: ')
		command = input_command(input_data)
		print(f'Command {command}')
		add_function(command, Address_book)
		append_function(command, Address_book)
		birthday_function(command, Address_book)
		change_function(command, Address_book)
		hello_function(command)
		phone_function(command, Address_book)
		remove_function(command, Address_book)
		save_function(command, Address_book)
		show_all_function(command, Address_book)


		if command == 'good bye' or command == 'close' or command == 'exit':
			print('Good bye!')
			break



if __name__ == '__main__':
	main()



