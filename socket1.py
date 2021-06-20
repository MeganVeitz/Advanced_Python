# Megan Veitz
# HW Chp 12
# Exercise 1:
# Change the socket program socket1.py to prompt the user for the URL so it can read any web page.

# You can use split('/') to break the URL into its component parts
# so you can extract the host name for the socket connect call.

# Add error checking using try and except to handle the condition
# where the user enters an improperly formatted or non-existent URL.

import socket
import validators


while True:
    website = input('Enter desired URL: ')
    if website.lower() == "exit":
        break
    valid_web = validators.url(website)
    if valid_web == True:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Url is valid.")
        websplit = website.split('/')
        try:
            print("in try")
            mysock.connect((websplit[2], 80))
            cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(website)
            mysock.send(cmd.encode())
            while True:
                data = mysock.recv(512)
                if len(data) < 1:
                    break
                print(data.decode(), end='')
        except socket.gaierror as err:
            print("in except 1")
            print("Not a valid site for sockets.")
            print(err)
            continue
        finally:
            mysock.close()

    else:
        print("Invalid url, try typing in another url.")

