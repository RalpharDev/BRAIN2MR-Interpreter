import program_execution
import time
import os
import subprocess
import random


skip_loading: bool = False
skip_warning: bool = False

help_message = """
BRAIN2MR INTERPRETER 
by RalpharDev
Inspired by Brainfuck, an esolang developed by Urban Müller in 1993

[command list]
help - shows instructions (this message)
clr - clears the terminal
quit - quits the BRAIN2MR INTEPRETER
ls - lists all .2mr files in /projects

run [file] - runs [file].2mr in the /projects directory
ide [file]
"""


warning_message = """--- ATTENTION ---
Please note that the BRAIN2MR INTERPRETER is not free software. 
After a 0 day trial period, you must either buy a license ($500) or remove it from your computer. 
This notification shows up every time you open the BRAIN2MR INTERPRETER after your initial expired trial period.
"""


def print_loading():
	subprocess.call("cls", shell=True)
	progress = 0
	print("BRAIN2MR INTERPRETER.")
	time.sleep(random.randrange(1,5) * 0.1)
	print("INITIALIZING...")
	time.sleep(random.randrange(1,5) * 0.1)
	print("CHECKING PROJECTS FOLDER...")
	time.sleep(random.randrange(1,5) * 0.1)
	verify_projects_folder()
	print("PROJECTS FOLDER OK")
	time.sleep(random.randrange(1,5) * 0.1)
	print("CHECKING BRAIN TUMOR...")
	time.sleep(random.randrange(1,5) * 0.1)
	print("TUMOR IS BENIGN")
	time.sleep(random.randrange(1,5) * 0.1)
	print("CHECKING 2MR IDE...")
	time.sleep(random.randrange(1,5) * 0.1)
	print("IDE IS FUNCTIONAL")
	time.sleep(random.randrange(1,5) * 0.1)
	print("MOVING FAST AND BREAKING THINGS...")
	time.sleep(random.randrange(1,5) * 0.1)
	print("BROKE LITERALLY EVERYTHING")
	time.sleep(random.randrange(1,5) * 0.1)
	print("CHECKING MEMORY...")
	time.sleep(0.6)
	while progress < 16777215:
		progress += int(random.random() * 1000)
		progress = min(progress, 16777215)
		out = str(hex(progress))[2::].upper()
		print(f"ADDRESS {out} OK")


	time.sleep(0.3)
	print("STARTING BRAIN2MR INTEPRETER. WTF IS AN ESOLANG.")
	time.sleep(1)
	subprocess.call("cls", shell=True)
	time.sleep(0.5)


def print_warning():
	w_message_out = ""
	for c in warning_message:
		w_message_out += c
		time.sleep(0.02)
		subprocess.call("cls", shell=True)
		print(w_message_out + "█")

	time.sleep(0.4)
	subprocess.call("cls", shell=True)
	time.sleep(1)
	subprocess.call("cls", shell=True)



def verify_projects_folder():
	if not os.path.isdir("projects"):
		print("ERROR: 'projects' folder not found. Make sure you are in the correct directory (BRAIN2MR Intepreter)")
		print("Pressing any key to exit.")
		input()
		exit()




def main():
	if not skip_loading: print_loading()	
	if not skip_warning: print_warning()
	verify_projects_folder()

	while True:
		subprocess.call("cls", shell=True)
		print("┏┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")	
		time.sleep(0.05)
		print("┋                                   ┋")
		time.sleep(0.05)
		print("┋     BRAIN2MR INTERPRETER  v1.0    ┋")
		time.sleep(0.05)
		print("┋                                   ┋")
		time.sleep(0.05)
		print("┗┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")	
		time.sleep(0.05)


		command = []
		reset = False
		while not reset:
			command = (input("> ").lower()).split()
			if len(command) > 0:
				match command[0]:
					case "help":
						print(help_message)
					case "clr":
						reset = True
					case "quit":
						exit()
					case "ls":
						print("projects/")
						for item in os.listdir("projects"):
							if ".2mr" in item:
								print(f"- {item[:-4]}")
					case "run":
						if len(command) < 2:
							print("run [file] - runs [file].2mr in the /projects directory")
						else:
							if os.path.exists(f"projects/{command[1]}.2mr"):
								subprocess.call("cls", shell=True)
								program_execution.exec_file(f"{command[1]}.2mr")
								reset = True
							else:
								print(f"Cannot run file: {command[1]}.2mr as it does not exist.")

						


					case _:
						print(f"Unknown Command: {command[0]}")
						print("Type \'help\' for command list")


if __name__ == "__main__":
	main()