class Handler: # Abstract handler
	def __init__(self, successor):
		self._successor = successor # Define who is the next handler

	def handle(self, request):
		handled = self._handle(request) # If handled, stop here

		# Otherwise, keep going
		if not handled:
			self._successor.handle(request)

	def _handle(self, request):
		raise NotImplementedError("Must provide implementation in the subclass.")

class ConcreteHandler1(Handler): # Inherits from the abstract handler
	def _handle(self, request):
		if 0 < request <= 10: # Provide a condition for handling
			print("Request {} handled in handler 1".format(request))
			return True

class DefaultHandler(Handler): # Inherits from the abstract handler

	def _handle(self, request):
		"""If there is no handler available"""
		# No condition checking since this is a default handler
		print("End of chain. no handler for {}".format(request))
		return True

class Client:
	def __init__(self):
		# Create handlers and use them in a sequence that you want
		self.handler = ConcreteHandler1(DefaultHandler(None))

	def delegate(self, requests): # Send requests one at a time
		for request in requests:
			self.handler.handle(request)

# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)