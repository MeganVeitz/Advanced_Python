# ############################
# Meg Veitz

import pymysql

mydatabase = "library_db"


connect = None
try:
    # connect your database and python ide
    connect = pymysql.connect(user="root")
    # create cursor object, named cur
    with connect.cursor() as cur:
        # new datatbase
        cur.execute('CREATE DATABASE {}'.format(mydatabase))
        # new table
        cur.execute('CREATE TABLE `library_db`.`books` (\n'
                    '`bid` VARCHAR(20),\n'
                    '`title` VARCHAR(30),\n'
                    '`author` VARCHAR(30),\n'
                    '`status` VARCHAR(30),\n'
                    ' PRIMARY KEY (`bid`));')

        cur.execute('CREATE TABLE `library_db`.`books_issued` (\n'
                    '`bid` VARCHAR(20),\n'
                    '`issuedto` VARCHAR(30),\n'
                    ' PRIMARY KEY (`bid`));')

except Exception as e:
    print("Exception Error")
    print(e)
finally:
    if connect:
        connect.close()
############################

# SQL goal:
# create database db;
# create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
# create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
