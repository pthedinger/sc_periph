#!/usr/bin/python
import socket,sys

port = 501
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = sys.argv[1]

print "Connecting.."
sock.connect((server_ip, port))
print "Connected"

msg = "Hi from test client"
print "Sending message: " + msg
sock.sendall(msg)

print "Closing..."
sock.close()
print "Closed"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "Connecting.."
sock.connect((server_ip, port))
print "Connected"

msg = "Hi from test client"
print "Sending message: " + msg
sock.sendall(msg)

print "Closing..."
sock.close()
print "Closed"
