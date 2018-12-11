""""
This script is responsible to pull shit from Slack. 
Usage: python slackapi.py <token>
"""

import sys, requests

slack_token = sys.argv[1]


def getUsers():
	jsonUsers = requests.get('https://slack.com/api/users.list?token={0}'.format(slack_token)).json()
	return jsonUsers

def getChannels():
	jsonChannels = requests.get('https://slack.com/api/channels.list?token={0}'.format(slack_token)).json()
	return jsonChannels

def getTeamInfo():
	jsonTeamInfo = requests.get('https://slack.com/api/team.info?token={0}'.format(slack_token)).json()
	return jsonTeamInfo

def getGeneralMessage(id):
	jsonMessages = requests.get('https://slack.com/api/channels.history?token={0}&channel={1}'.format(slack_token, id)).json()
	return jsonMessages

def main():
	print('Slack query script running')
	print('--------------------------\n')
	print('Team info')
	teamInfo = getTeamInfo()
	print('* Team name: {0}'.format(teamInfo['team']['domain']))
	print('* Team ID: {0}'.format(teamInfo['team']['id']))
	print('\nUsers:')
	print('---------')
	users = getUsers()
	for user in users['members']:
		userInf = 'Name: {0}'.format(user['profile']['real_name'].encode('utf-8'))
		try:
			userInf += ' Email: {0}'.format(user['profile']['email'].encode('utf-8'))
			print(userInf)
		except:
			print(userInf)
	print('\nChannels:')
	print('-----------')
	generalChannelId = ""
	channels = getChannels()
	for channel in channels['channels']:
		print('\n* Name: {0}, ID: {1}'.format(channel['name'].encode('utf-8'), channel['id'].encode('utf-8')))
		print('---------------------------------------------------------')
		
		"""
		uncomment the next three lines for super-sayan mode (get message from every channel that it can access)
		"""
		#getMessage = getGeneralMessage(channel['id'])
		#for message in getMessage['messages']:
		#	print('* {0}'.format(message['text'].encode('utf-8')))

		"""
		uncomment the next lines if you want message just for general channel
		"""
#		if channel['name'] == "general":
#			generalChannelId = channel['id']

#	print('\nMessage in General channel')
#	print('----------------------------')
#	messages = getGeneralMessage(generalChannelId)
#	for message in messages['messages']:
#		print('* {0}'.format(message['text'].encode('utf-8')))
main()
