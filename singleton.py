class Borg:

	# every instance of the class has access to the class attribute
	_shared_data = {}

	def __init__(self):
		self._dict__ = self._shared_data


class Singleton(Borg):

	def __init__(self, **kwargs):
		Borg.__init__(self)
		self._shared_data.update(kwargs)

	def __str__(self):
		return str(self._shared_data)

x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)
print(x)