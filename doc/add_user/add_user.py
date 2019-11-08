'''
	Добавляем группы и пользователей

'''


from time import sleep
from django.contrib.auth.models import User, Group

def rayon_from_file():
	with open('rayon.csv', 'r') as f:
		lines = f.read().splitlines()
	return lines


def users_from_file():
	with open('list_sotr.csv', 'r') as f:
		lines = f.read().splitlines()
	return lines
	#for line in lines:
	#	print(line)
	#	sleep(1)


def add_users():
	users = users_from_file()
	for user in users:
		mas_user = user.split('#')
		last_name = mas_user[0]
		first_name = mas_user[1] + ' ' + mas_user[2]
		username = mas_user[3]
		password = mas_user[4]
		group = mas_user[5]
		#print(last_name, first_name, username, password, group)
		#sleep(1)
		try:
			user = User.objects.create_user(last_name=last_name, first_name=first_name, username=username, password=password)
			user.groups.add(group) # add by id
			user.save()
		except:
			print(' error ' + group + ' ' + username)

def add_groups():
	rayons = rayon_from_file()
	for rayon in rayons:
		pk = rayon.split('#')[0]
		name = rayon.split('#')[1]
		my_group = Group.objects.create(pk=pk, name=name)

def all():
	print('add groups ...')
	add_groups()
	print('ready! \n add users ...')
	add_users()
	print('ready!')


'''
if __name__ == '__main__':
	main()
	test_00()
'''