# Meg Veitz
# 4/7/21
import mysql.connector
import time

class TweetHandler:
    def __init__(self):
        pass

    def create_tweet(self, tweet_text, username, is_verified):
        try:
            connection = mysql.connector.connect(user="root")
            cursor = connection.cursor()
            now = time.strftime('%Y-%m-%d %H:%M:%S')

            create_twt = "INSERT INTO `tweets_db`.`tweets` (tweet_text, username, is_verified, date_of_tweet) VALUES (%s, %s, %s, %s);"
            user_input = (tweet_text, username, is_verified, now)

            cursor.execute(create_twt, user_input)
            connection.commit()

        except mysql.connector.Error as error:
            print("Couldn't create tweet: {}".format(error))
        finally:
            cursor.close()
            connection.close()
            print("MySQL create connection is closed")

    def update_tweet(self, id, tweet_text):
        try:
            connection = mysql.connector.connect(user="root")
            cursor = connection.cursor()

            update_cmd = """UPDATE `tweets_db`.`tweets` SET tweet_text = %s WHERE tweet_id = %s;"""
            input_text = (tweet_text, id)
            cursor.execute(update_cmd, input_text)
            connection.commit()
            print("Your Tweet was updated successfully!")
        except mysql.connector.Error as error:
            print("Couldn't update Tweet: {}".format(error))
        finally:
            cursor.close()
            connection.close()
            print("MySQL update connection is closed")

    def delete_tweet(sef, id):
        try:
            connection = mysql.connector.connect(user="root")
            cursor = connection.cursor()

            delete_twt = 'DELETE FROM `tweets_db`.`tweets` WHERE tweet_id = %s;'
            inputs = (id,)
            cursor.execute(delete_twt, inputs)
            connection.commit()
            print("You deleted the tweet with the id: {}".format(id))
        except mysql.connector.Error as error:
            print("Couldn't delete Tweet: {}".format(error))
        finally:
            cursor.close()
            connection.close()
            print("MySQL delete connection is closed")

    def read_all_tweets (self):
        # print all
        try:
            connection = mysql.connector.connect(user="root")
            cursor = connection.cursor()
            read_twts = 'SELECT * from `tweets_db`.`tweets`;'
            cursor.execute(read_twts)
            # get all records
            records = cursor.fetchall()
            print("Here are total number of tweets to read: \n", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                print("Id =  ", row[0], )
                print("Username = ", row[1])
                print("Date of Tweet = ", row[2])
                print("The Tweet Text: ", row[3])
                print("Is the User Verified: ", row[4], "\n")

        except mysql.connector.Error as error:
            print("Couldn't read Tweets: {}".format(error))
        finally:
            cursor.close()
            connection.close()
            print("MySQL read connection is closed")
