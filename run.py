from main import *
def run(code, stack, pointer):
	if code == 'l\n':
		if pointer > 0:
			pointer -= 1
		else:
			errors.raiseError(3, f'Pointer unable to go under 0.')
	elif code == 'r\n':
		if pointer == len(stack):
			stack.append(0)
		else:
			pass
		pointer += 1
	elif code[0:5] == 'push ':
		stack[pointer] = code[5:6]
	elif code == 'del\n':
		stack[pointer] = 0
	elif code == 'cl\n':
		stack.clear()
	elif code == 'prt\n':
		print(stack[pointer], end = '')
	elif code == 'out\n':
		print(pointer, end = '')
	elif code == 'aspoi\n':
		print(ord(stack[pointer]), end = '')
	elif code == 'in\n':
		d = input('')
		stack[pointer] = d[0]
	elif code[0:6] == 'print ':
		print(code[6:], end = '')		
	elif code == 'n':
		print('')
	elif io:
		if code == 'io.clear\n':
			os.system('clear')
	elif code in ioc and io == False:
		errors.raiseError(2, f'Unknown library {code}.')
	return stack, pointer