"""
Tracy Tran
9/28/2015

This script takes a CSV file with Twitter user IDs & returns a CSV with the actual usernames in another column. 

"""

from twython import Twython
import csv

# My Twitter credentials.Please replace with your own at apps.twitter.com.
APP_KEY = "C0mughtR15ab8e06qGQbVjmLF"
APP_SECRET = "GOgphYsPfh3jR4JYLH6s0GPrq0wdzQr1IpwSKqidnqXxh1Fd7W"
OAUTH_TOKEN = "227459435-IHYybp0wrxGKV8WrgYyECFJ9osyx1dgvNttR2ilc"
OAUTH_TOKEN_SECRET = "fy5ezX1A3uRESUKnsjFniZQgWKxfoqySBlJJkwdBaBmLw"

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

user_id_list = []
usernames_list = []

# Opening the CSV
f = open('affluentwomen4.csv')
csv_f = csv.reader(f)

for row in csv_f:
	user_id_list.append(row)

	try: 
		name = twitter.lookup_user(user_id=row,timeout = 60)[0]['screen_name']
		usernames_list.append(name)

	except Exception:
		name = "Not available"
		usernames_list.append(name)

	else:
		continue

zipped = zip(user_id_list, usernames_list)

f.close()

# Creates a new CSV
with open('updated_affluent_women4.csv', 'wb') as newfile:
	writer = csv.writer(newfile)
	writer.writerows(zipped)

newfile.close()

print("WOO WOO WOOO")
