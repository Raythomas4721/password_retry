password = 'a123456'
i = 3
while i > 0:
	pwd = input('please enter your password:')
	if pwd == password:
		print('Sign in suceesfully')
		break
	else:
		i = i-1
		print('Wrong password, You have', i , 'more chance')
		