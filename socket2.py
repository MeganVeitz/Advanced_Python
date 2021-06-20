# Megan Veitz
# HW Chp 12
# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters.

# The program should retrieve the entire document and count the total number of characters and display the count
# of the number of characters at the end of the document.

import socket
import validators


while True:
    website = input('Enter desired URL: ')
    if website.lower() == "exit":
        break
    valid_web = validators.url(website)
    if valid_web:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Url is valid.")
        websplit = website.split('/')
        try:
            mysock.connect((websplit[2], 80))
            cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(website)
            mysock.send(cmd.encode('utf-8'))
            length = 0
            first_data = None
            while True:
                # 3,000 characters = 3,000 bytes due to enforcing utf-8 encoding
                data = mysock.recv(3000)
                if len(data) < 1:
                    break
                if not first_data:
                    first_data = data
                length += len(data)
            print("The first 3,000 characters are:\n{}".format(first_data.decode()))
            print("the count of the total number of characters is: {}".format(length))
        except socket.gaierror:
            print("Not a valid site for sockets.")
            continue
        finally:
            mysock.close()

    else:
        print("Invalid url, try typing in another url.")

