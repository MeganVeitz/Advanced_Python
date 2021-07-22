# Meg Veitz
# 4/7/21
# Create a menu driven CRUD application that handles tweets
# This will be a single db/single table that has the following columns: username, date_of_tweet, tweet_text, is_verified
# Menu options need to include: Create, Update, Read, and Delete a tweet

from mySQL.twitter_functions import TweetHandler
handler = TweetHandler()

cmd = True
while cmd:
    print(20 * '-')
    print(" M A I N - M E N U")
    print(20 * '-')
    print("1. Create Tweet")
    print("2. Update Tweet")
    print("3. Read Tweets")
    print("4. Delete Tweet")
    print("5. Exit Twitter")

    cmd = input("Welcome back to Twitter, select a choice: ")
    if cmd == "1":
        print("Creating Tweet")
        tweet_text = input("Type in your tweet: ")
        username = input("What's your username: ")
        is_verified = bool(input("Are you a verified user, True/False: "))
        handler.create_tweet(tweet_text, username, is_verified)

    elif cmd == "2":
        print("Updating Tweet")
        tweet_id = input("What's your tweets id? If you don't know Read all Tweets and find your id: ")
        updated_tweet = input("Type your new tweet: ")
        handler.update_tweet(tweet_id, updated_tweet)

    elif cmd == "3":
        print("Reading Tweets")
        handler.read_all_tweets()

    elif cmd == "4":
        print("Delete Tweet")
        tweet_id = input("What's your tweets id? If you don't know Read all Tweets and find your id: ")
        handler.delete_tweet(tweet_id)

    elif cmd == "5":
        print("Leaving Twitter, Goodbye!")
        cmd = False

    elif cmd !="":
        print("Invalid selection, please try agian!")

