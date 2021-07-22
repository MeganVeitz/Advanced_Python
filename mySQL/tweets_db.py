# Meg Veitz
# 4/7/21
import mysql.connector


connect = None
try:
    # connect your database and python ide
    connect = mysql.connector.connect(user="root")
    # create cursor object, named cur
    with connect.cursor() as cur:
        # new datatbase
        cur.execute('CREATE DATABASE tweets_db')
        # new table
        cur.execute('CREATE TABLE `tweets_db`.`tweets` (\n'
                    '`tweet_id` INT NOT NULL AUTO_INCREMENT,\n'
                    '`username` VARCHAR(15) NOT NULL,\n'
                    '`date_of_tweet` TIMESTAMP,\n'
                    '`tweet_text` VARCHAR(280) NOT NULL,\n'
                    '`is_verified` BOOLEAN,\n'
                    ' PRIMARY KEY (`tweet_id`));')

except Exception as e:
    print("Exception Error")
    print(e)
finally:
    if connect:
        connect.close()
