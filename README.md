# EeveeScript
___
EeveeScript is a programming language based off of Assembly, but easier.
## Key qualities
* Jumping - Like functions, but let you **move** around the code.
* Written in Python - Python is a very popular language, so making added EeveeScript functions should be easy.
* Frequent updates - EeveeScript is always expanding! 

## Functions
Function | Argument(s) | Description | Sample | Resources
------------ | ------------- | ------------- | ------------- | ------------------
_global start | None | Starts the program | `_global start`
_global end | None | Ends the program | `_global end`
push | int/str | Pushes  _int/str_ to the current stack. | `push 3`
push $ | variable |  Pushes _variable_ to the current stack. | `push $foo`
prt | None |  Prints current stack item at position of the pointer to the console. | `prt`
print | str |  Prints _str_ to console. | `print Hello World!`
print $ | variable |  Prints _variable_ to console. | `print $bar`
del | None | Deletes current item at the location of the pointer | `del`
cl | None | Clears the stack | `cl`
out | None | Prints the current position of the pointer | `out`
r | None | Moves the pointer right | `r`
l | None | Moves the pointer left | `l`
in | None | Pushes user input to stack | `in`
mov | stack_name | Moves current stack to stack_name | `mov ebx` | See _Using stacks_
if | condition, check | Compares item at postion of pointer to _check_ in some cases | `if eq` | See _Conditional Branching_
else | None | After `if`, if False, execute this | `else` 
endif | None| End conditional branch | `endif`
for | int | For _int_ times, execute this code | `for` | See _Control Flow_
endfor | None | End `for` loop | `endfor` 
int | name, int | Assign _name_ a value of _int_ | `int foo,34` | See _Variables_
str | name, str | Assign _name_ a value of _str_ | `str bar,hi` | See _Variables_ 
list | name, list | Assign _name_ a value of _list_ | `list barfoo,34,34` | See _Variables_
add | variable1, variable2 | Add _variable1_ and _variable2_ together and store the result in _variable1_| `add bar,foo`
sub | variable1, variable2 | Subtract _variable1_ and _variable2_ and store the result in _variable1_| `sub bar,foo`
mul | variable1, variable2 | Multiply _variable1_ and _variable2_ and store the result in _variable1_| `mul bar,foo`
jmp | str | Jump to label _str_ | `jmp foo` | See _Jumping_
func | str | Define _str_ | `func foo` | See _Functions_
end | None | After `func`, stop defining `func _str_` | `end` | See _Functions_
call | func | Call function _func_ | `call foo` | See _Functions_
