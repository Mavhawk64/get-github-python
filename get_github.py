import requests
import re
from datetime import datetime

#Obtain Username to be searched.
user = input("\n\nPlease insert GitHub Username (lowercase):\n")

#This is the URL to be scraped (JSON for ease)
url = 'https://api.github.com/users/' + user

#Using Requests Library, send a GET request, hopefully get <Reponse: 200>
data = requests.get(url)

#Find all (1) of the instances of '"public_repos":#' and return just the number.
repos = re.findall(r'(\"public_repos\":\d+)', data.text)[0].replace('\"public_repos\":','')

#Find User's name.
name = re.findall(r'(\"name\":\"\w+\s?\w+?\")', data.text)[0].replace('\"name\":', '').replace('\"','')
#Get the date and time of right when the program is ran.
today = datetime.now()

#Format the date and time to be DD Month, YYYY at HH:MM:SS
date = today.strftime("%d %B, %Y at %H:%M:%S")

#Print to screen.
print("\n%s has %s repositories posted to GitHub as of %s.\n\n" % (name, repos, date))