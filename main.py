import netease_api
from netease_api import search
from pprint import pprint
import os

welcome = """Hello! This is a open-source third party NetEase Music player!"""


while(True):
	print("What are you going to do..?")
	print("1. Search for songs")
	print("2. Listen to author's playlist")
	opt = input()
	if (opt == '1'):
		name = input("Enter name of your song: ")
		result = search(name.encode('utf8'), stype = 1)
		if (result == 'Search Failed!'):
			print (result + 'Are you connected to the Internet?')
		else:
			temp = []
			print ("   {:<18} {:<18} {:<18}".format("Name","Album","Artists"))
			for song, i in zip(result, range(0, 10)):
				song = {
					'name': song['name'],
					'album': song['album']['name'],
					'artists': song['artists'][0]['name'],
					'duration': song['duration'],
					'id': song['id']}
				# song_temp = 
				print (str(i) + ". {name:<18} {album:<18} {artists:<18}".format(**song))
				# print ("{name}\t\t{album}\t\t{artists}".format(**song))
				temp += [song]
			song_id = temp[int(input("Enter your choice: "))]['id']
			play_result = netease_api.play(song_id)
			if play_result:
				os.startfile(play_result)
