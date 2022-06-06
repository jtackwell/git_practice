#program creates a text file with name, address, and phone in a chosen directory

import os

print('\nWelcome to the contact information saver!')
print('\nThe current directory is:')
print(os.getcwd())

#used later to store user input
master_list =[]

#checks user input and changes directory
def user_dir():
	try:
		print('\nWhat directory would you like to use?')
		user_dir = input()
		os.chdir(user_dir)
		print('\nNow the directory is:')
		print(os.getcwd())
	except Exception as e:
		print(e)
		print('\nPlease try again')
		user_dir()	

user_dir()

#Takes users file name and stores it in a list	
def file_name():	
		print('\nPlease name the file used to store contact information:')
		contact = input()
		print("\nYou chose:")
		print(contact)
		master_list.append(contact)

file_name()

#takes users given contact information
def conatct_info():
	print("\nPlease enter your name:")
	name=input()
	master_list.append(name)

	print("\nPlease enter your address:")
	address=input()	
	master_list.append(address)

	print("\nPlease enter your phone number:")
	phone=input()
	master_list.append(phone)

conatct_info()

#creates file using given info from file_name() and contact_info()
with open(master_list[0], 'w') as file_object:
	file_object.write(master_list[1])
	+file_object.write("\n,\n")
	+file_object.write(master_list[2])
	+file_object.write('\n,\n')
	+file_object.write(master_list[3])

#prints information from file created
print(f'\nThe information saved in file "{master_list[0]}":')
with open(master_list[0],) as file_object:
	for line in file_object:
		print(line.strip())