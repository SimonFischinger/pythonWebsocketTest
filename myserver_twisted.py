from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                       WebSocketServerFactory
 
 
class MyServerProtocol(WebSocketServerProtocol):
 
   def onMessage(self, payload, isBinary):
      self.sendMessage(payload, isBinary)
 
 
if __name__ == '__main__':
 
   import sys
 
   from twisted.python import log
   from twisted.internet import reactor
 
   log.startLogging(sys.stdout)
 
   factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
   factory.protocol = MyServerProtocol
 
   reactor.listenTCP(9000, factory)
   reactor.run()
