from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace


@namespace('/notifications')
class NotificationsNamespace(BaseNamespace):
    def on_msg(self, msg):
    	print self.request

        pkt = dict(type='event',
                   name='msg',
                   endpoint=self.ns_name)

        for sessid, socket in self.socket.server.sockets.iteritems():
        	pkt.update({'args': 'Someone said: {0}, {1}'.format(msg, sessid)})
        	socket.send_packet(pkt)