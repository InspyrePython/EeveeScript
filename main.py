a = open('code.eve', 'r')
pointer = 0
mem = {'eax':[0, 0], 'ebx':[0, 0], 'ecx':[0, 0], 'edx':[0, 0]}
stack = mem['eax'] 
stack_name = 'eax'
code = a.readline()
funcs = {}
varis = {}
import os, errors, time
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
	elif code[0:6] == 'push $':
		stack[pointer] = varis[code[6:-1]]
	elif code[0:5] == 'push ':
		stack[pointer] = code[5:code.find(';')]
	elif code == '_global stack\n':
		print(*stack)
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
	elif code[0:7] == 'print $':
		print(varis[code[7:-1]])
	elif code == 'in\n':
		d = list(input(''))
		for i in range(len(d)):
			stack.insert(i, d[i])
	elif code[0:6] == 'print ':
		print(code[6:], end = '')
	elif code[0:4] == 'mov ':
		stack_name = code[4:-1]
		stack = mem[code[4:-1]]
	elif code == 'n':
		print('')
	elif code == 'io.clear\n':
		os.system('clear')
	elif code == '_global start\n':
		pass
	elif code[0:6] == 'sleep ':
		time.sleep(int(code[6:]))
	elif code[0:0] == '!':
		pass
	elif code == '\n':
		pass
	elif code == 'endif\n':
		pass
	elif code == 'endfor\n':
		pass
	elif code == 'pass':
		pass
	elif code == 'else\n':
		pass
	elif code == 'if eq\n':
		pass
	elif code == 'if neq\n':
		pass
	elif code[0:6] == 'if eq ':
		pass
	elif code[0:6] == 'if ls ':
		pass
	elif code[0:6] == 'if gr ':
		pass
	elif code[0:6] == 'if neq ':
		pass
	elif code == 'if ls\n':
		pass
	elif code == 'if gr\n':
		pass
	elif code[0:4] == 'for ':
		pass
	elif code[0:9] == 'while eq ':
		pass
	elif code[0:4] == 'int ':
		if code[code.find(',') + 1:-1] == 'in':
			try:
				varis[code[4:code.find(',')]] = int(input(''))
			except ValueError:
				errors.raiseError(4, 'Cannot convert to int.')
		else:
			varis[code[4:code.find(',')]] = int(code[code.find(',') + 1:-1])
	elif code[0:5] == 'call ':
		for snip in funcs[code[5:]].split('\n'):
			stack, pointer = run(snip, stack, pointer)
	elif code[0:4] == 'jmp ':
		jmpto = code[4:-1]
		a = open('code.eve', 'r')
		while code != jmpto + ':\n': 
			code = a.readline()
	elif code == 'end\n':
		pass
	elif code == 'pass\n':
		pass
	elif code[0:4] == 'add ':
		add1 = varis[code[4:code.find(',')]]
		varis[code[4:code.find(',')]] = add1 + varis[code[code.find(',') + 1:-1]]
		varis[code[code.find(',') + 1:-1]] = 0
	elif code[0:4] == 'sub ':
		add1 = varis[code[4:code.find(',')]]
		varis[code[4:code.find(',')]] = add1 - varis[code[code.find(',') + 1:-1]]
		varis[code[code.find(',') + 1:-1]] = 0
	elif code[0:4] == 'mul ':
		add1 = varis[code[4:code.find(',')]]
		varis[code[4:code.find(',')]] = add1 * varis[code[code.find(',') + 1:-1]]
		varis[code[code.find(',') + 1:-1]] = 0
	else:
		try:
			if code[len(code) - 2] == ':':
				pass
			else:
				errors.raiseError(0, f"Unknown {code}")
		except:
			pass
	return stack, pointer
if code == '_global start\n':
	while code != '_global end':
		if code == 'l\n':
			if pointer > 0:
				pointer -= 1
			else:
				errors.raiseError(3, f'Pointer unable to go under 0.')
				break
		elif code == 'r\n':
			if pointer == len(stack):
				stack.append(0)
			else:
				pass
			pointer += 1
		elif code[0:6] == 'push $':
			if type(varis[code[6:code.find(',')]]) == list:
				stack[pointer] = varis[code[6:code.find(',')]][int(code[code.find(',') + 1:-1])]
			else:
				stack[pointer] = varis[code[6:-1]]
		elif code[0:4] == 'grb ':
			varis[code[4:-1]] = stack[pointer]
		elif code[0:5] == 'push ':
			stack[pointer] = code[5:code.find(';')]
		elif code == '_global stack\n':
			print(*stack)
		elif code == '_global stack_name\n':
			print(stack_name)
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
		elif code[0:7] == 'print $':
			print(varis[code[7:-1]])
		elif code == 'in\n':
			stack[pointer] = input('')
		elif code[0:6] == 'print ':
			print(code[6:], end = '')
		elif code[0:4] == 'mov ':
			stack_name = code[4:-1]
			stack = mem[code[4:-1]]
		elif code == 'if eq\n':
			if stack[pointer] == stack[pointer + 1]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code == 'if neq\n':
			if stack[pointer] != stack[pointer + 1]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code[0:6] == 'if eq ':
			if stack[pointer] == code[6:code.find(';')]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code[0:6] == 'if ls ':
			if stack[pointer] < code[6:code.find(';')]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code[0:6] == 'if gr ':
			if stack[pointer] < code[6:code.find(';')]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code[0:6] == 'if neq ':
			if stack[pointer] != code[6:code.find(';')]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code == 'if ls\n':
			if stack[pointer] < stack[pointer + 1]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code == 'if gr\n':
			if stack[pointer] < stack[pointer + 1]:
				while code != 'else\n':
					stack, pointer = run(code, stack, pointer)
					code = a.readline()
				while code != 'endif\n':
					code = a.readline()
			else:
				while code != 'else\n':
					code = a.readline()
		elif code[0:4] == 'for ':
			repeat = code[4:]
			forcode = ''
			while code != 'endfor\n':
				forcode += code
				code = a.readline()
			for i in range(int(repeat)):
				lfor = forcode.split('\n')
				lfor.remove(lfor[0])
				lfor.remove(lfor[len(lfor) - 1])
				for snip in lfor:
					stack, pointer = run(snip, stack, pointer)
		elif code[0:9] == 'while eq ':
			forcode = ''
			char = code[9:code.find(';')]
			while code != 'endwhile\n':
				forcode += code
				code = a.readline()
			while stack[pointer] == char:
				lfor = forcode.split('\n')
				lfor.remove(lfor[0])
				lfor.remove(lfor[len(lfor) - 1])
				for snip in lfor:
					stack, pointer = run(snip, stack, pointer)
		elif code == 'n':
			print('')
		elif code == 'io.clear\n':
			os.system('clear')
		elif code == '_global end':
			break
		elif code == '_global start\n':
			pass
		elif code == 'brg':
			code = a.readline()
		elif code[0:6] == 'sleep ':
			time.sleep(int(code[6:]))
		elif code[0:0] == '!':
			pass
		elif code == '\n':
			pass
		elif code == 'endif\n':
			pass
		elif code == 'endfor\n':
			pass
		elif code == 'pass':
			pass
		elif code == 'else\n':
			pass
		elif code[0:4] == 'int ':
			if code[code.find(',') + 1:-1] == 'in':
				try:
					varis[code[4:code.find(',')]] = int(input(''))
				except ValueError:
					errors.raiseError(4, 'Cannot convert to int.')
			else:
				varis[code[4:code.find(',')]] = int(code[code.find(',') + 1:-1])
		elif code[0:4] == 'str ':
			if code[code.find(',') + 1:-1] == 'in':
				varis[code[4:code.find(',')]] = input('')
			else:
				varis[code[4:code.find(',')]] = code[code.find(',') + 1:-1]
		elif code[0:5] == 'list ':
			parse = code[5:].split(',')
			parse[len(parse) - 1] = parse[len(parse) - 1].replace('\n', '')
			varis[parse[0]] = parse[1:]
		elif code[0:5] == 'func ':	
			funccode = ''
			name = code[5:]
			while code != 'func\n':
				funccode += code
				code = a.readline()
			funcs[name] = funccode
		elif code[0:5] == 'call ':
			for snip in funcs[code[5:]].split('\n'):
				stack, pointer = run(snip, stack, pointer)
		elif code[0:4] == 'jmp ':
			jmpto = code[4:-1]
			a = open('code.eve', 'r')
			while code != jmpto + ':\n': 
				code = a.readline()

		elif code == 'end\n':
			pass
		elif code[len(code) - 2] == ':':
			pass
		elif code == 'pass\n':
			pass
		elif code[0:4] == 'add ':
			add1 = varis[code[4:code.find(',')]]
			varis[code[4:code.find(',')]] = add1 + varis[code[code.find(',') + 1:-1]]
			varis[code[code.find(',') + 1:-1]] = 0
		elif code[0:4] == 'sub ':
			add1 = varis[code[4:code.find(',')]]
			varis[code[4:code.find(',')]] = add1 - varis[code[code.find(',') + 1:-1]]
			varis[code[code.find(',') + 1:-1]] = 0
		elif code[0:4] == 'mul ':
			add1 = varis[code[4:code.find(',')]]
			varis[code[4:code.find(',')]] = add1 * varis[code[code.find(',') + 1:-1]]
			varis[code[code.find(',') + 1:-1]] = 0
		elif code[0:5] == 'lprt ':
			print(varis[code[5:code.find(',')]][int(code[code.find(',') + 1:-1])])
		elif code[0:5] == 'apnd ':
			varis[code[5:code.find(',')]].append(code[code.find(',') + 1:-1])
		else:
			errors.raiseError(0, f"Unknown {code}")
		code = a.readline()