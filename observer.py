class Subject(object): # Represents what is being 'observed'

	def __init__(self):
		self._observers = [] # This makes references to all the observers, and is a one-to-many relationship

	def attach(self, observer):
		# If the observer is not already in the observers list, append the observer to the list.
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer): # Remove the observer
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	def notify(self, modifier=None):
		for observer in self._observers: # For all the observers in the list
			if modifier != observer: # If `modifier` is not None, i.e. an observer is making the modification, then it doesn't need to be notified.
				observer.update(self)

class Core(Subject): # Inherits from the Subject class

	def __init__(self, name=""):
		Subject.__init__(self)
		self._name = name # set the name of the core
		self._temp = 0 # initialize the temperature of the core.

	@property # Getter that gets the core temperature
	def temp(self):
		return self._temp

	@temp.setter #Setter that sets the core temperature
	def temp(self, temp):
		self._temp = temp
		# Notify the observers whenever somebody changes the core temperature
		self.notify()

class TempViewer:

	def update(self, subject): # Alert method that is invoked when the temperature changes
		print("Temperature viewer: {} has Temperature {}".format(subject._name, subject._temp))


c1 = Core("Core 1")
c2 = Core("Core 2")

v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c1.temp = 90