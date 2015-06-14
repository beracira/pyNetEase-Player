from netease_api import search
from pprint import pprint
import netease_api
import os
import sys

welcome = """Hello! This is a open-source third party NetEase Music player!"""

print (welcome)

while(True):
	print("What are you going to do..?")
	print("1. Search for songs")
	print("2. Search for album")
	print("3. Listen to author's playlist")
	print("4. Exit")
	opt = input()
	if (opt == '1'):
		name = input("Enter name of your song: ")
		result = search(name.encode('utf8'), stype = 1)['songs']
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
			netease_api.download(song_id)

	if (opt == '2'):
		name = input("Enter name of your album: ")
		result = search(name.encode('utf8'), stype = 10)['albums']
		if (result == 'Search Failed!'):
			print (result + 'Are you connected to the Internet?')
		else:
			temp = []
			print ("   {:<24} {:<24} {:>6}".format("Name","Artists","Size"))
			for (album, i) in zip(result, range(0, 10)):
				album = {
					'name': album['name'],
					'artist': album['artist']['name'],
					'size': album['size'],
					'id': album['id']}
				print (str(i) + ". {name:<24} {artist:<24} {size:>6}".format(**album))
				temp += [album]
			album_id = temp[int(input("Enter your choice: "))]['id']
			netease_api.download_by_album(album_id)

	if (opt == '3'):
		pass

	if (opt == '4'):
		sys.exit(0)
				

