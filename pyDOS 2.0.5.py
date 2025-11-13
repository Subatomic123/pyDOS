import time
import os
import random

state = {
    "unrooted": False,
    "rooted": True,
    "system_deleted": False,
    "system_intact": True,
    "bin_deleted": False,
    "bin_intact": True,
    "daemon_deleted": False,
    "daemon_intact": False,
    "system_and_bin_deleted": False,
    "system_and_bin_intact": True,
    "Disk_A": True,
    "Disk_B": False,
    "Disk_C": False,
    "Disk_D": False,
    "cannot_open_programs": False
    
}



ver = "2.0.5"



def calc():
    if state["cannot_open_programs"]:
        print("opening...")
        time.sleep(1.3)
        print("cannot open.")
    else:
        print("|=================|")
        print("|(         Calculator           )|")
        print("|=================|")
        print("type 'exit'' to exit")
        print("type 'help' for help")
        while True:
            math1 = input("Enter Operation")
            if math1.lower() == "exit":
                break
            if math1.lower() == "help":
                print("+, -, / and x*")
                continue
            try:
                math2 = int(input("Enter first number"))
                math3 = int(input("Enter second Number"))
            except ValueError:
                print("Enter a valid number.")
                continue
            if math1.lower() == "+":  # why, nevermind
                math2 += math3
                print("=", math2)
            if math1.lower() == "-":
                math2 -= math3
                print("=", math2)
            if math1.lower() == "*":
                math2 *= math3
                print("=", math2)
            if math1.lower() == "/":
                try:
                	math2 /= math3
                	print("=", math2)
                except ZeroDivisionError:
                	print("Invalid calculation")
            if math1.lower() == "x":
                math2 *= math3
                print("=", math2)
			
			
def soon():
		while True:
			print("coming soon")
			time.sleep(1.5)
			break		
		
		

def money():
	print("|============|")
	print("|   money sim.    |")
	print("|============|")
	money2 = 100
	while True:
		try:
			money1 = int(input("choose amount of money"))
		except ValueError:
			print("invalid.")
			continue
		if money1 >= money2:
			print("Not enough money!")
		else:
			random.choice(["True", "False"])
			money2 += money1
			print("you won! you have this amount now!", money2)












print("Booting from floppy disk...")
time.sleep(1.5)
print("START")
time.sleep(0.5)
print("type 'help' for help")
time.sleep(0.1)
print("type 'shutdown' to shutdown")
time.sleep(0.5)

while True:
	
	if state["Disk_A"]:
		user = input("A:/")
	
	user_disk = user.lower()
	
	
	disks = "a", "b", "c", "d"
	    	
	

	if state["Disk_C"]:
		user = input("C:/")
		
		
	if state["Disk_B"]:
		user = input("B:/")
		
	if state["Disk_D"]:
		user = input("D:/")
		
	if user.lower() == "help":
		print("commands are: help, sysinfo, sysver, whoami, filesys, unroot, root, del, state, A:, B: C:, D:, shutdown, ls /directory/ (must be on /user/), {program name}.exe, fileinfo {file}, programs (to list programs)")
		
	if user.lower() == "programs":
		print("Apps are: calc.exe, coming_soon.exe, money.exe")
		
	
	if user.lower() == "sysinfo":
		print("Graphics: None")
		print("CPU: Intel(R) 80486(TM)")
		print("Operating System: pyDOS")
		print("Kernel: DOS ")
		print("Monitor: 16'7 Text mode")
		print("Timezone: GMT+2")
		local_time = time.localtime()
		print("Time:", local_time)
		print("ver:", ver)
		print("RAM free: 2MB")
		print("RAM total: 3MB")
		print("Floppy disk(s): 1MB")
		print("Hard disk: 4MB")
		print("Sound: PC speaker")
		print("programs: 2")
		print("programming language: Python")
		
	elif user.lower() == "sysver":
		print("ver:", ver)
	
	elif user.lower() == "whoami":
		if state["unrooted"]:
			print("user")
		else:
			print("root")
		
		
	elif user.lower() == "filesys":
		if state["system_and_bin_deleted"]:
		    print("/")
		    print("daemon/")
		elif state["bin_deleted"]:
		    print("/")
		    print("/system/")
		    print("daemon/")
		elif state["bin_intact"]:
		    print("/")
		    print("/bin/")
		    print("/system/")
		    print("daemon/")
		    
		elif state["system_intact"]:
		    print("/")
		    print("/bin/")
		    print("/system/")
		    print("daemon/")
		else:
		    print("/")
		    print("/bin/")
		    print("daemon/")
		  
			
		
		
	elif user.lower() == "unroot":
		print("you're no longer root.")
		state["unrooted"] = True
		state["rooted"] = False
		
	elif user.lower() == "root":
		print("You're now root!")
		state["unrooted"] = False
		state["rooted"] = True
		
	elif user.lower() == "del /system/":
		if state["rooted"]:
			confirm = input("are you sure? y/n")
			if confirm == "y":
			    state["cannot_open_programs"] = True
			    state["system_deleted"] = True
			    state["system_intact"] = False
			    print("system deleted.")
			    if state["bin_deleted"] and state["system_deleted"]:
			    	state["system_and_bin_deleted"] = True
			    	state["bin_deleted"] = False
			    	state["system_deleted"] = False
			
			else: print("Operation Cancelled.")
		
		else:
			print("Insufficient permissions.")
	
	
			
	elif user.lower() == "del /bin/":
		if state["rooted"]:
			confirm = input("are you sure? y/n")
			if confirm == "y":
			    state["cannot_open_programs"] = True
			    state["bin_deleted"] = True
			    state["bin_intact"] = False
			    print("bin deleted.")
			    if state["bin_deleted"] and state["system_deleted"]:
			    	state["system_and_bin_deleted"] = True
			    	state["bin_deleted"] = False
			    	state["system_deleted"] = False
			
			else: print("Operation Cancelled.")
		
		else:
			print("Insufficient permissions.")
			
			
			
			if state["system_and_bin_deleted"]:
				state["cannot_open_programs"] = True
			

			if state["system_and_bin_deleted"]:
						state["system_and_bin_intact"] = False
						
									
												
															
																		
																					
																								
																										
																																
	elif user.lower() == "state":
		print("States:")
		for key, value in state.items():
			print(f"{key}: {value}")

	elif user.lower() == "ls /user/":
		print("/Pictures/")
		print("/Other_files/")
		print("/Programs/")
		print("/Videos/")
		print("/data/")
		print("/trashbin/")
		
	elif user.upper() == "A:":
		state["Disk_A"] = True
		state["Disk_C"] = False
		state["Disk_B"] = False
		state["Disk_D"] = False
		print("A:")
	
			
	elif user.upper() == "C:":
		state["Disk_A"] = False
		state["Disk_C"] = True
		state["Disk_B"] = False
		state["Disk_D"] = False
		print("C:")
		
		
	elif user.lower() == "shutdown":
		print("shutting down...")
		time.sleep(1.5)
		break
	
	
	elif user.lower() == "calc.exe":
		print("opening...")
		time.sleep(2.5)
		calc()
		
	elif user.upper() == "B:":
		print("B:")
		state["Disk_B"] = True
		state["Disk_C"] = False
		state["Disk_A"] = False
		state["Disk_D"] = False
		
	elif user.upper() == "D:":
		print("D:")
		state["Disk_D"] = True
		state["Disk_C"] = False
		state["Disk_A"] = False
		state["Disk_B"] = False
		
		
	elif user.lower() == "ls /user/programs/":
		print("calc.exe")
		print("coming_soon.exe")
		print("money.exe")
		
	elif user.lower() == "fileinfo calc.exe":
		print("Last Modified: 27th of september, 2025")
		print("Directory: /user/programs/")
		print("Function: money()")
		print("Name: calc.exe")
		print("filetype: DOS executable")
		print("source: system")
		print("author: Microsoft")
		print("Description: Calculator for math.")
		print("size: 4 kilobytes")
		print("version: 1.0.4")
		
	elif user.lower() == "fileinfo coming_soon.exe":
				print("Name: coming_soon.exe")
				print("Function: soon()")
				print("Directory: /user/programs/")
				print("Last Modified: 28th of september, 2025")
				print("filetype: DOS executable")
				print("source: system")
				print("author: Microsoft")
				print("Description: Cool app coming soon.")
				print("size: 321 bytes")
				print("version: 1.0.0 Beta 1")
		
		
	
	elif user.lower() == "coming_soon.exe":
		if state["cannot_open_programs"]:
			print("opening...")
			time.sleep(0.7)
			print("CRITICAL: LNCHR2 = NULL")
		else:
			print("opening...")
			time.sleep(0.9)
			soon()
	
	elif user.lower() == "money.exe":
		if state["cannot_open_programs"]:
			time.sleep(0.98)
			print("CRITICAL: LNCHR2 = NULL")
		else:
			print("opening...")
			time.sleep(1.1)
			money()
	
	elif user.lower() == "fileinfo money.exe":
				print("Name: money.exe")
				print("Function: money()")
				print("Directory: /user/programs/")
				print("Last Modified: 29th of september, 2025")
				print("filetype: DOS executable")
				print("source: system")
				print("author: Microsoft")
				print("Description: Gain money in a simulator!")
				print("size: 17 kilobytes")
				print("version: 1.0.1")
				
				
	elif user.lower() == "fileinfo":
		print("enter program name")
		
	
	else:
		print("bad command, type 'help'")	