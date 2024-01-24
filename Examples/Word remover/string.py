class String:
	def __init__(self, text):
		self._text: str = str(text)

	def starts_with(self, prefix):
		if not isinstance(prefix, String):
			return self._text[0:len(prefix)] == prefix

		return self._text[0:prefix.len()] == prefix._text

	def ends_with(self, suffix):
		if not isinstance(suffix, String):
			return self._text[-len(suffix):] == suffix

		return self._text[-suffix.len():] == suffix._text		

	def len(self):
		length = 0

		for char in self._text: length += 1

		return length

	def replace(self, target, to):
		return self._text.replace(target, to)

	def remove(self, target):
		return self.replace(target, '')

	def split(self, delimiter:str=None):
		if delimiter: return self._text.split(delimiter)

		return self._text.split()

	def number_of(self, char:str):
		count = 0

		for c in self._text:
			if c == char: count += 1

		return count

	def __str__(self):
		return self._text

	def __int__(self):
		return int(self._text)
	
	def __float__(self):
		return float(self._text)
	
	def __bool__(self):
		return bool(self._text)
	
	def __len__(self):
		return self.len()
	
	def __repr__(self):
		return f'String(\'{self._text}\')'

	def __contains__(self, other):
		return other in self._text