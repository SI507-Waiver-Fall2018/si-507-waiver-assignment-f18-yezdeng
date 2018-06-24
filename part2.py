# Name: Yezhi Deng 
# Uniq: yezdeng
# UMID: 43578445


# these should be the only imports you need
import sys
import sqlite3



### input

### Open database
db = sqlite3.connect("Northwind_small.sqlite") 


### part2.py customers: prints the list of all customers

command = sys.argv[1]


if (command == "customers"):
	
	### Select id, company name from table Customer
	cursor_customers = db.execute("SELECT id, CompanyName from Customer")
	customer_id = []
	customer_company_name = []

	print("ID" + '\t' + "Customer Name")
	for row in cursor_customers:
		customer_id.append(row[0])
		customer_company_name.append(row[1])
		print(row[0] + '\t' + row[1])




### part2.py employees: prints the list of all employees
if (command == "employees"):

	### Select id, company name from table Employee
	cursor_employee = db.execute("SELECT id, LastName, FirstName from Employee")
	employee_id = []
	employee_name = []

	print("ID" + '\t' + "Employee Name")
	for row in cursor_employee:
		employee_id.append(row[0])
		employee_name.append(row[2] + ' ' + row [1])
		print(str(row[0]) + '\t' + row[2] + ' ' + row [1])

	### Output
	# print(employee_id)
	# print(employee_name)

# print(len(sys.argv))

if (len(sys.argv) >= 3):

	[command, search] = sys.argv[2].split("=")


	## part2.py orders cust=<customer id>: prints the list of order dates for  eg. orders cust=ALFKI
	## all orders placed for the specified customer. Use the customer ID for this command.
	if (command == "cust"):
		cust_id = search

		cursor = db.cursor()
		cursor.execute("SELECT OrderDate FROM 'Order' WHERE Customerid='{}'".format(cust_id))
		result = cursor.fetchall()
		print(result)
		print("Order Dates")
		for date in result:
			print(date[0])

	else: 
		emp_last_name = search
		cursor = db.cursor()

		cursor.execute("SELECT OrderDate FROM 'Order' WHERE EmployeeId = (SELECT id FROM 'Employee' WHERE LastName='{}')".format(emp_last_name))
		result = cursor.fetchall()
		print(result)
		print("Order Dates")
		for date in result:
			print(date[0])


db.close()