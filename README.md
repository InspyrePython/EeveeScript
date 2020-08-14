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
func | None | After `func`, stop defining `func _str_` | See _Functions_
end | None | After a label, stop defining that label | `end` | See _Jumping_
call | func | Call function _func_ | `call foo` | See _Functions_
lprt | list, int | Print item _int_ of list _list_ | `lprt foo,1`
apnd | list, str\int | Append _str/int_ to _list_ | `apnd bar,hello`
n | None | Print a newline | `n`
io.clear | None | Clear the console | `io.clear`
pass | None | Pass and do nothing | `pass` 

## Using Stacks
There are 4 stacks in EeveeScript,
* eax
* ebx
* ecx
* and edx

All stacks behave the same.
As with the `mov` command, _stack_name_ can be any one of these values.

## Conditional Branching
### if
The `if` command is easy to handle.
There are 8 different varieties for `if`
* if eq; - Checks if the item at the position of the pointer is equal to the one next to it
* if neq; - Checks if the item at the position of the pointer is not equal to the one next to it
* if gr; - Checks if the item at the position of the pointer is greater than the one next to it
* if ls; - Checks if the item at the position of the pointer is less than the one next to it
* if eq _check_; - Checks if the item at the position of the pointer is equal to _check_
* if neq _check;_ - Checks if the item at the position of the pointer is not equal to _check_
* if gr _check_; - Checks if the item at the position of the pointer is greater than  _check_
* if ls _check_; - Checks if the item at the position of the pointer is less than _check_

Note:
You cannot execute ifs inside of an if, you have to do something like this:
```
if eq north;
print North it is..
else
pass
endif
if eq south;
print South.. Ok.
else
pass
endif
```

If the result is False, we move on to...
### else
Else executes the code under it **if** the if command above it resulted in False.
After, it goes to...
### endif
Endif ends the if/else statement.

## Control Flow
With the `for` command, we can repeat something x amount of times.
Example:
```
for 3
print bar
```
Note: 
You can't put `if` inside `for` loops
Yes, `while` is coming soon.

## Jumping
`jmp` is a special command.
`jmp` is like a train with "stops" that are labels
### What are "labels"?
Labels are words, followed by ":", that have code in the middle, and end with `end`.
An example of a label:
```
hello:
print hi
end
```
### Ok, so what's the purpose?
`jmp` allows you to jump to labels.
Example:
```
jmp say_hello
```
