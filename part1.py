# Name: Yezhi Deng 
# Uniq: yezdeng
# UMID 43578445


	# these should be the only imports you need
import tweepy
from tweepy import OAuthHandler
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('popular')

import json
import sys


### Tweeter keys, use api to access data
consumer_key = 'utSnTpb2rERC2P0C9dxlia6oi'
consumer_secret = 'DagJOkhlV7I3iUeYcyoSeWTvIEKk4l1YSTIcWFTauPuLStapiZ'
access_token = '965302032432279559-rMzHul8T6iwYJAANkB2JIlUGbyYfGMk'
access_secret = 'mxAnL0GC9KSRRDZDyoioqj7toFpsOsWsRmabJB5sfVeqZ'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
###



def tweetAnalysis(username, num_tweets):

	#  1. username & num_tweets 
	print("USER: " + username)
	print("TWEETS ANALYZED: " + str(num_tweets))

	#  2. store words accessed in a string
	tweet_text = ''
	status_lst = []
	for status in tweepy.Cursor(api.user_timeline, screen_name = username).items(num_tweets):
		tweet_text += status.text
		status_lst.append(status._json)

	#  3. delete stop words
	tokens = nltk.word_tokenize(tweet_text)
	tweet_text_clean = []
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	for word in tokens:
		if(word[0].upper() in letters and word != 'https' and word != 'http' and word != 'RT'):
			tweet_text_clean.append(word)

	#  4. Use nltk package to split and tag words
	tokens_tagged = nltk.tag.pos_tag(tweet_text_clean)
	# print(tokens_tagged)

###
###
	#  5. Select nouns
	noun_lst = []
	for token in tokens_tagged:
		if(token[1] == 'NN'):
			noun_lst.append(token[0])	
	# print(noun_lst)

	#  6. Find top 5 most frequent nouns
	### put nouns and frequency into a dic
	noun_dic = {}
	for noun in noun_lst:
		if noun.lower() not in noun_dic:
			noun_dic[noun.lower()] = 1
		else:
			noun_dic[noun.lower()] += 1

	# print(noun_dic)


	# create a .csv file to save nouns
	f = open('noun_data.csv','w')
	f.write("Noun, Number\n")

	### Put nouns into a list 
	noun_lst_norepeat = []
	for noun in noun_dic:
		noun_lst_norepeat.append(noun)

	### sort noun_sort
	noun_sort = sorted(noun_lst_norepeat, reverse = True, key = lambda x : noun_dic[x])
	# print(noun_sort)
	print("The 5 most frequent nouns are: ")
	i = 0
	while (i < 5):
		print(noun_sort[i] + "(" + str(noun_dic[noun_sort[i]]) + ")")
		# wirte the output into .csv file
		f.write("{},{}\n".format(noun_sort[i], noun_dic[noun_sort[i]]))
		i += 1

	f.close()
###
###

	# 5. Select verbs
	verb_lst = []
	for token in tokens_tagged:
		if(token[1] == 'VB'):
			verb_lst.append(token[0])	
	# print(verb_lst)

	#  6. Find top 5 most frequent verbs
	### put verbs and frequency into a dic
	verb_dic = {}
	for verb in verb_lst:
		if verb.lower() not in verb_dic:
			verb_dic[verb.lower()] = 1
		else:
			verb_dic[verb.lower()] += 1

	# print(verb_dic)

	### Put verbs into a list 
	verb_lst_norepeat = []
	for verb in verb_dic:
		verb_lst_norepeat.append(verb)

	### sort noun_sort
	verb_sort = sorted(verb_lst_norepeat, reverse = True, key = lambda x : verb_dic[x])
	# print(noun_sort)
	print("The 5 most frequent verbs are: ")
	i = 0
	while (i < 5):
		print(verb_sort[i] + "(" + str(verb_dic[verb_sort[i]]) + ")")
		i += 1	 
###
###
	# 5. Select adjs
	adj_lst = []
	for token in tokens_tagged:
		if(token[1] == 'JJ'):
			adj_lst.append(token[0])	
	# print(adj_lst)

	#  6. Find top 5 most frequent adjs
	### put adjs and frequency into a dic
	adj_dic = {}
	for adj in adj_lst:
		if adj.lower() not in adj_dic:
			adj_dic[adj.lower()] = 1
		else:
			adj_dic[adj.lower()] += 1

	# print(verb_dic)

	### Put verbs into a list 
	adj_lst_norepeat = []
	for adj in adj_dic:
		adj_lst_norepeat.append(adj)

	### sort noun_sort
	adj_sort = sorted(adj_lst_norepeat, reverse = True, key = lambda x : adj_dic[x])
	# print(noun_sort)
	print("The 5 most frequent adjs are: ")
	i = 0
	while (i < 5):
		print(adj_sort[i] + "(" + str(adj_dic[adj_sort[i]]) + ")")
		i += 1	 
###
###

	num_retweets = 0
	num_favorited_tweets = 0
	num_retweeted_tweets = 0

	for status in status_lst:
		### if it is a retweeted tweet
		if ('retweeted_status' in status):
			num_retweets += 1

		else: 
			### retweeted times (by others)
			if (status['retweet_count'] > 0): 
				num_retweeted_tweets += 1

			### favorited times (by others)?
			if (status['favorite_count'] >0): 
				num_favorited_tweets += 1


	original_tweets = num_tweets - num_retweets
	print("ORIGINAL TWEETS: " + str(original_tweets))
	print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): " + str(num_favorited_tweets))
	print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): " + str(num_retweeted_tweets))




username = sys.argv[1]
item_num = int(sys.argv[2])

###
### Call the function
tweetAnalysis(username, int(item_num))
