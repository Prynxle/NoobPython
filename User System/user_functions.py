#register_user
#edit_user


def register_user():
	fname = str(input("Enter First Name: "))
	lname = str(input("Enter Second Name: "))
	
	user_dict = {

	'user_name': fname + '' + lname,
	'email': fname + lname + '@gmail.com',

}
	return user_dict


def editted_user(user):
	if user != '':
		user = register_user()

	else: 
		print('\n Wrong')

	return user
