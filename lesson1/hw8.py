from datetime import datetime, timedelta


#users = [{'Vasya': datetime(1989, 5, 8)}, {'Vasya2': datetime(1989, 5, 9)}, {'Vasya3': datetime(1989, 5, 14)}]

def congratulate(users):

	now = datetime.date(datetime.now()) # Определяем текущую дату
	two_days_before = timedelta(days=2) # Определяем дату предидущей субботы (при условии, что текущая дата определяется в понедельник)
	start_hb_week = now - two_days_before #Начало недели Happy Birthday

	mo = []
	tu = []
	we = []
	th = []
	fr = []

	week = {'Monday': mo, 'Tuesday': tu, 'Wednesday': we, 'Thursday': th, 'Friday': fr}


	for i in users:
		for key, val in i.items():
			for j in range(0, 7):
				wd = start_hb_week + timedelta(days=j)
				if datetime.strftime(val, '%m-%d') == datetime.strftime(wd, '%m-%d'):
					if datetime.strftime(wd, '%A') == 'Saturday' or	datetime.strftime(wd, '%A') == 'Sunday' or	datetime.strftime(wd, '%A') == 'Monday':
						mo.append(key)
					elif datetime.strftime(wd, '%A') == 'Tuesday':
						tu.append(key)
					elif datetime.strftime(wd, '%A') == 'Wednesday':
						we.append(key)
					elif datetime.strftime(wd, '%A') == 'Thursday':
						th.append(key)
					elif datetime.strftime(wd, '%A') == 'Friday':
						fr.append(key)


	for day, user in week.items():
		if user:
			print(f'{day}: {", ".join(user)}')


if __name__ == '__main__':
	congratulate(users)

