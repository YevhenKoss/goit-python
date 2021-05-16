from input_function import *


def main():
	while True:
		input_data = input('Enter the command: ')
		command = input_command(input_data)
		print(f'Command {command}')
		add_function(command)
		change_function(command)
		hello_function(command)
		phone_function(command)
		show_all_function(command)

		if command == 'good bye' or command == 'close' or command == 'exit':
			print('Good bye!')
			break



if __name__ == '__main__':
	main()