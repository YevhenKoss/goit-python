from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record] = record


class Field:
    pass


class Name(Field):
	def __init__(self, name):
		self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


class Record:

	def __init__(self, name):
		self.name = name
		self.phones = []
		self.new_phone = ''


	def add_phone(self, phone):
		self.phones.append(phone)


	def edit_phone(self, phone, new_phone):
		for i in self.phones:
			if i == phone:
				idx = self.phones.index(i)
				self.phones[idx] = new_phone


	def remove_phone(self, phone):
		self.phones.remove(phone)




