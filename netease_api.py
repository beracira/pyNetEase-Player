from http import client
from pprint import pprint as print
from time import ctime
from urllib import parse, request
import base64
import hashlib
import json
import os
# import pyglet
import PyQt5

search_url = 'http://music.163.com/api/search/get'

#set cookie
cookie_opener = request.build_opener()
cookie_opener.addheaders.append(('Cookie', 'appver=2.7.0'))
cookie_opener.addheaders.append(('Referer', 'http://music.163.com'))
request.install_opener(cookie_opener)

def netease_hymn():
    return """
    player's Game Over,
    u can abandon.
    u get pissed,
    get pissed,
    Hallelujah my King!
    errr oh! fuck ohhh!!!!
    """

def encrypted_id(dfsId):
	# f = open("data1.out", "w")

	# byte1 = bytearray('3go8&$8*3*3h0k(2)2'.encode('ascii'))
	# byte2 = bytearray(id)
	# byte1_len = len(byte1)
	# for i in range(len(byte2)):
	# 	byte2[i] = byte2[i]^byte1[i%byte1_len]

	# byte2 = hashlib.md5(byte2).digest()
	# result = base64.b64encode(byte2).decode()
	# result = result.replace('/', '_')
	# result = result.replace('+', '-')

	# return result
	x = [ord(i[0]) for i in netease_hymn().split()]
	y = ''.join([chr(i - 61) if i > 96 else chr(i + 32) for i in x])
	byte1 = bytearray(y, encoding='ascii')
	byte2 = bytearray(str(dfsId), encoding='ascii')
	for i in range(len(byte2)):
	    byte2[i] ^= byte1[i % len(byte1)]
	m = hashlib.md5()
	m.update(byte2)
	result = base64.b64encode(m.digest()).decode('ascii')
	result = result.replace('/', '_')
	result = result.replace('+', '-')
	return result


def search_by_name(name):
	params = {
		's' : name,
		'type' : 100,
		'offset' : 0,
		'limit' : 10
	}
	params = parse.urlencode(params)
	params = params.encode('utf8')
	resp = request.urlopen(search_url, params).readall()

	data = json.loads(resp.decode())
	print(data)

	# print(params)


def search_by_songs(name):
	params = {
		's' : name,
		'type' : 1,
		'offset' : 0,
		'limit' : 10
	}
	params = parse.urlencode(params).encode('utf8')
	resp = request.urlopen(search_url, params).readall()

	data = json.loads(resp.decode())
	print(data)

def search(s, stype, offset = 0, limit = 10):
	'''
	s: target string
	stype: song(1), album(10), singer(100), playlist(1000), user(1002)
	limit: maximum return item
	'''
	params = {
		's' : s,
		'type' : stype,
		'offset' : offset,
		'limit' : limit
	}
	params = parse.urlencode(params).encode('utf8')
	resp = request.urlopen(search_url, params).readall()

	data = json.loads(resp.decode())

	if (data['code'] == 200):
		return data['result']
	else:
		return 'Search Failed!'


def get_song_url(sid, data):
	template = "http://m5.music.126.net/{0}/{1}.mp3"

	dfsid = ''

	try:
		dfsid = data['hMusic']['dfsId']
	except:
		try:
			dfsid = data['mMusic']['dfsId']
		except:
			return data['mp3Url']

	print (template.format(encrypted_id(str(dfsid).encode("utf8")), dfsid))
	return template.format(encrypted_id(str(dfsid).encode("utf8")), dfsid)



def download(sid, button, path = "Downloads\\"):
	try:
		os.mkdir(path)
	except:
		pass

	print (sid)
	button.setText("Downloading")

	detail_url = r"http://music.163.com/api/song/detail/?id={0}&ids=['{0}']".format(sid)
	resp = request.urlopen(detail_url).readall()
	data = json.loads(resp.decode())['songs'][0]
	# print (data)

	name = data['name']
	artist = data['artists'][0]['name']
	# print ("Start downloading: " + name)

	if (not os.path.isfile(path + name + " " + artist + '.mp3')):
		mp3_url = get_song_url(sid, data)

		data = request.urlopen(mp3_url).readall()

		f = open(path + name + " " + artist + '.mp3', "wb")
		f.write(data)
		f.close()

	button.setText("Finished!")

	# print ("Downloaded successfully!")
	# print (f)
	# os.startfile(name + '.mp3')
	# sound = pyglet.media.load(name + '.mp3', streaming=True)
	# sound.play()
	# pyglet.app.run()
	return name + '.mp3'
	# 	except:
	# 		print ("File could not be written.")
	# except:
	# 	print ("Cannot connect.")
	# return False

def download_by_album(aid, button):
	album_url =  "http://music.163.com/api/album/{0}/".format(aid)

	resp = request.urlopen(album_url).readall()
	data = json.loads(resp.decode())['album']

	# time = ctime(data['publishTime'] / 1000)[-4:0]
	artist = data['artist']['name']
	name = data['name']
	path = "Downloads\\" + name + " " + artist + " " + "\\"


	try:
		os.mkdir(path)
	except:
		pass

	# print ("Cover downloading...")

	# button text
	length = len(data['songs'])
	button.setText("%d/%d".format(0, length))

	pic = request.urlopen(data['picUrl']).readall()
	f = open(path + "cover.jpg", "wb")
	f.write(pic)
	f.close()

	length = len(data['songs'])
	button.setText("%d / %d".format(0, length))
	for (song, i) in zip(data['songs'], range(length)):
		download(song['id'], path)
		button.setText("%d/%d".format(i + 1, length))


	# print ("Album downloaded!")



print (search_by_songs("two of us"))
# print (search("The Beatles Bootleg Recordings 1963".encode("utf8"), 10))
# resp = request.urlopen(r"http://music.163.com/api/album/2956076/").readall()
# data = json.loads(resp.decode())
# print (data)



# print(encrypted_id(209079))

# music_url = 'http://m1.music.126.net/\
# {0}/{1}.mp3'.format(encrypted_id("1070924325466615".encode()), 1070924325466615)

# print (music_url)

# resp = request.urlopen(r"http://music.163.com/api/song/detail/?id=28949444&ids=['28949444']").readall()
# resp = request.urlopen(r"http://music.163.com/api/artist/178059/").readall()
# # resp = request.urlopen(r"http://music.163.com/api/playlist/detail?id=76494274").readall()
# data = json.loads(resp.decode())
# print (data)

# download_by_album(2956076)

