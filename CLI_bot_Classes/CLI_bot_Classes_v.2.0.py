from collections import UserDict
from datetime import date
from re import S


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record] = record

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        keys = tuple(self.data.keys())
        if self.index == len(keys):
            raise StopIteration
        key = keys[self.index]
        record = self.data[key]
        self.index += 1
        return record.name, record.phone


class Birthday():
    def __init__(self, birthday):
        birthday = str(birthday)
        birthday = str(birthday)
        dob_data = birthday.split(".")
        today = date.today().year
        if dob_data[0].isdigit and int(dob_data[0]) > 0 and int(dob_data[0]) <= 31:
            if dob_data[1].isdigit and int(dob_data[1]) > 0 and int(dob_data[1]) <= 12:
                if dob_data[2].isdigit and int(dob_data[2]) > 0 and int(dob_data[2]) <= today:
                    self.__birthday = birthday
                else:
                    print('You have to enter numbers separated by a dot: XX.XX.XXXX')
            else:
                print('You have to enter numbers separated by a dot: XX.XX.XXXX')
        else:
            print('You have to enter numbers separated by a dot: XX.XX.XXXX')

    @property
    def date_of_birth(self):
        return self.__birthday

    @date_of_birth.setter
    def birthday(self, birthday):
        birthday = str(birthday)
        dob_data = birthday.split(".")
        today = date.today().year
        if dob_data[0].isdigit and int(dob_data[0]) > 0 and int(dob_data[0]) <= 31:
            if dob_data[1].isdigit and int(dob_data[1]) > 0 and int(dob_data[1]) <= 12:
                if dob_data[2].isdigit and int(dob_data[2]) > 0 and int(dob_data[2]) <= today:
                    self.__birthday = birthday
                else:
                    print('You have to enter numbers separated by a dot: XX.XX.XXXX')
            else:
                print('You have to enter numbers separated by a dot: XX.XX.XXXX')
        else:
            print('You have to enter numbers separated by a dot: XX.XX.XXXX')


class Name():
    def __init__(self, name):
        name = str(name)
        self.__name = name.capitalize()

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        name = str(name)
        self.__name = name.capitalize()


class Phone():
    def __init__(self, phone):
        phone = str(phone)
        phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", ""))
        if phone.isdigit() and len(phone) == 12:
            self.__phone = phone
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            self.__phone = None
    
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        phone = str(phone)
        phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", ""))
        if phone.isdigit() and len(phone) == 12:
            self.__phone = phone
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')


class Record():
    def __init__(self, name, phone, birthday=None):
        phones = []
        phones.append(phone)

        self.contact_data = contact_data = {}
        self.name = contact_data['Name'] = name
        self.phone = contact_data['Phone'] = phones
        if birthday!= None:
            self.birthday = contact_data['Birthday'] = birthday

    def add_phone(self, phone):
        self.phone.append(phone)

    def edit_phone(self, phone, new_phone):
        for i in self.phone:
            if i == phone:
                idx = self.phone.index(i)
                self.phone[idx] = new_phone

    def remove_phone(self, phone):
        self.phone.remove(phone)

    def days_to_birthday(self, birthday):
        if birthday != None:
            today = date.today()
            dob_data = birthday.split(".")
            dobDay = int(dob_data[0])
            dobMonth = int(dob_data[1])
            dobYear = int(dob_data[2])
            dob = date(dobYear,dobMonth,dobDay)
            thisYear = today.year
            nextBirthday = date(thisYear,dobMonth,dobDay)
            if today<nextBirthday:
                gap = (nextBirthday - today).days
                print('Your birhday is in " + str(gap) + " days.')
            elif  today == nextBirthday:
                print('Today is your birthday! Happy Birthday!')
            else:
                nextBirthday = date(thisYear+1,dobMonth,dobDay)
                gap = (nextBirthday - today).days
                print('Your birthday is in ' + str(gap) + ' days.')
        else:
            print('Enter date of birth')



