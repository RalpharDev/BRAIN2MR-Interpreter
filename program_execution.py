import os

lp: int = 0
pointer = 0

cmd_list = [
	"R",
	"Rs",
	"Rc",
	"Rb",
	"Rx",
	"SND",
	"Wi",
]


cmd_list_args = [
	"BUY",
	"SLL",
	"JMP",
	"CPY",
	"W",
	"Wn",
	"M",
	"Mr",
	"Ml",
	"ADD",
	"SUB",
	"MUL",
	"DIV",
	"MOD",
]


units = []
max_units = 0
send = ""



def shift_pointer(val):
	global pointer
	pointer = (pointer + val) % len(units)


def exec_file(file_name):
	global lp
	global max_units
	f = open(f"projects/{file_name}")
	commands = f.read().split("\n")
	max_units = len(units)

	lp = 0
	while lp < len(commands):
		if not exec_line(commands[lp]): 
			print("==========================")
			print("-1: PREMATURE TERMINATION.")
			print("Exiting...")
			input()
			return

		lp += 1

	print("==========================")
	print("0: PROGRAM END.")
	print(f"Units used: {max_units}")
	print("Exiting...")
	input()


def verify_pointer(cmd) -> bool:
	global lp
	global pointer
	if pointer > len(units)-1: 
		print(f"ERROR at Line {lp}: cannot perform operation '{cmd}' on unauthorized unit.")
		return False

	return True


def arithmetic(ins, arg) -> bool:	
	global units
	global lp
	global pointer
	if len(units) < 1:
		print(f"ERROR at Line {lp}: cannot '{ins}' if unit 0 is unauthorized")
		return False

	if arg > len(units)-1:
		print(f"ERROR at Line {lp}: cannot '{ins}' because unit {arg} is unauthorized")
		return False
	
	if not verify_pointer(ins): return False
	match ins:
		case "ADD":
			units[0] = units[pointer] + units[arg]
		case "SUB":
			units[0] = units[pointer] - units[arg]
		case "MUL":
			units[0] = units[pointer] * units[arg]
		case "DIV":
			units[0] = int(units[pointer] / units[arg])
		case "MOD":
			units[0] = units[pointer] % units[arg]

	return True




def exec_line(line: str) -> bool:
	global lp
	global units
	global pointer
	global send
	global max_units
	command = line.split()
	# Ignore Comments and empty line
	if (len(command) == 0) or (command[0] == "INFO"):
		return True	
	
	## ERRORS
	if (len(command) == 1):
		if command[0] in cmd_list_args:
			print(f"ERROR at Line {lp}: command '{command[0]}' requires an argument but none were given.")
			return False
		if command[0] not in cmd_list:
			print(f"ERROR at Line {lp}: '{command[0]}' not a command.")
			return False
	if (len(command) == 2):
		if command[0] in cmd_list:
			print(f"ERROR at Line {lp}: command '{command[0]}' was given an argument when none required.")
			return False
		if command[0] not in cmd_list_args:
			print(f"ERROR at Line {lp}: '{command[0]}' not a command.")
			return False	
		if not command[1] == "$":
			if (not command[1].isnumeric()) or (float(int(command[1])) != float(command[1])):
				print(f"ERROR at Line {lp}: bad argument '{command[1]}'")
				return False


	ins = command[0]
	arg = 0
	if len(command) > 1: 
		if command[1] == "$":
			if len(units) > 0:
				arg = units[0]
			else:
				print(f"ERROR at line {lp}: cannot access unit 0 with '$' because it is unauthorized.")
				return False
		else:
			arg = int(command[1]) % 256

	match ins:
		# Memory
		case "BUY":
			for _ in range(arg):
				units.append(0)

			max_units = max(len(units), max_units)
		case "SLL":
			if arg > len(units):
				print(f"ERROR at Line {lp}: 'SLL' cannot sell unauthorized units.")
				return False

			units = units[:len(units)-arg]
			pointer = min(pointer, len(units)-1)


		# Write
		case "W":
			if not verify_pointer(ins): return False
			units[pointer] = arg
		case "Wn":
			if not verify_pointer(ins): return False
			units[pointer] = arg
			shift_pointer(1)
		case "Wi":
			if not verify_pointer(ins): return False
			user_input = input("> ")
			if len(user_input) > 0:
				if (user_input.isnumeric()) and (float(int(user_input)) == float(user_input)):
					# Int mode
					units[pointer] = int(user_input)
				else:
					# Char mode, only take first character
					units[pointer] = ord(user_input[0])

		# Copy
		case "CPY":
			if not verify_pointer(ins): return False
			if arg > len(units)-1:
				print(f"ERROR at Line {lp}: cannot '{ins}' because unit {arg} is unauthorized")
				return False

			units[pointer] = units[arg]



		# Read
		case "R":
			if not verify_pointer(ins): return False
			send += str(units[pointer])
		case "Rc":
			if not verify_pointer(ins): return False
			send += chr(units[pointer])
		case "Rs":
			if not verify_pointer(ins): return False
			val = 0
			if units[pointer] < 128:
				val = units[pointer]
			else:
				val = units[pointer] - 256
			send += str(val)
		case "Rb":
			if not verify_pointer(ins): return False
			send += str(bin(units[pointer])[2:])
		case "Rx":
			if not verify_pointer(ins): return False
			send += str(hex((units[pointer])))


		# Send
		case "SND":
			print(send)
			send = ""
			

		# Move
		case "Mr":
			shift_pointer(arg)
		case "Ml":
			shift_pointer(-arg)
		case "M":
			# if arg > len(units):
			# 	print(f"ERROR at Line {lp}: 'M' Cannot move to unauthorized unit")
			# 	return False
			pointer = arg


		# Flow Control
		case "JMP":
			if len(units) < 2:
				print(f"ERROR at Line {lp}: cannot 'JMP' if unit 1 is unauthorized")
				return False

			if units[1] == 0:
				lp = arg-1 # -1 because the first line (line 1) is index 0

		# Arithmetic
		case "ADD", "SUB", "MUL", "DIV", "MOD":
			if not arithmetic(ins, arg): return False







	return True 






if __name__ == "__main__":
	print("program_execution.py handles the \'r [file]\' command in main.py")