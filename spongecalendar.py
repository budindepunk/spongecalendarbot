import tweepy
import gspread
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()

client = tweepy.Client(
    consumer_key= os.environ['api_key'],
    consumer_secret= os.environ["api_secret"],
    access_token= os.environ["access_token"],
    access_token_secret= os.environ["access_token_secret"]
)
auth = tweepy.OAuth1UserHandler(
    consumer_key= os.environ["api_key"],
    consumer_secret= os.environ["api_secret"],
    access_token= os.environ["access_token"],
    access_token_secret= os.environ["access_token_secret"]
)
api = tweepy.API(auth)

# esto lo voy a precisar cuando exista tuitear imagenes
""" gc = gspread.service_account("credentials.json")
wks = gc.open("spongecalendar").sheet1

tweet = wks.acell('A1').value

client.create_tweet(text = tweet)
wks.delete_rows(1) """


#mientras 
arte_bob = "▕▔▔▔▔▔▔▔▔▔▔▔╲┈┈┈\n▕╮╭┻┻╮╭┻┻╮╭▕╮╲┈┈\n▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏┈\n▕╭┻┻┻┛┗┻┻┛┈▕┈╰▏┈\n▕╰━━━┓┈┈┈╭╮▕╭╮▏┈\n▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏┈\n▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏┈"
today = date.today()
fecha = today.strftime("%B %d, %Y")

tweet = "🟨 📅 🟨 " + fecha + " 🟨 📅 🟨" + "\n" + arte_bob
client.create_tweet(text = tweet)
