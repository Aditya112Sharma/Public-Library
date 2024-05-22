import pickle
import os
#1. Add Customer Record
def addCustomer():
        Customer=dict()
        Customer['Customer_id']=int(input("Enter new Customer id"))
        Customer['Customer_Name']=input("Enter Customer Name")
        Customer['Customer_Address']=input("Enter Address of Customer")
        Customer['Customer_Contact']=input("Enter Contact Number")
        H=open("Customer.dat","ab")
        pickle.dump(Customer,H)
        H.close()
        
#2. Dispaly All Customer Records 
def showCustomer():
	H=open("Customer.dat","rb")
	while True:	
		try:
			a=pickle.load(H)
			print("Customer ID :" , a['Customer_id'])
			print("Name :", a['Customer_Name'])
			print("Address :",a['Customer_Address'])
			print("Contact Number :", a['Customer_Contact'])
			print()
		except EOFError:
			break
	H.close()
	
#3. Edit Customer  Record
def editCustomer():
	H=open("Customer.dat","rb")
	Ad=int(input("Enter Customer id "))
	S=open("C1.dat","wb")
	found=False
	while True:	
		try:
			a=pickle.load(H)
			print("Customer ID :" , a['Customer_id'])
			print("Name :", a['Customer_Name'])
			print("Address :",a['Customer_Address'])
			print("Contact Number :", a['Customer_Contact'])
			if a['Customer_id']==Ad:
				found=True
				print("Enter Updated Details ")
				a['Customer_Name']=input("Enter Customer Name")
				a['Customer_Address']=input("Enter Address of Customer")
				a['Customer_Contact']=input("Enter Contact Number")
			pickle.dump(a,S)	
		except EOFError:
			break
	S.close()
	H.close()
	if found==True:
		os.remove("Customer.dat")
		os.rename("C1.dat","Customer.dat")
	else:
		print("Record not found")
		
#4. Remove Customer Record
def removeCustomer():
	H=open("Customer.dat","rb")
	S=open("C2.dat","wb")
	n=int(input("Enter Customer_ID  for removing record"))
	try:
		while True:	
			Customer=pickle.load(H)
			if Customer["Customer_id"]!=n:
				pickle.dump(Customer,S)			
	except EOFError:
		print("Record deleted")
	else:
		H.close()
		S.close()
		
	S.close()
	H.close()
	os.remove("Customer.dat")
	os.rename("C2.dat","Customer.dat")

#5. Add Book 
def addbook():
	P=open("book.dat","ab")
	Book=dict()
	Book['Book_id']=int(input("Enter new Book id"))
	Book['Type']=input("Enter Book Type")
	Book['Name']=input("Enter Name of the book ")
	Book['Baserate']=int(input("Enter Basic Rate "))
	Book['Issued']="NO"
	Book['Customer_id']=0
	P=open("book.dat","ab")
	pickle.dump(Book,P)
	P.close()

#6. Show Books
def showbooks():
	P=open("book.dat","rb")
	while True:	
		try:
			Book=pickle.load(P)
			print("Book ID  :" , Book['Book_id'])
			print("Book Type : ",	Book['Type'])
			print("Book Name :",  Book['Name'])
			print("Base Rate :", Book['Baserate'])
			print("Issued :",Book['Issued'])
			print("Issue to Client: ",Book['Customer_id'])
			print()
		except EOFError:
			break

#7. Edit Book Info
def modifybook():
	P=open("book.dat","rb")
	A=open("C3.dat","wb")
	m=int(input("Enter book id"))
	found=False
	while True:	
		try:
			V=pickle.load(P)
			if V['Book_id']==m:
				print("Book  :" , V['Book_id'])
				print("Book Type ",	V['Type'])
				print("Name",V['Name'])
				print("Base Rate", V['Baserate'])
				print("Issued ",V['Issued'])
				print("Issue to Customer ",V['Customer_id'])
				print()	
				print("Re-Enter the details to update")
				V['Book_id']=int(input("Enter new Book id"))
				V['Type']=input("Enter Book Type")
				V['Name']=input("Enter Name of the Book ")
				V['Baserate']=int(input("Enter Basic Rate "))
			pickle.dump(V,A)			

		except EOFError:
			break
	P.close()
	A.close()
	os.remove("book.dat")
	os.rename("C3.dat","book.dat")


#8. Issue Book
def issuebook():
	P=open("book.dat","rb")

	while True:	
		try:
			V=pickle.load(P)
			if V['Issued'].upper()=="NO":
				print("Book ID  :" , V['Book_id'])
				print("Book Type ",	V['Type'])
				print("Name",V['Name'])
				print("Base Rate", V['Baserate'])
				print("Issued ",V['Issued'])
				print("Issue to Customer ",V['Customer_id'])
				print()
		except EOFError:
			break
	P.close()
	P=open("book.dat","rb")
	P1=open("C4.dat","wb")
	m=int(input("Enter book id"))
	n=int(input("Enter Customer id"))
	found=False
	while True:	
		try:
			V=pickle.load(P)
			if V['Book_id']==m and V['Issued'].upper()=="NO" :
				found=True
				print("Book ID  :" ,V['Book_id'])
				print("Book Type ",V['Type'])
				print("Name",V['Name'])
				print("Base Rate",V['Baserate'])
				print("Issued ",V['Issued'])
				print("Issue to Customer ",V['Customer_id'])
				print()
				print("Issueing details")
				V['Issued']="YES"
				V['Customer_id']=n
				
			pickle.dump(V,P1)
		except EOFError:
			break
	P1.close()
	P.close()
	if found==False:
		print("Book not found or may be issued")
	else:
		os.remove("book.dat")
		os.rename("C4.dat","book.dat")

#9. Issued Books
def issuedbooks():
	P=open("book.dat","rb")
	while True:	
		try:
			V=pickle.load(P)
			if V['Issued'].upper()=="YES":
				print("Book ID  :" , V['Book_id'])
				print("Book Type ",	V['Type'])
				print("Name",V['Name'])
				print("Base Rate", V['Baserate'])
				print("Issued ",V['Issued'])
				print("Issue to Customer ",V['Customer_id'])
				print()
		except EOFError:
			break
	P.close()


#10.Billing and Deposite
def billing():
	Bill=dict()
	Bill['Bill_id']=int(input("Enter Bill id"))
	Bill['No. of days Issued']=int(input("Enter no. of days issued"))
	P=open("book.dat","rb")
	P1=open("C6.dat","ab")
	P2=open("temp.dat","wb")
	m=int(input("Enter Book id"))
	pickle.dump(Bill,P1)
	while True:	
		try:
			V=pickle.load(P)
			if V['Issued']=="YES" and V['Book_id']==m:
				print("Book ID  :" , V['Book_id'])
				print("Book Type ",	V['Type'])
				print("Name",V['Name'])
				print("Base Rate", V['Baserate'])
				print("Issued ",V['Issued'])
				print("Issue to Customer ",V['Customer_id'])
				print("Total amount=",V['Baserate'] + 5*Bill['No. of days Issued'])
				print()
				V['Issued']="NO"
				V['Customer_id']=0
			pickle.dump(V,P2)
		except EOFError:
			break
	P.close()
	P1.close()
	P2.close()
	os.remove("book.dat")
	os.rename("temp.dat","book.dat")
#Menu	
while True:
	print("1. Add Customer Record")
	print("2. Display All Customer Records ")
	print("3. Edit Customer  Record")
	print("4. Remove Customer Record")
	print("5. Add Book ")
	print("6. Show Books")
	print("7. Edit Book Info")
	print("8. Issue Book")
	print("9. Issued Books")
	print("10. Bill ")
	print("11. Exit")
	Q=int(input("Enter choice "))
	if Q==1:
		addCustomer()
	elif Q==2:
		showCustomer()
	elif Q==3:
		editCustomer()
	elif Q==4:
		removeCustomer()
	elif Q==5:
		addbook()
	elif Q==6:
		showbooks()
	elif Q==7:
		modifybook()
	elif Q==8:
		issuebook()
	elif Q==9:
		issuedbooks()
	elif Q==10:
		billing()
	elif Q==11:
		break

print("Thanks")
