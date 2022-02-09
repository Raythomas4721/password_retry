password = 'a123456'
i = 3
while i > 0:
	i = i-1
	pwd = input('please enter your password:')
	if pwd == password:
		print('Sign in suceesfully')
		break
	else:
		print('Wrong password')
		if i >0:	
			print('You have', i , 'more chance')
		else:
			print('No more chance!.This account will be locked')