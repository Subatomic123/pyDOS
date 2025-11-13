import time
import os
import random
import logging
from datetime import datetime
date = datetime.now().astimezone()

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
    "cannot_open_programs": False,
    "dummy": True,
    "HDD": False,
    "Floppy": True,
    "Network": False,
    "CD": False,
    "booting": True,
    "rebooted": False,
    "cannot_boot": False
    
}



procs =  {

"system32": "Active",
"Taskmngr.exe":" Inactive",
"calc.exe": "Inactive",
"coming_soon.exe": "Inactive",
"money.exe": "Inactive",
"explorer.exe": "Active",
"sysWOW64": "Active",
"win32": "Active"

}

pid = {

"system32": "1",
"taskmngr.exe": "2",
"calc.exe": "3",
"coming_soon.exe": "4",
"money.exe": "5",
"explorer.exe": "6",
"sysWOW64": "7",
"win32": "8"

}

filesys = (["/system/", "/bin/", "/init/", "/dalvik/", "init.rc", "/daemon/", "/boot/", "/krnl/"])



ver = "3.0.0 Beta 4"
programs = 5
dummy = 0




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

def task_manager():
        procs.update({"Taskmngr.exe": "Active"})
        while True:
            print("type 'help' for help")
            print("type 'exit' to exit")
            task = input("Type the program you want to pkill:")
            if "system32" in task.lower():
                procs.update({"system32": "Inactive"})
                print("process stopped ((")
            if task.lower() == "procs":
                       for key, value in procs.items():
                           print("---------------")
                           print(f"{key}:{value}")
                           print("----------------")
            if task.lower() == "exit":
                   break
            if task.lower() == "pid":
                   for key, value in pid.items():
                       print("-----------------")
                       print(f"{key}:{value}")
                       print("-----------------")
            if task.lower() == "help":
                   print("exit, procs, pid and help, type process name to pkill")
            if "taskmngr.exe" in task.lower():
                   break
            if "calc.exe" in task.lower():
                   print("Program calc.exe is already connected!")
            if "win32" in task.lower():
                   procs.update({"win32": "Inactive"})
                   
def kernel_panic():
                   print("\033[31mKERNEL PANIC\033[0m")
                   print("\033[32mP y D O S\033[0m")
                   while True:
                       time.sleep(1)
                   
def devtool():
    print("type 'help' for help")
    print("type 'exit to exit")
    while True:
        user2 = input("")
        if user2.lower() == "hardbrick":
            hardbrick()
        if user2.lower() == "bootloop":
            bootloop()
        if user2.lower() == "help":
            print("bootloop, hardbrick, exit, help, krnlpnc")
        if user2.lower() == "exit":
            break
        if user2.lower() == "krnlpnc":
            kernel_panic()


def post():
            print("\033[32mTrue\033[0m")
            if "/system/" not in filesys and "/bin/" not in filesys or "/boot/" not in filesys:
                hardbrick()
            else:
                state["booting"] = True
                print("Floppy Disk.... OK")
                time.sleep(0.5)
                print("RAM.... OK")
                time.sleep(0.5)
                print("Processor.... OK")
                time.sleep(1)
                bios()


def bios():
		if "/system/" not in filesys:
		    bootloop()
		if state["booting"]:
			print("/=============/")
			print("/     I      B           M  /")
			print("/============/")
			time.sleep(1)
			mbr()
		else:
		  print("rebooting to BIOS...")
		  time.sleep(6)
		  for i in range(1000):
		  	print("")
		  print("type 'help' for help")
		  print("type 'reboot' to reboot")
		  while True:
		      user = input("bios >>>")
		      if user.lower() == "help":
		      	print("help, reboot, lpmode, boot_device")
		      elif user.lower() == "reboot":
		           print("exiting...")
		           time.sleep(1)
		           reboot()
		      elif user.lower() == "lpmode":
		          confirm = input("would you really like to enter lpmode? y/n")
		          if confirm == "y":
		              print("rebooting into lpmode...")
		              time.sleep(1)
		              safemode()     	
		      if user.lower() == "boot_device":
		          	options = input("Options: HDD (type H) Floppy Disk (type F), CD-ROM (type C), Network (Type N):   =   ")
		          	if options == "H":
		          	       	if not state["HDD"]:
		          	       	    state["HDD"] = True
		          	       	    state["Floppy"] = False
		          	       	    reboot()
					

		
	
	
def safemode():
	print("you're in low-power mode.")
	print("type 'help' for help")
	print("type 'bios' to go to bios")
	while True:
		safeuser = input("RAM:/")
		if safeuser.lower() == "bios":
			time.sleep(1)
			print("going to bios...")
			time.sleep(3)
			break
		elif safeuser.lower() == "help":
			time.sleep(1)
			print("help, bios")
			
			
	


def reboot():
	    state["rebooted"] = True
	    time.sleep(2)
	    print("rebooting to system...")
	    time.sleep(1)
	    post()

def bootloop():
        while True:
            print("Booting from floppy disk...")
            time.sleep(2)

def hardbrick():
    if "/boot/" not in filesys:
        syshalt()
    print("\033[31mCRITICAL: No bootable target!!\033[0m")
    while True:
        time.sleep(1)
        
def syshalt():
    print("\033[31mSYSTEM HALTED\033[0m")



def mbr():
    if state["booting"]:
        print("=MASTER BOOT RECORD=")
        time.sleep(2)
        print("Finding stage2...")
        time.sleep(3)
        print("\033[32mFoun9\033[0m")
        time.sleep(0.1)
        bootstage2()

def bootstage1():
    if state["system_and_bin_deleted"]:
        if state["rebooted"]:
            state["cannot_boot"] = True
    else: 
        if state["Floppy"]:
            print("Booting from Floppy Disk..")
            print("/*********\\")
            print("/  pyDOS        \\")
            print("\\*********/")
            print("   ------------")
            mbr()
    if state["HDD"]:
    	print("Booting from Hard Drive...")
    	print("/*********\\")
    	print("/  pyDOS        \\")
    	print("\\*********/")
    	print("   ------------")
    	mbr()
    	
    	
def bootstage2():    	
    time.sleep(2.0)
    for i in range(500):
        print("")
    print("\033[32mSTART\033[0m")
    time.sleep(0.5)
    print("type 'help' for help")
    time.sleep(0.1)
    print("type 'shutdown' to shutdown")
    time.sleep(0.5)
    DOS()
    
def DOS():
    state["booting"] = False
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
            print("commands are: help, sysinfo, sysver, whoami, filesys, unroot, root, del, state, A:, B: C:, D:, shutdown, ls /directory/ (must be on /user/), {program name}.exe, fileinfo {file}, programs (to list programs), numprog (to show number of programs), bios")

        if user.lower() == "programs":
            print("Apps are: calc.exe, coming_soon.exe, money.exe, taskmngr.exe")

        if user.lower() == "numprog":
            print("Number of programs:", programs)

        if user.lower() == "sysinfo":
            print("Graphics: None")
            print("CPU: Intel(R) 80486(TM)")
            print("Operating System: pyDOS")
            print("Kernel: DOS ")
            print("Monitor: 16'7 Text mode")
            print("Timezone:", time.tzname)
            print(date.strftime("Date: %Y-%m-%d at %H:%M"))
            print("Offset:", date.strftime("%z"))
            print("ver:", ver)
            print("RAM free: 2MB")
            print("RAM total: 3MB")
            print("Floppy disk(s): 1MB")
            print("Hard disk: 4MB")
            print("Sound: PC speaker")
            print("programs:", programs)
            print("programming language: Python")
            
            
            
        
        elif user.lower() == "sysver":
            print("ver:", ver)

        elif user.lower() == "whoami":
            if state["unrooted"]:
                print("user")
            else:
                print("root")

        elif user.lower() == "filesys":
            print(filesys)

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
                    filesys.remove("/system/")
                    state["cannot_open_programs"] = True
                    state["system_deleted"] = True
                    state["system_intact"] = False
                    print("system deleted.")
                    if state["bin_deleted"] and state["system_deleted"]:
                        state["system_and_bin_deleted"] = True
                        state["bin_deleted"] = False
                        state["system_deleted"] = False
                else:
                    print("Operation Cancelled.")
            else:
                print("Insufficient permissions.")

        elif user.lower() == "del /bin/":
            if state["rooted"]:
                confirm = input("are you sure? y/n")
                if confirm == "y":
                    filesys.remove("/bin/")
                    state["cannot_open_programs"] = True
                    state["bin_deleted"] = True
                    state["bin_intact"] = False
                    print("bin deleted.")
                    if state["bin_deleted"] and state["system_deleted"]:
                        state["system_and_bin_deleted"] = True
                        state["bin_deleted"] = False
                        state["system_deleted"] = False
                else:
                    print("Operation Cancelled.")
            else:
                print("Insufficient permissions.")

            if state["system_and_bin_deleted"]:
                state["cannot_open_programs"] = True

            if state["system_and_bin_deleted"]:
                state["system_and_bin_intact"] = False

        elif user.lower() == "del /boot/":
            confirm4 = input("Are you sure? y/n")
            if confirm4 == "y":
                if state["rooted"]:
                    filesys.remove("/boot/")
                else:
                    print("Not enough permissions.")
            else:
                print("Operation Cancelled.")
        
        
        elif user.lower() == "del /krnl/":
            confirm5 = input("Are you sure? y/n")
            if confirm5 == "y":
                if state["rooted"]:
                    filesys.remove("/krnl/")
                else:
                    print("Insufficient Permissions")
            else:
                print("Operation Cancelled.")
            
        
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
            if state["rooted"]:
                state["Disk_A"] = False
                state["Disk_C"] = True
                state["Disk_B"] = False
                state["Disk_D"] = False
                print("C:")
            else:
                print("Insufficient Permissions: Protected Disk")

        elif user.lower() == "shutdown":
            print("Shutting down...")
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

        elif user.lower() == "bios":
            print("Going to bios...")
            time.sleep(4)
            bios()
        elif user.lower() == "reboot":
             reboot()
        elif user.lower() == "taskmngr.exe":
            print("Opening...")
            time.sleep(0.9)
            task_manager()
        elif user.lower() == "devtools.exe":
            time.sleep(0.9)
            print("Opening...")
            devtool()


        else:
            print("bad command, type 'help'")
            
            
             
            
            
            
post()