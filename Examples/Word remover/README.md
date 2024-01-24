Hello guy! This README is going to teach you how to use the better string class of this library!

The class is called String. It is in the Library directory `Bean` and in the module `string`.

Basics:
	initialising:
		You can make a custom string instance like this:

		# Import the string class

		from Bean.string import String

		# Make an instance, you can choose any value and name you want.

		name = String("Jake")

		# Print it or do something

		print(name)

	Replacing a word:
		To replace a word you can use the replace function:

		name = String("jake conner")

		name = name.replace('conner', 'smith')

		print(name) # output: jake smith

	Splitting the string:
		To split a string use the split function with the delimiter of your choice:

		name = String("jake conner")

		name = name.split(' ') # split by space

		print(name) # output: ['jake', 'smith']

	 	It also works with letters or whole strings:

	 	name = String("jake conner")

		name = name.split('ke') # split by 'ke'

		print(name) # output: ['ja', ' smith']

	Check for startswith and endswith:
		To check if a string starts with something, use the starts_with function with the prefix of your choice:

		name = String("jake conner")

		name = name.starts_with('jake')

		print(name) # output: True

		And if it doesn't

		name = String("jake conner")

		name = name.starts_with('c')

		print(name) # output: False

		To check if a string ends with something, use the ends_with function with the suffix of your choice:

		name = String("jake conner")

		name = name.ends_with('conner')

		print(name) # output: True

		And if it doesn't

		name = String("jake conner")

		name = name.ends_with('jake')

		print(name) # output: False
		
	Getting the string length:
		To get the string length simply use the '.len()' function and it'll return the len as an integer

	check if something is in the string:
		Just like normal string you can use the 'in' keyword to check if a string is in the string

	Count the number of specified text:
		To count the number of a specified text found in the string, simply use the '.number_of()' function with the text to count as the argument.

Optionally you can also remove a text by using the '.remove()' function and the text to remove as the argument, that can also be done with replace

Thanks for reading this! Have a good day.