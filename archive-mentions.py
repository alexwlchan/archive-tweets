#!/usr/bin/python

import tweepy
import pytz
import os

# Parameters.
me = 'username'
urlprefix = 'http://twitter.com/'
tweetdir = os.environ['HOME'] + '/Dropbox/twitter/'
tweetfile = tweetdir + 'mentions.txt'
idfile = tweetdir + 'lastID.txt'
datefmt = '%B %-d, %Y at %-I:%M %p'
homeTZ = pytz.timezone('US/Central')
utc = pytz.utc

def setup_api():
  """Authorize the use of the Twitter API."""
  a = {}
  with open(os.environ['HOME'] + '/.twitter-credentials') as credentials:
    for line in credentials:
      k, v = line.split(': ')
      a[k] = v.strip()
  auth = tweepy.OAuthHandler(a['consumerKey'], a['consumerSecret'])
  auth.set_access_token(a['token'], a['tokenSecret'])
  return tweepy.API(auth)

# Authorize.
api = setup_api()

# Get the ID of the last downloaded mention.
a = {}
with open(idfile, 'r') as f:
  for line in f:
	k, v = line.split(': ')
	a[k] = v.strip()
  lastID = a['mention']

# Collect all the mentions since the last one.
tweets = api.mentions(since_id=lastID)

# Write them out to the mentions.txt file.
with open(tweetfile, 'a') as f:
    for t in reversed(tweets):
      ts = utc.localize(t.created_at).astimezone(homeTZ)
      lines = ['',
               t.text,
               '',
               'at [' + ts.strftime(datefmt) + '](' + urlprefix + t.user.screen_name + '/status/' + t.id_str + ') by [@' + t.user.screen_name + '](' + urlprefix + t.user.screen_name + ')',
               '- - - - -',
               '']
      f.write('\n'.join(lines).encode('utf8'))
      lastID = t.id_str

# Update the ID of the last downloaded mention.
with open(idfile, 'r') as f:
  data = f.readlines()

print data
print "mention: " + data[0]

data[1] = 'mention: ' + lastID + '\n'

with open(idfile, 'w') as f:
  f.writelines ( data )
