def most_frq_words(s):
	empty = {}
	for string in s:
		if string in empty:
			empty[string] += 1
		else
		
SyntaxError: invalid syntax
def most_frq_words(s):
	empty = {}
	for string in s:
		if string in empty:
			empty[string] += 1
		else:
			empty[string] = 1
	print(empty)

	

 
 def most_frq_words(s):
	empty = {}
	for string in s:
		if string in empty:
			empty[string] += 1
		else:
			empty[string] = 1
	print(empty)

	
>>> most_frq_words("mom")
{'m': 2, 'o': 1}
>>> def most_frq_words(s):
	empty = {}
	for list in s:
		if string in empty:
			empty[string] += 1
		else:
			empty[string] = 1
	print(empty)


most_frq_words("cat, bat, bat, cat")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    most_frq_words("cat, bat, bat, cat")
  File "<pyshell#19>", line 4, in most_frq_words
    if string in empty:
NameError: name 'string' is not defined
>>> def most_frq_words(s):
	empty = {}
	s = s.split()
	for string in s:
		if string in empty:
			empty[string] += 1
		else:
			empty[string] = 1
	print(empty)

	
>>> most_frq_words("cat bat bat cat")
{'cat': 2, 'bat': 2}
>>> def most_frq_words(s):
	empty = {}
	s = s.replace(" ","")
	for string in s:
		if string in empty:
			empty[string] += 1
		else:
			empty[string] = 1
	print(empty)

	
>>> most_frq_words("cdad mom")
{'c': 1, 'd': 2, 'a': 1, 'm': 2, 'o': 1}
>>> 
