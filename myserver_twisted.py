from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                       WebSocketServerFactory
 
 
class MyServerProtocol(WebSocketServerProtocol):
	def onMessage(self, payload, isBinary):
		messageCounter()	
		self.sendMessage(payload+"hellooooooooo", isBinary)
		
		if (getCount() == 5):
			self.sendMessage("FUMPF")
			
 

count = 0;
def messageCounter():
	global count
	count += 1

def getCount():
	global count
	return count
	 
if __name__ == '__main__':
 
   import sys
 
   from twisted.python import log
   from twisted.internet import reactor
 
   log.startLogging(sys.stdout)
 
   factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
   factory.protocol = MyServerProtocol
 
   reactor.listenTCP(9000, factory)
   reactor.run()
