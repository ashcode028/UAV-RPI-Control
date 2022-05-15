# Import socket module
import socket
import numpy as np

def random_data():

    x1 = np.random.randint(0, 55, None)         # Dummy temperature
    y1 = np.random.randint(0, 45, None)         # Dummy humidigy
    my_sensor = "{},{}".format(x1,y1)
    return my_sensor 
        
        
        
def client():
	# local host IP '127.0.0.1'
	host = '192.168.1.9'

	# Define the port on which you want to connect
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# connect to server on local computer
	s.connect((host,port))

	while True:
		message = random_data()
		# message sent to server
		s.send(message.encode('utf-8'))
		data = s.recv(1024)
 
		# print the received message
		# here it would be a reverse of sent message
		print('Received from the server :',str(data.decode('ascii')))
 
	s.close()

if __name__ == '__main__':
	client()

