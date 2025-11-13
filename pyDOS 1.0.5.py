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
    "Disk_A": False,
    "Disk_B": False,
    "Disk_C": True,
    "Disk_D": False
    
}







print("Booting from floppy disk...")
time.sleep(1.5)
print("START")
time.sleep(0.5)
print("type 'help' for help")
time.sleep(0.1)

while True:
	
	if state["Disk_C"]:
		user = input("C:/")
	
	user_disk = user.lower()
	
	
	disks = "a", "b", "c", "d"
	    	
	

	if state["Disk_A"]:
		user = input("A:/")
		
	if user.lower() == "help":
		print("commands are: help, sysinfo, sysver, whoami, filesys, unroot, root, del, state, A:, C:")
		
	
	if user.lower() == "sysinfo":
		print("Graphics: None")
		print("CPU: Intel(R) 80486(TM)")
		print("Operating System: DOS")
		print("Kernel: SOD")
		print("Monitor: 16'7 Text mode")
		print("Timezone: GMT+2")
		local_time = time.localtime()
		print("Time:", local_time)
		print("ver: 1.0.4")
		print("RAM free: 2MB")
		print("RAM total: 3MB")
		print("Floppy disk(s): 1MB")
		print("Hard disk: 4MB")
		print("Sound: PC speaker")
		
	elif user.lower() == "sysver":
		print("ver: 1.0.4")
	
	elif user.lower() == "whoami":
		if state["unrooted"]:
			print("user")
		else:
			print("root")
		
		
	elif user.lower() == "filesys":
		if state["system_and_bin_deleted"]:
		    print("/")
		    print("daemon/")
		if state["bin_deleted"]:
		    print("/")
		    print("/system/")
		    print("daemon/")
		if state["bin_intact"]:
		    print("/")
		    print("/bin/")
		    print("/system/")
		    print("daemon/")
		    
		if state["system_intact"]:
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
			    state["system_deleted"] = True
			    state["system_intact"] = False
			    print("system deleted.")
			
			else: print("Operation Cancelled.")
		
		else:
			print("Insufficient permissions.")
	
	
			
	elif user.lower() == "del /bin/":
		if state["rooted"]:
			confirm = input("are you sure? y/n")
			if confirm == "y":
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
			
			
	elif user.lower() == "state":
		print("States:")
		for key, value in state.items():
			print(f"{key}: {value}")

	elif user.lower() == "ls /user/":
		print("/Pictures/")
		print("/Other_files/")
		
		
	elif user.upper() == "A:":
		state["Disk_A"] = True
		state["Disk_C"] = False
		print("A:")
	
			
	elif user.upper() == "C:":
		state["Disk_A"] = False
		state["Disk_C"] = True
		print("C:")
		
	

	
	
	
	
	
	else:
		print("bad command, type 'help'")