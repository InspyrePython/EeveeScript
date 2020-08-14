errors = [
	'SyntaxError',
	'ImportError',
	'IncludeError',
	'PointerError',
	'TypeError',
]
def raiseError(errorindex, message):
	import replit
	replit.clear()
	print(f'\033[31m{errors[errorindex]}: {message}')