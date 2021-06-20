# Megan Veitz
# HW Chp 12
# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document.
#
# Don’t worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

from urllib import request, parse, error
import validators


while True:
    website = input('Enter desired URL: ')
    if website.lower() == "exit":
        break
    valid_web = validators.url(website)
    if valid_web:
        url_web = request.urlopen(website)
        count = 0
        line_string = ""
        for line in url_web:
            line_string = ""
            for char in line.decode().strip():
                count += 1
                if count < 3001:
                    line_string = line_string + char
            if line_string:
                print(line_string)
        print("Overall count is {}".format(count))

