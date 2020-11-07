#!/usr/bin/env python
# --------------------------------------------------
# Miguel Riem Oliveira.
# PARI, September 2020.
# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
import time
import argparse


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# define example data to be sent to the server

while True:
    ap = argparse.ArgumentParser(description='Definition of a test mode:MESSAGE TO SEND:')

    ap.add_argument('-m', '--MS', type=str, default="xxx",
                    help=' Message to send.')

    args = vars(ap.parse_args())
    string = args['MS']
    messages = [str(string)]
    for message in messages:
        print ('Sending message: ' + str(message))
        message_formated = str(message).encode("utf-8")
        sock.sendall(message_formated)
        time.sleep(2)  # wait for two seconds
    if string=='q':
        break
sock.close()  # close connection

