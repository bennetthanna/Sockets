import socket
import sys

if len(sys.argv) != 3:
	print "usage: ./client.py port_number input_file"
	exit(1)

try:
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Client: connecting"
	client_socket.connect(('127.0.0.1', int (sys.argv[1])))
	print "Client: connected"

	input_file = open(sys.argv[2])
	for line in input_file:
		client_socket.send(line)
	input_file.close()
	client_socket.close()

except Exception as err:
    print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(err), err
    exit(1)
