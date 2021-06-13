from collections import UserDict
from datetime import date
import re
import pickle


class AddressBook(UserDict):

    def add_record(self, record):
        contact_number = len(self.data) + 1
        self.data[contact_number] = record
        contact_number += 1
        return contact_number

    def find(self, find_data):
        result = []
        for k, i in self.data.items():
            if re.findall(find_data, i.contact_data['Name'], re.IGNORECASE) != []:
                result.append([k, i.contact_data['Name'], i.contact_data['Phone']])
            else:
                for j in range(0, len(i.contact_data['Phone'])):
                    if re.findall(find_data, i.contact_data['Phone'][j], re.IGNORECASE) != []:
                        result.append([k, i.contact_data['Name'], i.contact_data['Phone']])
        return result

    def __getstate__(self):
        attributes = self.__dict__
        return attributes
    
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
        return record.name, record.phone, record.birthday


class Birthday():

    def __init__(self, birthday):
            birthday = str(birthday)
            dob_data = birthday.split(".")
            today = date.today().year
            if dob_data[0].isdigit and int(dob_data[0]) > 0 and int(dob_data[0]) <= 31:
                if dob_data[1].isdigit and int(dob_data[1]) > 0 and int(dob_data[1]) <= 12:
                    if dob_data[2].isdigit and int(dob_data[2]) > 0 and int(dob_data[2]) <= today:
                        self.__birthday = birthday
                    else:
                        print('You have to enter numbers separated by a dot: DD.MM.YYYY')
                else:
                    print('You have to enter numbers separated by a dot: DD.MM.YYYY') 
            else:
                print('You have to enter numbers separated by a dot: DD.MM.YYYY')

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
                    print('You have to enter numbers separated by a dot: DD.MM.YYYY')
            else:
                print('You have to enter numbers separated by a dot: DD.MM.YYYY')
        else:
            print('You have to enter numbers separated by a dot: DD.MM.YYYY')


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

    def __init__(self, name, phone, birthday):
        phones = []
        phones.append(phone.phone)
        self.contact_data = contact_data = {}
        self.name = contact_data['Name'] = name.name
        self.phone = contact_data['Phone'] = phones
        if birthday != None and birthday != '':
            self.birthday = contact_data['Birthday'] = birthday.birthday
        else:
            self.birthday = None

    def add_phone(self, phone):
        phone = str(phone)
        phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", ""))
        if phone.isdigit() and len(phone) == 12:
            self.contact_data['Phone'].append(phone)
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            self.phone = None
        
    def edit_phone(self, phone, new_phone):
        phone = str(phone)
        phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", ""))
        if phone.isdigit() and len(phone) == 12:
            phone = phone
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            phone = None
        new_phone = str(new_phone)
        new_phone = (
            new_phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", ""))
        if new_phone.isdigit() and len(new_phone) == 12:
            new_phone = new_phone
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
            new_phone = phone
        for i in self.contact_data['Phone']:
            if i == phone:
                idx = self.contact_data['Phone'].index(i)
                self.contact_data['Phone'][idx] = new_phone

    def remove_phone(self, phone):
        phone = str(phone)
        phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", ""))
        if phone.isdigit() and len(phone) == 12:
            self.contact_data['Phone'].remove(phone)
        else:
            print('Wrong phone number format. Try "+XX(XXX)XXX-XX-XX"')
        
    def days_to_birthday(self):
        if self.birthday != None:
            today = date.today()
            dob_data = self.birthday.split(".")
            dobDay = int(dob_data[0])
            dobMonth = int(dob_data[1])
            dobYear = int(dob_data[2])
            dob = date(dobYear,dobMonth,dobDay)
            thisYear = today.year
            nextBirthday = date(thisYear,dobMonth,dobDay)
            if today < nextBirthday:
                gap = (nextBirthday - today).days
                print("Abonent's birhday is in " + str(gap) + ' days.')
            elif  today == nextBirthday:
                print("Today is abonent's birthday! Happy Birthday!")
            else:
                nextBirthday = date(thisYear+1,dobMonth,dobDay)
                gap = (nextBirthday - today).days
                print("Abonent's birthday is in " + str(gap) + ' days.')
        else:
            print("Current contact doesn't have date of birth")