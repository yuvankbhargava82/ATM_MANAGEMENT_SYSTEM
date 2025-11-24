# creating the lists of usernames, their respective PINs and their bank statements
users = ["user1", "user2", "user3"]
pins = ["1234", "2222", "3333"]
amounts = [100000, 200000, 300000]
count = 0
# while loop checks existance of the enterd username in the given list
while True:
	user = input("Enter User Name: ")
	user = user.lower()
	if user in users:
		if(user == users[0]):
			n = 0
		elif(user == users[1]):
			n = 1
		else:
			n = 2
		break
	else:
		print("----------------")
		print("INVALID USERNAME")
		print("----------------")
# checking the pin is correct or not
while count < 3:
	print("------------------")
	pin = str(input("Please Enter your PIN: "))
	print("------------------")
	if pin.isdigit():
			if pin == pins[n]:
				break
			else:
				count += 1
				print("-----------")
				print("INVALID PIN")
				print("-----------")
				print()
	else:
		print("------------------------")
		print("PIN CONSISTS OF 4 DIGITS")
		print("------------------------")
		count += 1
# in case of a valid pin- continuing, or exiting
if count == 3:
	print("-----------------------------------")
	print("3 Unsuccessful PIN Attempts, Exiting")
	print("!!!!!YOUR CARD HAS BEEN LOCKED!!!!!")
	print("-----------------------------------")
	exit()

print("-------------------------")
print("LOGIN SUCCESSFUL")
print("-------------------------")
print()
print("--------------------------")
print(str.capitalize(users[n]), "Welcome to the ATM")
print("----------ATM SYSTEM-----------")
# Main menu
while True:
	print("-------------------------------")
	response = input("SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nExit_______(E) \n: ").lower()
	print("-------------------------------")
	response = response.lower()
	if response == "s":
		print("---------------------------------------------")
		print(str.capitalize(users[n]), "You have ", amounts[n],"RUPEES in your Account.")
		print("---------------------------------------------")
	elif response == "w":
		print("---------------------------------------------")
		cash_out = int(input("Enter the Amount you would like to Withdraw: "))
		print("---------------------------------------------")
		if cash_out%10 != 0:
			print("------------------------------------------------------")	
			print("AMOUNT YOU WANT TO WITHDRAW MUST BE A MULTIPLE OF 10")
			print("------------------------------------------------------")
		elif cash_out > amounts[n]:
			print("-----------------------------")
			print("YOU HAVE INSUFFICIENT BALANCE")
			print("-----------------------------")
		else:
			amounts[n] = amounts[n] - cash_out
			print("-----------------------------------")
			print("Your New Balance is: ", amounts[n], "RUPEES")
			print("-----------------------------------")
			
	elif response == "l":
		print()
		print("Press '1' for cash deposit")
		print("Press '2' for cheque deposit")
		ch=int(input())
		if(ch==1):
			print("---------------------------------------------")
			cash_in = int(input("Enter the amount of cash you want to deposit"))
			print("---------------------------------------------")
			if cash_in%10 != 0:
				print("----------------------------------------------------")
				print("AMOUNT YOU WANT TO LODGE MUST BE A MULTIPLE OF 10")
				print("----------------------------------------------------")
			else:
				amounts[n] = amounts[n] + cash_in
				print("----------------------------------------")
				print("Your New Balance is: ", amounts[n], "RUPEES")
				print("----------------------------------------")
		elif(ch==2):
			print("---------------------------------------------")
			cheque_in=int(input("Enter the amount on cheque you want to deposit "))
			print("---------------------------------------------")
			if cheque_in%10 != 0:
				print("----------------------------------------------------")
				print("AMOUNT YOU WANT TO LODGE MUST BE A MULTIPLE OF 10")
				print("----------------------------------------------------")
			else:
				amounts[n] = amounts[n] + cheque_in
				print("----------------------------------------")
				print("Your New Balance is: ", amounts[n], "RUPEES")
				print("----------------------------------------")
	elif response == "p":
		print("-----------------------------")
		new_pin = str(input("Enter a New PIN: "))
		print("-----------------------------")
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			print("------------------")
			new_pin1 = str(input("Confirm the New PIN: "))
			print("-------------------")
			if new_pin1 != new_pin:
				print("------------")
				print("PIN MISMATCH")
				print("------------")
			else:
				pins[n] = new_pin
				print("NEW PIN SAVED")
		else:
			print("-------------------------------------")
			print("   New PIN must consist Of 4 Digits \nand must be different from the Previous PIN")
			print("-------------------------------------")
	elif response == "e":
		print("Thank you! Have a nice day!!!")
		exit()
	else:
		print("------------------")
		print("RESPONSE NOT VALID")
		print("------------------")
