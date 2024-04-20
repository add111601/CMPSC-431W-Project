import psycopg2

def starting_Screen():
	print("""\nWelcome to the LA Crimes Database CL Interface!
Please select an option:
		1. Weapons
		2. Codes
		3. Locations
		4. LA Areas
		5. Police
		6. Victims
		7. Crimes(In totality, so most joins will be here)
		8. Insert Data
		9. Update Data
		10. Delete Data
		11. Exit""")
	choice = input("Enter your Choice (1-11): ")
	return choice

def weapons():
	print("""\nWeapons Statistics
Please select an option:
	1. Amount of crimes by weapons
	2. List Weapons
	3. Go Back""")
	choice = input("Enter your Choice (1-3): ")
	return choice

def weapons1(): # If inside weapons option and selecting option 1
	ch = input("Would you like it to be sorted (y or n)? ")
	while(True):
		if(ch == 'y'):
			ui = input("Ascending or Descending order (a or d)? ")
			while(True):
				if(ui == 'a'):
					cur.execute("SELECT Weapon_Desc, COUNT(*) FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code = Weapon.Weapon_Code GROUP BY Weapon_Desc ORDER BY COUNT(*) ASC;")
					li = cur.fetchall()
					for i in li:
						print(i)
					break
				elif(ui == 'd'):
					cur.execute("SELECT Weapon_Desc, COUNT(*) FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code = Weapon.Weapon_Code GROUP BY Weapon_Desc ORDER BY COUNT(*) DESC;")
					li = cur.fetchall()
					for i in li:
						print(i)
					break
				else:
					print("Invalid response. Please enter again")
					ui = input("Ascending or Descending order (a or d)? ")
			break
		elif(ch == 'n'):
			cur.execute("SELECT Weapon_Desc, COUNT(*) FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code = Weapon.Weapon_Code GROUP BY Weapon_Desc;")
			li = cur.fetchall()
			for i in li:
				print(i)
			break
		else:
			print("Invaild response. Please enter again")
			ch = input("Would you like it to be sorted (y or n)? ")
		

def weapons2(): # If inside weapons option and selecting option 2
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = int(input("""
What would you like to sort by:
	1. Weapon Code ASC
	2. Weapon Code DESC
	3. Weapon Description ASC
	4. Weapon Description DESC\n"""))
			while(True):
				if(inp == 1):
					cur.execute("SELECT * FROM Weapon ORDER BY Weapon_Code ASC;")
					break
				elif(inp == 2):
					cur.execute("SELECT * FROM Weapon ORDER BY Weapon_Code DESC;")
					break
				elif(inp == 3):
					cur.execute("SELECT * FROM Weapon ORDER BY Weapon_Desc ASC;")
					break
				elif(inp == 4):
					cur.execute("SELECT * FROM Weapon ORDER BY Weapon_Desc DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = int(input("""
What would you like to sort by:
	1. Weapon Code ASC
	2. Weapon Code DESC
	3. Weapon Description ASC
	4. Weapon Description DESC\n"""))
			break
		elif(ch == 'n'):
			cur.execute("SELECT * FROM Weapon;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")

	li = cur.fetchall() 
	for i in li:
		print(i)

def codes(): # If on welcome screen and user selects Codes
	print("""\nCode Statistics
Please select an option:
	1. Amount of crimes by codes
	2. List all codes
	3. Go Back""")
	choice = input("Enter your Choice (1-3): ")
	return choice

def codes1(): # If inside codes and user selects option 1
	ch = input("Would you like the data to be sorted (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp == 'a'):
					cur.execute("SELECT Crime_Code_Desc, COUNT(*) FROM Codes GROUP BY Crime_Code_Desc ORDER BY COUNT(*) ASC;")
					break
				elif(inp == 'd'):
					cur.execute("SELECT Crime_Code_Desc, COUNT(*) FROM Codes GROUP BY Crime_Code_Desc ORDER BY COUNT(*) DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending")
			break
		elif(ch == 'n'):
			cur.execute("SELECT Crime_Code_Desc, COUNT(*) FROM Codes GROUP BY Crime_Code_Desc")
			break
		else:
			print("Invaild response. Please enter again")
			ch = input("Would you like the data to be sorted (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def codes2(): # If inside codes and user selects option 2
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = int(input("""
What would you like to sort by:
	1. Code ASC
	2. Code DESC
	3. Code_Desc ASC
	4. Code_Desc DESC
	5. Mocodes ASC
	6. Mocodes DESC
	7. All Crime Codes ASC
	8. All Crime Codes DESC\n"""))
			if(inp == 1):
				cur.execute("SELECT * FROM Codes ORDER BY Crime_Code ASC;")
				break
			elif(inp == 2):
				cur.execute("SELECT * FROM Codes ORDER BY Crime_Code DESC;")
				break
			elif(inp == 3):
				cur.execute("SELECT * FROM Codes ORDER BY Crime_Code_Desc ASC;")
				break
			elif(inp == 4):
				cur.execute("SELECT * FROM Codes ORDER BY Crime_Code_Desc DESC;")
				break
			elif(inp == 5):
				cur.execute("SELECT * FROM Codes ORDER BY Mocodes ASC;")
				break
			elif(inp == 6):
				cur.execute("SELECT * FROM Codes ORDER BY Mocodes DESC;")
				break
			elif(inp == 7):
				cur.execute("SELECT * FROM Codes ORDER BY All_Crime_Code ASC;")
				break
			elif(inp == 8):
				cur.execute("SELECT * FROM Codes ORDER BY All_Crime_Code ASC;")
				break
			else:
				print("Invalid response. Please enter again")
				inp = int(input("""
What would you like to sort by:
	1. Code ASC
	2. Code DESC
	3. Code_Desc ASC
	4. Code_Desc DESC
	5. Mocodes ASC
	6. Mocodes DESC
	7. All Crime Codes ASC
	8. All Crime Codes DESC\n"""))

			break 
		elif(ch == 'n'):
			cur.execute("SELECT * FROM Codes;")
			break
		else:
			print("Invaild response. Please enter again")
			ch = input("Would you like to sort the output (y or n)")
	li = cur.fetchall()
	for i in li:
		print(i)

def location(): # If on welcome screen and user selects Locations
	print("""Location Statistics
Please select an option: 
	1. Location of most recent crimes 
	2. List all location data
	3. Go Back""")
	choice = input("Enter your Choice (1-3): ")
	return choice

def location1(): # If on location and user selects option 1
	ch = int(input("Enter the number of records you would like to view: "))
	cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc INNER JOIN Crime ON VicLoc.DR_NO=Crime.DR_NO ORDER BY Date_Committed DESC")
	li = cur.fetchmany(ch)
	for i in li:
		print(i)

def location2():
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = int(input("""
What would you like to sory by:
	1. Lat ASC
	2. Lat DESC
	3. Lon ASC
	4. Lon DESC
	5. Location ASC
	6. Location DESC
	7. Cross Street ASC
	8. Cross Street DESC\n"""))
			if(inp == 1):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Lat ASC;")
				break
			elif(inp == 2):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Lat DESC;")
				break
			elif(inp == 3):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Lon ASC;")
				break
			elif(inp == 4):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Lon DESC;")
				break
			elif(inp == 5):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Loc ASC;")
				break
			elif(inp == 6):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Loc DESC;")
				break
			elif(inp == 7):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Cross_Street ASC;")
				break
			elif(inp == 8):
				cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc ORDER BY Cross_Street DESC;")
				break
			else:
				print("Invalid response. Please enter again")
				inp = int(input("""
What would you like to sory by:
	1. Lat ASC
	2. Lat DESC
	3. Lon ASC
	4. Lon DESC
	5. Location ASC
	6. Location DESC
	7. Cross Street ASC
	8. Cross Street DESC\n"""))
			break 
		elif(ch == 'n'):
			cur.execute("SELECT Lat, Lon, Loc, Cross_Street FROM VicLoc;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def area(): # If on welcome screen and user selects Areas
	print(""" Area Statistics 
Please select an option:
	1. Count of crimes by Areas
	2. Count of crimes by Premis
	3. List all Area data
	4. Go Back""")
	choice = input("Enter your Choice (1-4): ")
	return choice

def area1(): # If on area and user selects option 1
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp == 'a'):
					cur.execute("SELECT Area_Name, COUNT(*) FROM Area GROUP BY Area_Name ORDER BY COUNT(*) ASC;")
					break 
				elif(inp == 'd'):
					cur.execute("SELECT Area_Name, COUNT(*) FROM Area GROUP BY Area_Name ORDER BY COUNT(*) DESC;")
					break 
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			
			break
		elif(ch == 'n'):
			cur.execute("SELECT Area_Name, COUNT(*) FROM Area GROUP BY Area_Name;")
			break 
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i) 

def area2():
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp == 'a'):
					cur.execute("SELECT Premis_Desc, COUNT(*) FROM Area GROUP BY Premis_Desc ORDER BY COUNT(*) ASC;")
					break 
				elif(inp == 'd'):
					cur.execute("SELECT Premis_Desc, COUNT(*) FROM Area GROUP BY Premis_Desc ORDER BY COUNT(*) DESC;")
					break 
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			
			break
		elif(ch == 'n'):
			cur.execute("SELECT Premis_Desc, COUNT(*) FROM Area GROUP BY Premis_Desc;")
			break 
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i) 

def area3():
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = int(input("""
What would you like to sory by:
	1. Area Code ASC
	2. Area Code DESC
	3. Area Name ASC
	4. Area Name DESC
	5. Premis Code ASC
	6. Premis Code DESC
	7. Premis Desc ASC
	8. Premis Desc DESC\n"""))
			if(inp == 1):
				cur.execute("SELECT * FROM Area ORDER BY Area ASC;")
				break
			elif(inp == 2):
				cur.execute("SELECT * FROM Area ORDER BY Area DESC;")
				break
			elif(inp == 3):
				cur.execute("SELECT * FROM Area ORDER BY Area_Name ASC;")
				break
			elif(inp == 4):
				cur.execute("SELECT * FROM Area ORDER BY Area_Name DESC;")
				break
			elif(inp == 5):
				cur.execute("SELECT * FROM Area ORDER BY Premis_Code ASC;")
				break
			elif(inp == 6):
				cur.execute("SELECT * FROM Area ORDER BY Premis_Code DESC;")
				break
			elif(inp == 7):
				cur.execute("SELECT * FROM Area ORDER BY Premis_Desc ASC;")
				break
			elif(inp == 8):
				cur.execute("SELECT * FROM Area ORDER BY Premis_Desc DESC;")
				break
			else:
				print("Invalid response. Please enter again")
				inp = int(input("""
What would you like to sory by:
	1. Area Code ASC
	2. Area Code DESC
	3. Area Name ASC
	4. Area Name DESC
	5. Premis Code ASC
	6. Premis Code DESC
	7. Premis Desc ASC
	8. Premis Desc DESC\n"""))
			break 
		elif(ch == 'n'):
			cur.execute("SELECT * FROM Area;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def police(): # If on welcome screen and user selects Police
	print(""" Police Statistics
Please select an option:
	1. Count of times Police Districts reports to a crime
	2. List all Police Districts and case number
	3. Go Back""")
	choice = input("Enter your Choice (1-3): ")
	return choice

def police1(): # If on Police and user selects option 1
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp == 'a'):
					cur.execute("SELECT Reporting_District, COUNT(*) FROM Crime GROUP BY Reporting_District ORDER BY COUNT(*) ASC;")
					break # Break out of direction loop
				elif(inp == 'd'):
					cur.execute("SELECT Reporting_District, COUNT(*) FROM Crime GROUP BY Reporting_District ORDER BY COUNT(*) DESC;")
					break # Break out of direction loop
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			
			break 
		elif(ch == 'n'):
			cur.execute("SELECT Reporting_District, COUNT(*) FROM Crime GROUP BY Reporting_District;")
			break 
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i) 

def police2():
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp == 'a'):
					cur.execute("SELECT DR_NO, Reporting_District FROM Crime ORDER BY Reporting_District ASC;")
					break 
				elif(inp == 'd'):
					cur.execute("SELECT DR_NO, Reporting_District FROM Crime ORDER BY Reporting_District DESC;")
					break 
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			
			break 
		elif(ch == 'n'):
			cur.execute("SELECT DR_NO, Reporting_District FROM Crime;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def victims(): #If on welcome screen and user selects Victims
	print("""\nVictim Statistics
Please select an option:
	1. Victim count by Sex
	2. Victim count by Descent
	3. List all Victim Data
	4. Go Back""")
	choice = input("Enter your Choice (1-4): ")
	return choice

def victims1():
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp == 'a'):
					cur.execute("SELECT Sex, COUNT(*) FROM VicLoc GROUP BY Sex ORDER BY COUNT(*) ASC;")
					break # Break out of direction loop
				elif(inp == 'd'):
					cur.execute("SELECT Sex, COUNT(*) FROM VicLoc GROUP BY Sex ORDER BY COUNT(*) DESC;")
					break # Break out of direction loop
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			
			break 
		elif(ch == 'n'):
			cur.execute("SELECT Sex, COUNT(*) FROM VicLoc GROUP BY Sex;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def victims2():
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp == 'a'):
					cur.execute("SELECT Vic_Descent, COUNT(*) FROM VicLoc GROUP BY Vic_Descent ORDER BY COUNT(*) ASC;")
					break 
				elif(inp == 'd'):
					cur.execute("SELECT Vic_Descent, COUNT(*) FROM VicLoc GROUP BY Vic_Descent ORDER BY COUNT(*) DESC;")
					break 
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			
			break 
		elif(ch == 'n'):
			cur.execute("SELECT Vic_Descent, COUNT(*) FROM VicLoc GROUP BY Vic_DESCENT;")
			break 
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i) 

def victims3():
	ch = input("Would you like to sort the output (y or n)? ")
	while(True):
		if(ch == 'y'):
			inp = int(input("""
What would you like to sory by:
	1. Age ASC
	2. Age DESC
	3. Sex ASC
	4. Sex DESC
	5. Vic Descent ASC
	6. Vic Descent DESC\n"""))
			if(inp == 1):
				cur.execute("SELECT DR_NO, Age, Sex, Vic_Descent FROM VicLoc ORDER BY Age ASC;")
				break
			elif(inp == 2):
				cur.execute("SELECT DR_NO, Age, Sex, Vic_Descent FROM VicLoc ORDER BY Age DESC;")
				break
			elif(inp == 3):
				cur.execute("SELECT DR_NO, Age, Sex, Vic_Descent FROM VicLoc ORDER BY Sex ASC;")
				break
			elif(inp == 4):
				cur.execute("SELECT DR_NO, Age, Sex, Vic_Descent FROM VicLoc ORDER BY Sex DESC;")
				break
			elif(inp == 5):
				cur.execute("SELECT DR_NO, Age, Sex, Vic_Descent FROM VicLoc ORDER BY Vic_Descent ASC;")
				break
			elif(inp == 6):
				cur.execute("SELECT DR_NO, Age, Sex, Vic_Descent FROM VicLoc ORDER BY Vic_Descent DESC;")
				break
			else:
				print("Invalid response. Please enter again")
				inp = int(input("""
What would you like to sory by:
	1. Age ASC
	2. Age DESC
	3. Sex ASC
	4. Sex DESC
	5. Vic Descent ASC
	6. Vic Descent DESC\n"""))
			break 
		elif(ch == 'n'):
			cur.execute("SELECT DR_NO, Age, Sex, Vic_Descent FROM VicLoc;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Would you like to sort the output (y or n)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def crimes(): # If on welcome screen and user selects Crimes
	print("""Crime Statistics
Please select an option:
	1. All Crime Data (with code descriptions only; THIS WILL TAKE A LONG TIME)
	2. Crimes by Date Reported
	3. Crimes by Date Committed
	4. Crimes by Time Committed
	5. Crimes by Victim Statistcs
	6. Crimes by Location Stats
	7. Crimes by Status
	8. Crimes by Area Stats
	9. Crimes by Code Stats
	10. Crimes by Weapon Stats
	11. Go Back""")
	choice = input("Enter your Choice (1-12): ")
	return choice

def crime1(): # If on Crimes and user selects option 1
	cur.execute("""
		SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed,
		Reporting_District, Age, Sex, Vic_Descent, Lat, Lon, Loc, Cross_Street,
		Status_Desc, Area_Name, Premis_Desc, Crime_Code_Desc, Weapon_Desc
		FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO INNER JOIN
		Status s ON c.Status=s.Status INNER JOIN Area a ON c.Area=a.Area
		INNER JOIN Codes co ON c.Crime_Code=co.Crime_Code INNER JOIN
		Weapon w ON c.Weapon_Code=w.Weapon_Code;""")
	# li = cur.fetchall()
	li = cur.fetchmany(10)
	for i in li:
		print(i)

def crime2(): # If on Crimes and user selects option 2
	ch = input("Ascending or Descending (a or d)? ")
	while(True):
		if(ch=='a'):
			cur.execute("SELECT * FROM Crime ORDER BY Date_Reported ASC;")
			break
		elif(ch=='d'):
			cur.execute("SELECT * FROM Crime ORDER BY Date_Reported DESC;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Ascending or Descending (a or d)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def crime3(): # If on Crimes and user selects option 3
	ch = input("Ascending or Descending (a or d)? ")
	while(True):
		if(ch=='a'):
			cur.execute("SELECT * FROM Crime ORDER BY Date_Committed ASC;")
			break
		elif(ch=='d'):
			cur.execute("SELECT * FROM Crime ORDER BY Date_Committed DESC;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Ascending or Descending (a or d)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def crime4(): # If on Crimes and user selects option 4
	ch = input("Ascending or Descending (a or d)? ")
	while(True):
		if(ch=='a'):
			cur.execute("SELECT * FROM Crime ORDER BY Time_Committed ASC;")
			break
		elif(ch=='b'):
			cur.execute("SELECT * FROM Crime ORDER BY Time_Committed DESC;")
			break
		else:
			print("Invalid response. Please enter again")
			ch = input("Ascending or Descending (a or d)? ")
	li = cur.fetchall()
	for i in li:
		print(i)

def crime5(): # If on Crimes and user selects option 5
	ch = int(input("""
Please Select the Victim Statistics you would like:
	1. Crimes on Victims of Specific Descent
	2. Crimes on Victims of Specific Age
	3. Crimes on Victims of Specific Sex
	4. Crimes and Victims Ordered By Age
	5. Crimes and Victims Ordered by Descent
	6. Crimes and Victims Ordered by Sex
	7. Go Back\n"""))
	while(True):
		if(ch==1):
			print("Inside Here")
			crime5_1()
			break
		elif(ch==2):
			crime5_2()
			break
		elif(ch==3):
			crime5_3()
			break
		elif(ch==4):
			ch = input("Ascending or Descending (a or d)? ")
			while(True):
				if(ch=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Age ASC;")
					break
				elif(ch=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Age DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					ch = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==5):
			ch = input("Ascending or Descending (a or d)? ")
			while(True):
				if(ch=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Vic_Descent ASC;")
					break
				elif(ch=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Vic_Descent DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					ch = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==6):
			ch = input("Ascending or Descending (a or d)? ")
			while(True):
				if(ch=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Sex ASC;")
					break
				elif(ch=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Sex DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					ch = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==7):
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Please Select the Victim Statistics you would like:
	1. Crimes on Victims of Specific Descent
	2. Crimes on Victims of Specific Age
	3. Crimes on Victims of Specific Sex
	4. Crimes and Victims Ordered By Age
	5. Crimes and Victims ORdered by Descent
	6. Crimes and Victims Ordered by Sex
	7. Go Back\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime5_1():
	ch = int(input("""
Select which Descent
	1. Other Asian
	2. Black
	3. Chinese
	4. Filipino
	5. Hispanic
	6. Native American
	7. Korean
	8. Other
	9. Vietnamese
	10. White
	11. Unknown\n"""))
	while(True):
		if(ch==1):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='A');")
			break
		elif(ch==2):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='B');")
			break
		elif(ch==3):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='C');")
			break
		elif(ch==4):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='F');")
			break
		elif(ch==5):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='H');")
			break
		elif(ch==6):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='I');")
			break
		elif(ch==7):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='K');")
			break
		elif(ch==8):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='O');")
			break
		elif(ch==9):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='V');")
			break
		elif(ch==10):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='W');")
			break
		elif(ch==11):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Vic_Descent='U' OR Vic_Descent IS NULL);")
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Select which Descent:
	1. Other Asian
	2. Black
	3. Chinese
	4. Filipino
	5. Hispanic
	6. Native American
	7. Korean
	8. Other
	9. Vietnamese
	10. White
	11. Unknown\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime5_2():
	ch = int(input("""
Select an option:
	1. Greater than
	2. Less than
	3. Equal to\n"""))
	inp = int(input("Enter the age "))
	while(True):
		if(ch==1):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Age > %s);", (inp,))
			break
		elif(ch==2):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Age < %s);", (inp,))
			break
		elif(ch==3):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Age = %s);", (inp,))
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Select an option
	1. Greater than
	2. Less than
	3. Equal to\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime5_3():
	ch = int(input("""
Select which Sex
	1. Female
	2. Male
	3. Unknown\n"""))
	while(True):
		if(ch==1):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Sex='F');")
			break
		elif(ch==2):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Sex='M');")
			break
		elif(ch==3):
			cur.execute("SELECT * FROM Crime WHERE DR_NO IN (SELECT DR_NO FROM VicLoc WHERE Sex='X' OR Sex IS NULL);")
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Select which Sex
	1. Female
	2. Male
	3. Unknown\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime6(): # If on Crimes and user selects option 6
	ch = int(input("""
Please Select an option:
	1. Crimes Sorted by Latitude
	2. Crimes Sorted by Longitude
	3. Crimes Sorted by Location
	4. Crimes Sorted by Cross Street
	5. Go Back\n"""))
	while(True):
		if(ch==1):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Lat ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Lat DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==2):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Lon ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Lon DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==3):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Loc ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Loc DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==4):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Cross_Street ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Reporting_District, Age, Sex, Vic_Descent FROM Crime c INNER JOIN VicLoc v ON c.DR_NO=v.DR_NO ORDER BY Cross_Street DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==5):
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Please Select an option:
	1. Crimes Sorted by Latitude
	2. Crimes Sorted by Longitude
	3. Crimes Sorted by Location
	4. Crimes Sorted by Cross Street
	5. Go Back\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime7(): # If on Crimes and user selects option 7
	ch = int(input("""
Select the status:
	1. Adult Other
	2. Invest Cont
	3. Adult Arrest
	4. Juv Arrest
	5. Juv Other
	6. Unknown\n"""))
	while(True):
		if(ch==1):
			cur.execute("SELECT * FROM Crime INNER JOIN Status ON Crime.Status=Status.Status WHERE Crime.Status='AO';")
			break
		elif(ch==2):
			cur.execute("SELECT * FROM Crime INNER JOIN Status ON Crime.Status=Status.Status WHERE Crime.Status='IC';")
			break
		elif(ch==3):
			cur.execute("SELECT * FROM Crime INNER JOIN Status ON Crime.Status=Status.Status WHERE Crime.Status='AA';")
			break
		elif(ch==4):
			cur.execute("SELECT * FROM Crime INNER JOIN Status ON Crime.Status=Status.Status WHERE Crime.Status='JA';")
			break
		elif(ch==5):
			cur.execute("SELECT * FROM Crime INNER JOIN Status ON Crime.Status=Status.Status WHERE Crime.Status='JO';")
			break
		elif(ch==6):
			cur.execute("SELECT * FROM Crime INNER JOIN Status ON Crime.Status=Status.Status WHERE Crime.Status='CC';")
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Select the status:
	1. Adult Other
	2. Invest Cont
	3. Adult Arrest
	4. Juv Arrest
	5. Juv Other
	6. Unknown\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime8(): # If on Crimes and user selects option 8
	ch = int(input("""
Please Select an option:
	1. Crimes Sorted by Area Code
	2. Crimes Sorted by Area Name
	3. Crimes Sorted by Premis Code
	4. Crimes Sorted by Premis Description
	5. Go Back\n"""))
	while(True):
		if(ch==1):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT * FROM Crime ORDER BY Area ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT * FROM Crime ORDER BY Area DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==2):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Reporting_District, Crime_Code, Weapon_Code, Area_Name FROM Crime c INNER JOIN Area a ON c.Area=a.Area ORDER BY Area_Name ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Reporting_District, Crime_Code, Weapon_Code, Area_Name FROM Crime c INNER JOIN Area a ON c.Area=a.Area ORDER BY Area_Name DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==3):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Reporting_District, Crime_Code, Weapon_Code, Premis_Code FROM Crime c INNER JOIN Area a ON c.Area=a.Area ORDER BY Premis_Code ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Reporting_District, Crime_Code, Weapon_Code, Premis_Code FROM Crime c INNER JOIN Area a ON c.Area=a.Area ORDER BY Premis_Code DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==4):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Reporting_District, Crime_Code, Weapon_Code, Premis_Desc FROM Crime c INNER JOIN Area a ON c.Area=a.Area ORDER BY Premis_Desc ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Reporting_District, Crime_Code, Weapon_Code, Premis_Desc FROM Crime c INNER JOIN Area a ON c.Area=a.Area ORDER BY Premis_Desc DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==5):
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Please Select an option:
	1. Crimes Sorted by Area Code
	2. Crimes Sorted by Area Name
	3. Crimes Sorted by Premis Code
	4. Crimes Sorted by Premis Description
	5. Go Back\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime9(): # If on Crimes and user selects option 9
	ch = int(input("""
Please Select an option:
	1. Crimes Sorted by Crime Code
	2. Crimes Sorted by Crime Code Description
	3. Crimes Sorted by Mocodes
	4. Go Back\n"""))
	while(True):
		if(ch==1):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT * FROM Crime ORDER BY Crime_Code ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT * FROM Crime ORDER BY Crime_Code DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==2):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Area, Reporting_District, Weapon_Code, Crime_Code_Desc FROM Crime c INNER JOIN Codes co ON c.Crime_Code=co.Crime_Code ORDER BY Crime_Code_Desc ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Area, Reporting_District, Weapon_Code, Crime_Code_Desc FROM Crime c INNER JOIN Codes co ON c.Crime_Code=co.Crime_Code ORDER BY Crime_Code_Desc DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==3):
			inp = input("Ascending or Descending (a or d)? ")
			while(True):
				if(inp=='a'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Area, Reporting_District, Weapon_Code, Mocodes FROM Crime c INNER JOIN Codes co ON c.Crime_Code=co.Crime_Code ORDER BY Mocodes ASC;")
					break
				elif(inp=='d'):
					cur.execute("SELECT c.DR_NO, Date_Reported, Date_Committed, Time_Committed, Status, Area, Reporting_District, Weapon_Code, Mocodes FROM Crime c INNER JOIN Codes co ON c.Crime_Code=co.Crime_Code ORDER BY Mocodes DESC;")
					break
				else:
					print("Invalid response. Please enter again")
					inp = input("Ascending or Descending (a or d)? ")
			break
		elif(ch==4):
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Please Select an option:
	1. Crimes Sorted by Crime Code
	2. Crimes Sorted by Crime Code Description
	3. Crimes Sorted by Mocodes
	4. Go Back\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def crime10(): # If on Crimes and user selects option 10
	ch = int(input("""
Select the type of weapon:
	1. Firearm
	2. Sharp Weapon
	3. Blunt Weapon
	4. No Weapon
	5. Extraneous Weapon\n"""))
	while(True):
		if(ch==1):
			cur.execute("SELECT * FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code=Weapon.Weapon_Code WHERE Crime.Weapon_Code LIKE '1__';")
			break
		elif(ch==2):
			cur.execute("SELECT * FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code=Weapon.Weapon_Code WHERE Crime.Weapon_Code LIKE '2__';")
			break
		elif(ch==3):
			cur.execute("SELECT * FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code=Weapon.Weapon_Code WHERE Crime.Weapon_Code LIKE '3__';")
			break
		elif(ch==4):
			cur.execute("SELECT * FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code=Weapon.Weapon_Code WHERE Crime.Weapon_Code LIKE '4__';")
			break
		elif(ch==5):
			cur.execute("SELECT * FROM Crime INNER JOIN Weapon ON Crime.Weapon_Code=Weapon.Weapon_Code WHERE Crime.Weapon_Code LIKE '5__';")
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
Select the type of weapon:
	1. Firearm
	2. Sharp Weapon
	3. Blunt Weapon
	4. No Weapon
	5. Extraneous Weapon\n"""))
	li = cur.fetchall()
	for i in li:
		print(i)

def update(): # If user wants to update data
	ch = int(input("""
What table would you like to update:
	1. Crime
	2. VicLoc
	3. Codes
	4. Area
	5. Status
	6. Weapon\n"""))
	while(True):
		if(ch == 1):
			col = int(input("""
Select the column to update:
	1. DR_NO
	2. Date Reported
	3. Date Committed
	4. Time Comitted
	5. Status
	6. Area
	7. Reporting District
	8. Crime Code
	9. Weapon Code\n"""))
			cond_col = int(input("""
Select the column for the Condition:
	1. DR_NO
	2. Date Reported
	3. Date Committed
	4. Time Comitted
	5. Status
	6. Area
	7. Reporting District
	8. Crime Code
	9. Weapon Code\n"""))
			val = input("Enter the new value: ")
			cond = input("Enter the condition: ")
			if(col == 1 and cond_col == 1):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 2):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 3):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 4):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 5):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 6):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 7):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 8):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 9):
				cur.execute("UPDATE Crime SET DR_NO = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 2 and cond_col == 1):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 2):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 3):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 4):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 5):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 6):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 7):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 8):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 9):
				cur.execute("UPDATE Crime SET Date_Reported = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 3 and cond_col == 1):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 2):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 3):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 4):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 5):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 6):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 7):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 8):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 9):
				cur.execute("UPDATE Crime SET Date_Committed = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 4 and cond_col == 1):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 2):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 3):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 4):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 5):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 6):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 7):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 8):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 9):
				cur.execute("UPDATE Crime SET Time_Committed = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 5 and cond_col == 1):
				cur.execute("UPDATE Crime SET Status = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 2):
				cur.execute("UPDATE Crime SET Status = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 3):
				cur.execute("UPDATE Crime SET Status = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 4):
				cur.execute("UPDATE Crime SET Status = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 5):
				cur.execute("UPDATE Crime SET Status = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 6):
				cur.execute("UPDATE Crime SET Status = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 7):
				cur.execute("UPDATE Crime SET Status = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 8):
				cur.execute("UPDATE Crime SET Status = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 9):
				cur.execute("UPDATE Crime SET Status = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 6 and cond_col == 1):
				cur.execute("UPDATE Crime SET Area = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 2):
				cur.execute("UPDATE Crime SET Area = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 3):
				cur.execute("UPDATE Crime SET Area = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 4):
				cur.execute("UPDATE Crime SET Area = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 5):
				cur.execute("UPDATE Crime SET Area = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 6):
				cur.execute("UPDATE Crime SET Area = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 7):
				cur.execute("UPDATE Crime SET Area = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 8):
				cur.execute("UPDATE Crime SET Area = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 9):
				cur.execute("UPDATE Crime SET Area = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 7 and cond_col == 1):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 2):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 3):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 4):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 5):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 6):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 7):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 8):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 9):
				cur.execute("UPDATE Crime SET Reporting_District = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 8 and cond_col == 1):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 2):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 3):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 4):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 5):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 6):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 7):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 8):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 9):
				cur.execute("UPDATE Crime SET Crime_Code = %s WHERE Weapon_Code = %s", (val, cond))
				break

			elif(col == 9 and cond_col == 1):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 2):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Date_Reported = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 3):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Date_Committed = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 4):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Time_Committed = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 5):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 6):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 7):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Reporting_District = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 8):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 9 and cond_col == 9):
				cur.execute("UPDATE Crime SET Weapon_Code = %s WHERE Weapon_Code = %s", (val, cond))
				break

		elif(ch == 2):
			col = int(input("""
Select the column to update:
	1. DR_NO
	2. Age
	3. Sex
	4. Victim Descent
	5. Latitude
	6. Longitude
	7. Location
	8. Cross Street\n"""))
			cond_col = int(input("""
Select the column for the Condition:
	1. DR_NO
	2. Age
	3. Sex
	4. Victim Descent
	5. Latitude
	6. Longitude
	7. Location
	8. Cross Street\n"""))
			if(col == 2):
				val = int(input("Enter the new value: "))
			else:
				val = input("Enter the new value: ")
			if(cond_col == 2):
				cond = int(input("Enter the condition: "))
			else:
				cond = input("Enter the condition: ")
			if(col == 1 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET DR_NO = %s WHERE Cross_Street = %s", (val, cond))
				break

			elif(col == 2 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET Age = %s WHERE Cross_Street = %s", (val, cond))
				break

			elif(col == 3 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET Sex = %s WHERE Cross_Street = %s", (val, cond))
				break

			elif(col == 4 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET Vic_Descent = %s WHERE Cross_Street = %s", (val, cond))
				break

			elif(col == 5 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 5 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET Lat = %s WHERE Cross_Street = %s", (val, cond))
				break

			elif(col == 6 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 6 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET Lon = %s WHERE Cross_Street = %s", (val, cond))
				break

			elif(col == 7 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 7 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET Loc = %s WHERE Cross_Street = %s", (val, cond))
				break

			elif(col == 8 and cond_col == 1):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE DR_NO = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 2):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE Age = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 3):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE Sex = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 4):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE Vic_Descent = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 5):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE Lat = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 6):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE Lon = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 7):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE Loc = %s", (val, cond))
				break
			elif(col == 8 and cond_col == 8):
				cur.execute("UPDATE VicLoc SET Cross_Street = %s WHERE Cross_Street = %s", (val, cond))
				break

		elif(ch == 3):
			col = int(input("""
Select the column to update:
	1. Crime_Code
	2. Crime_Code_Desc
	3. Mocodes
	4. All Crime Codes\n"""))
			cond_col = int(input("""
Select the column for the Condition:
	1. Crime_Code
	2. Crime_Code_Desc
	3. Mocodes
	4. All Crime Codes\n"""))
			val = input("Enter the new value: ")
			cond = input("Enter the condition: ")
			if(col == 1 and cond_col == 1):
				cur.execute("UPDATE Codes SET Crime_Code = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 2):
				cur.execute("UPDATE Codes SET Crime_Code = %s WHERE Crime_Code_Desc = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 3):
				cur.execute("UPDATE Codes SET Crime_Code = %s WHERE Mocodes = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 4):
				cur.execute("UPDATE Codes SET Crime_Code = %s WHERE All_Crime_Code = %s", (val, cond))
				break

			elif(col == 2 and cond_col == 1):
				cur.execute("UPDATE Codes SET Crime_Code_Desc = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 2):
				cur.execute("UPDATE Codes SET Crime_Code_Desc = %s WHERE Crime_Code_Desc = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 3):
				cur.execute("UPDATE Codes SET Crime_Code_Desc = %s WHERE Mocodes = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 4):
				cur.execute("UPDATE Codes SET Crime_Code_Desc = %s WHERE All_Crime_Code = %s", (val, cond))
				break

			elif(col == 3 and cond_col == 1):
				cur.execute("UPDATE Codes SET Mocodes = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 2):
				cur.execute("UPDATE Codes SET Mocodes = %s WHERE Crime_Code_Desc = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 3):
				cur.execute("UPDATE Codes SET Mocodes = %s WHERE Mocodes = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 4):
				cur.execute("UPDATE Codes SET Mocodes = %s WHERE All_Crime_Code = %s", (val, cond))
				break

			elif(col == 4 and cond_col == 1):
				cur.execute("UPDATE Codes SET All_Crime_Code = %s WHERE Crime_Code = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 2):
				cur.execute("UPDATE Codes SET All_Crime_Code = %s WHERE Crime_Code_Desc = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 3):
				cur.execute("UPDATE Codes SET All_Crime_Code = %s WHERE Mocodes = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 4):
				cur.execute("UPDATE Codes SET All_Crime_Code = %s WHERE All_Crime_Code = %s", (val, cond))
				break

		elif(ch == 4):
			col = int(input("""
Select the column to update:
	1. Area
	2. Area Name
	3. Premis
	4. Premis Code\n"""))
			cond_col = int(input("""
Select the column for the Condition:
	1. Area
	2. Area Name
	3. Premis
	4. Premis Code\n"""))
			val = input("Enter the new value: ")
			cond = input("Enter the condition: ")
			if(col == 1 and cond_col == 1):
				cur.execute("UPDATE Area SET Area = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 2):
				cur.execute("UPDATE Area SET Area = %s WHERE Area_Name = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 3):
				cur.execute("UPDATE Area SET Area = %s WHERE Premis_Code = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 4):
				cur.execute("UPDATE Area SET Area = %s WHERE Premis_Desc = %s", (val, cond))
				break

			elif(col == 2 and cond_col == 1):
				cur.execute("UPDATE Area SET Area_Name = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 2):
				cur.execute("UPDATE Area SET Area_Name = %s WHERE Area_Name = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 3):
				cur.execute("UPDATE Area SET Area_Name = %s WHERE Premis_Code = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 4):
				cur.execute("UPDATE Area SET Area_Name = %s WHERE Premis_Desc = %s", (val, cond))
				break

			elif(col == 3 and cond_col == 1):
				cur.execute("UPDATE Area SET Premis_Code = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 2):
				cur.execute("UPDATE Area SET Premis_Code = %s WHERE Area_Name = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 3):
				cur.execute("UPDATE Area SET Premis_Code = %s WHERE Premis_Code = %s", (val, cond))
				break
			elif(col == 3 and cond_col == 4):
				cur.execute("UPDATE Area SET Premis_Code = %s WHERE Premis_Desc = %s", (val, cond))
				break

			elif(col == 4 and cond_col == 1):
				cur.execute("UPDATE Area SET Premis_Desc = %s WHERE Area = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 2):
				cur.execute("UPDATE Area SET Premis_Desc = %s WHERE Area_Name = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 3):
				cur.execute("UPDATE Area SET Premis_Desc = %s WHERE Premis_Code = %s", (val, cond))
				break
			elif(col == 4 and cond_col == 4):
				cur.execute("UPDATE Area SET Premis_Desc = %s WHERE Premis_Desc = %s", (val, cond))
				break

		elif(ch == 5):
			col = int(input("""
Select the column to update:
	1. Status
	2. Status Description\n"""))
			cond_col = int(input("""
Select the column for the Condition:
	1. Status
	2. Status Description\n"""))
			val = input("Enter the new value: ")
			cond = input("Enter the condition: ")
			if(col == 1 and cond_col == 1):
				cur.execute("UPDATE Status SET Status = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 2):
				cur.execute("UPDATE Status SET Status = %s WHERE Status_Desc = %s", (val, cond))
				break

			elif(col == 2 and cond_col == 1):
				cur.execute("UPDATE Status SET Status_Desc = %s WHERE Status = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 2):
				cur.execute("UPDATE Status SET Status_Desc = %s WHERE Status_Desc = %s", (val, cond))
				break

		elif(ch == 6):
			col = int(input("""
Select the column to update:
	1. Weapon
	2. Weapon Description\n"""))
			cond_col = int(input("""
Select the column for the Condition:
	1. Weapon
	2. Weapon Description\n"""))
			val = input("Enter the new value: ")
			cond = input("Enter the condition: ")
			if(col == 1 and cond_col == 1):
				cur.execute("UPDATE Weapon SET Weapon_Code = %s WHERE Weapon_Code = %s", (val, cond))
				break
			elif(col == 1 and cond_col == 2):
				cur.execute("UPDATE Weapon SET Weapon_Code = %s WHERE Weapon_Desc = %s", (val, cond))
				break

			elif(col == 2 and cond_col == 1):
				cur.execute("UPDATE Weapon SET Weapon_Desc = %s WHERE Weapon_Code = %s", (val, cond))
				break
			elif(col == 2 and cond_col == 2):
				cur.execute("UPDATE Weapon SET Weapon_Desc = %s WHERE Weapon_Desc = %s", (val, cond))
				break

		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
What table would you like to update:
	1. Crime
	2. VicLoc
	3. Codes
	4. Area
	5. Status
	6. Weapon\n"""))
	conn.commit()

def insert(): # If user wants to insert new data
	ch = int(input("""
What table would you like to insert into:
	1. Crime
	2. VicLoc
	3. Codes
	4. Area
	5. Status
	6. Weapon\n"""))
	while(True):
		if(ch == 1):
			li = ['DR_NO', 'Date_Reported', 'Date_Committed', 'Time_Committed', 'Status', 'Area', 'Reporting_District', 'Crime_Code', 'Weapon_Code']
			for i in range(0,10):
				print(li[i])
				li[i] = input("Enter the data (Enter '-1' if NULL): ")
			for i in range(len(li)):
				if(li[i] == '-1'):
					li[i] = None
			cur.execute("INSERT INTO Crime VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7], li[8]))
			break
		elif(ch == 2):
			li = ['DR_NO', 'Age', 'Sex', 'Vic_Descent', 'Lat', 'Lon', 'Loc', 'Cross_Street']
			for i in range(0,9):
				print(li[i])
				li[i] = input("Enter the data (Enter '-1' if NULL): ")
			for i in range(len(li)):
				if(li[i] == '-1'):
					li[i] = None
			if(li[2] != None):
				li[2] = int(li[2])
			if(li[4] != None):
				li[4] = float(li[4])
			if(li[5] != None):
				li[5] = float(li[5])
			cur.execute("INSERT INTO VicLoc VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7]))
			break
		elif(ch == 3):
			li = ['Crime_Code', 'Crime_Code_Desc', 'Mocodes', 'All_Crime_Codes']
			for i in range(0,5):
				print(li[i])
				li[i] = input("Enter the data (Enter '-1' if NULL): ")
			for i in range(len(li)):
				if(li[i] == '-1'):
					li[i] = None
			cur.execute("INSERT INTO Codes VALUES(%s, %s, %s, %s)", (li[0], li[1], li[2], li[3]))
			break
		elif(ch == 4):
			li = ['Area', 'Area_Name', 'Premis_Code', 'Premis_Desc']
			for i in range(0,5):
				print(li[i])
				li[i] = input("Enter the data (Enter '-1' if NULL): ")
			for i in range(len(li)):
				if(li[i] == '-1'):
					li[i] = None
			cur.execute("INSERT INTO Area VALUES(%s, %s, %s, %s)", (li[0], li[1], li[2], li[3]))
			break
		elif(ch == 5):
			li = ['Status', 'Status_Desc']
			for i in range(0,2):
				print(li[i])
				li[i] = input("Enter the data (Enter '-1' if NULL): ")
			for i in range(len(li)):
				if(li[i] == '-1'):
					li[i] = None
			cur.execute("INSERT INTO Status VALUES(%s, %s)", (li[0], li[1]))
			break
		elif(ch == 6):
			li = ['Weapon_Code', 'Weapon_Desc']
			for i in range(0,2):
				print(li[i])
				li[i] = input("Enter the data (Enter '-1' if NULL): ")
			for i in range(len(li)):
				if(li[i] == '-1'):
					li[i] = None
			cur.execute("INSERT INTO Weapon VALUES(%s, %s)", (li[0], li[1]))
			break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
What table would you like to insert into:
	1. Crime
	2. VicLoc
	3. Codes
	4. Area
	5. Status
	6. Weapon\n"""))
	conn.commit()

def delete(): # If user wants to delete data
	ch = int(input("""
What table would you like to delete from:
	1. Crime
	2. VicLoc
	3. Codes
	4. Area
	5. Status
	6. Weapon\n"""))
	while(True):
		if(ch == 1):
			col = int(input("""
Select the column to delete from:
	1. DR_NO
	2. Date Reported
	3. Date Committed
	4. Time Comitted
	5. Status
	6. Area
	7. Reporting District
	8. Crime Code
	9. Weapon Code\n"""))
			cond = input("Enter the condition: ")
			if(col == 1):
				cur.execute("DELETE FROM Crime WHERE DR_NO = %s", (cond,))
				break
			elif(col == 2):
				cur.execute("DELETE FROM Crime WHERE Date_Reported = %s", (cond,))
				break
			elif(col == 3):
				cur.execute("DELETE FROM Crime WHERE Date_Committed = %s", (cond,))
				break
			elif(col == 4):
				cur.execute("DELETE FROM Crime WHERE Time_Committed = %s", (cond,))
				break
			elif(col == 5):
				cur.execute("DELETE FROM Crime WHERE Status = %s", (cond,))
				break
			elif(col == 6):
				cur.execute("DELETE FROM Crime WHERE Area = %s", (cond,))
				break
			elif(col == 7):
				cur.execute("DELETE FROM Crime WHERE Reporting_District = %s", (cond,))
				break
			elif(col == 8):
				cur.execute("DELETE FROM Crime WHERE Crime_Code = %s", (cond,))
				break
			elif(col == 9):
				cur.execute("DELETE FROM Crime WHERE Weapon_Desc = %s", (cond,))
				break
		elif(ch == 2):
			col = int(input("""
Select the column to update:
	1. DR_NO
	2. Age
	3. Sex
	4. Victim Descent
	5. Latitude
	6. Longitude
	7. Location
	8. Cross Street\n"""))
			cond = input("Enter the condition: ")
			if(col == 1):
				cur.execute("DELETE FROM VicLoc WHERE DR_NO = %s", (cond,))
				break
			elif(col == 2):
				cur.execute("DELETE FROM VicLoc WHERE Age = %s", (cond,))
				break
			elif(col == 3):
				cur.execute("DELETE FROM VicLoc WHERE Sex = %s", (cond,))
				break
			elif(col == 4):
				cur.execute("DELETE FROM VicLoc WHERE Vic_Descent = %s", (cond,))
				break
			elif(col == 5):
				cur.execute("DELETE FROM VicLoc WHERE Lat = %s", (cond,))
				break
			elif(col == 6):
				cur.execute("DELETE FROM VicLoc WHERE Lon = %s", (cond,))
				break
			elif(col == 7):
				cur.execute("DELETE FROM VicLoc WHERE Loc = %s", (cond,))
				break
			elif(col == 8):
				cur.execute("DELETE FROM VicLoc WHERE Cross_Street = %s", (cond,))
				break
		elif(ch == 3):
			col = int(input("""
Select the column to update:
	1. Crime_Code
	2. Crime_Code_Desc
	3. Mocodes
	4. All Crime Codes\n"""))
			cond = input("Enter the condition: ")
			if(col == 1):
				cur.execute("DELETE FROM Codes WHERE Crime_Code = %s", (cond,))
				break
			elif(col == 2):
				cur.execute("DELETE FROM Codes WHERE Crime_Code_Desc = %s", (cond,))
				break
			elif(col == 3):
				cur.execute("DELETE FROM Codes WHERE Mocodes = %s", (cond,))
				break
			elif(col == 4):
				cur.execute("DELETE FROM Codes WHERE All_Crime_Code = %s", (cond,))
				break
		elif(ch == 4):
			col = int(input("""
Select the column to update:
	1. Area
	2. Area Name
	3. Premis
	4. Premis Code\n"""))
			cond = input("Enter the condition: ")
			if(col == 1):
				cur.execute("DELETE FROM Area WHERE Area = %s", (cond,))
				break
			elif(col == 2):
				cur.execute("DELETE FROM Area WHERE Area_Name = %s", (cond,))
				break
			elif(col == 3):
				cur.execute("DELETE FROM Area WHERE Premis_Code = %s", (cond,))
				break
			elif(col == 4):
				cur.execute("DELETE FROM Area WHERE Premis_Desc = %s", (cond,))
				break
		elif(ch == 5):
			col = int(input("""
Select the column to update:
	1. Status
	2. Status Description\n"""))
			cond = input("Enter the condition: ")
			if(col == 1):
				cur.execute("DELETE FROM Status WHERE Status = %s;", (cond,))
				break
			elif(col == 2):
				cur.execute("DELETE FROM Status WHERE Status_Desc = %s;", (cond,))
				break

		elif(ch == 6):
			col = int(input("""
Select the column to update:
	1. Weapon
	2. Weapon Description\n"""))
			cond = input("Enter the condition: ")
			if(col == 1):
				cur.execute("DELETE FROM Weapon WHERE Weapon_Code = %s;", (cond,))
				break
			elif(col == 2):
				cur.execute("DELETE FROM Weapon WHERE Weapon_Desc = %s;", (cond,))
				break
		else:
			print("Invalid response. Please enter again")
			ch = int(input("""
What table would you like to update:
	1. Crime
	2. VicLoc
	3. Codes
	4. Area
	5. Status
	6. Weapon\n"""))
	conn.commit()

def main():
	choice = int(starting_Screen())
	while(True):
		if(choice == 1):
			c = int(weapons())
			while(True):
				if(c == 1):
					weapons1()
					break
				elif(c == 2):
					weapons2()
					break
				elif(c == 3):
					print("Going back...")
					break
				else:
					print("\nInvalid choice. Please enter again")
					c = int(weapons())

			
		elif(choice == 2):
			c = int(codes())
			while(True):
				if(c == 1):
					codes1()
					break
				elif(c == 2):
					codes2()
					break
				elif(c == 3):
					print("Going back...")
					break
				else:
					print("\nInvaild choice. Please enter again")
					c = int(codes())

			

		elif(choice == 3):
			c = int(location())
			while(True):
				if (c == 1):
					location1()
					break
				elif(c == 2):
					location2()
					break
				elif(c == 3):
					print("Going back...")
					break
				else:
					print("\nInvaild choice. Please enter again")
					c = int(location())
			

		elif(choice == 4):
			c = int(area())
			while(True):
				if(c == 1):
					area1()
					break
				elif(c == 2):
					area2()
					break
				elif(c == 3):
					area3()
					break
				elif(c == 4):
					print("Going back...")
					break
				else:
					print("\nInvaild choice. Please enter again")
					c = int(area())
			

		elif(choice == 5):
			c = int(police())
			while(True):
				if(c == 1):
					police1()
					break
				elif(c == 2):
					police2()
					break
				elif(c == 3):
					print("Going back...")
					break
				else:
					print("\nInvaild choice. Please enter again")
					c = int(police())
			

		elif(choice == 6):
			c = int(victims())
			while(True):
				if(c == 1):
					victims1()
					break
				elif(c == 2):
					victims2()
					break
				elif(c == 3):
					victims3()
					break
				elif(c == 4):
					print("Going back...")
					break
				else:
					print("\nInvaild choice. Please enter again")
					c = int(victims())
			

		elif(choice == 7):
			c = int(crimes())
			while(True):
				if(c == 1):
					crime1()
					break
				elif(c == 2):
					crime2()
					break
				elif(c == 3):
					crime3()
					break
				elif(c == 4):
					crime4()
					break
				elif(c == 5):
					crime5()
					break
				elif(c == 6):
					crime6()
					break
				elif(c == 7):
					crime7()
					break
				elif(c == 8):
					crime8()
					break
				elif(c == 9):
					crime9()
					break
				elif(c == 10):
					crime10()
					break
				elif(c == 11):
					print("Going back...")
					break
				else:
					print("\nInvaild choice. Please enter again")
					c = int(crimes())

		elif(choice == 8):
			insert()

		elif(choice == 9):
			update()

		elif(choice == 10):
			delete()		

		elif(choice == 11):
			print("Exiting...")
			cur.close()
			conn.close()
			break

		else:
			print("\n***Invalid choice. Please enter again***")
			choice = int(starting_Screen())

		choice = int(starting_Screen())
		
	print("Successfully exited connection")
	print("Have a nice day!")



db = input("Enter the name of the database: ")
hst = input("Enter the name of the host: ")
usr = input("Enter the the database user: ")
pword = input("Enter the database password: ")
prt = input("Enter the database port: ")

try:
	conn = psycopg2.connect(database=db, host=hst, user=usr, password=pword, port=prt)
except psycopg2.Error as e:
	print("Unable to connect!")
	print(e.pgerror)
	print(e.diag.message_detail)
	exit(1)

# For testing purposes, to speed up the process
# try:
# 	conn = psycopg2.connect(database='Crimes_LA', host='localhost', user='postgres', password='admin1116', port='5432')
# except psycopg2.Error as e:
# 	print("Unable to connect!")
# 	print(e.pgerror)
# 	print(e.diag.message_detail)
# 	exit(1)

print("Connected!")
cur = conn.cursor()
main()