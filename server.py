import socket
import sys
import signal
import threading

bank_accounts = {}
mutex = threading.Lock()

def signal_handler(signum, frame):
	print "In signal handler"

	outputFile = open('log.txt', 'w+')

	for account in bank_accounts:
		outputFile.write('%s %s%r\n' % (account, '$', bank_accounts[account]))

	outputFile.close()
	server_socket.close()
	exit(1)

if len(sys.argv) != 2:
	print "usage: ./server.py port_number"
	exit(1)

try:
	signal.signal(signal.SIGINT, signal_handler)
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('127.0.0.1', int (sys.argv[1])))
	server_socket.listen(5)

	(connection, address) = server_socket.accept()
	data = connection.recv(1000)
	line = data.split('\n')
	empty_string = ''
	if empty_string in line:
		line.remove('')

	for transaction in line:
		transaction_information = transaction.split(' ')

		if transaction_information[1] == 'debit' or transaction_information[1] == 'credit':
			if transaction_information[1] == 'debit':
				amount = transaction_information[2].replace('$', '')
				amount = float(amount)
				amount *= (-1)
			elif transaction_information[1] == 'credit':
				amount = transaction_information[2].replace('$', '')
				amount = float(amount)

			if transaction_information[0] in bank_accounts:
				bank_accounts[transaction_information[0]] += amount
			else:
				bank_accounts.update({transaction_information[0]: amount})

	while(1):
		pass

except Exception as err:
    print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(err), err
    exit(1)
