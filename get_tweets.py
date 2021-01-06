#http://www.tweepy.org/
import sys
import tweepy
import smtplib
import ssl
# author: https://github.com/kagaya25/How-to-Send-Emails-Using-Python---Plain-Text
from plyer import notification 
#Twitter API credentials and enter them here
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#method to get a user's last tweets
def get_tweets(username):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	number_of_tweets = 1

	#get tweets
	tweets_for_csv = ""
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
		print(tweet.text)
		tweets_for_csv = tweet.text

	Sendmail(tweets_for_csv);
def Sendmail(tweets):

	smptp_server = 'smtp.gmail.com'
	port = 587      # for that server
	print("Mailing Starting ")
	sender = input("Enter your email: ")
	password = input("Enter your password: ")
	context = ssl.create_default_context()    # creates secure SSl context
	
	message = '''\
	Subject: New video for mrBeast


	subscribe to my channel and like
	www.youtube.com/kagayajohn?sub_confirmation=1

	 {}.
	'''.format(tweets)
	print("This is the " + tweets)
	receiver = input("Enter your Send to : ")
	try:
	    server = smtplib.SMTP(smptp_server, port)
	    server.ehlo()   # enable connecting to server
	    server.starttls(context=context)  # secures the connection
	    server.login(sender, password)
	    server.sendmail(sender, receiver, message)
	    print('Your mail is sent successfully.')
	except Exception as e:
	    sys.stderr.write("A problem occured: ")
	    sys.stderr.flush()
	    print(e)

	finally:
	    server.quit()
'''
Note:
You have to allow less secure apps on gmail, 
https://myaccount.google.com/lesssecureapps
'''


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        
        get_tweets(sys.argv[1])
    else:
        print ("Error: enter one username")
