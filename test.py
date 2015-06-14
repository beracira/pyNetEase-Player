import pyglet
from http import client
from pprint import pprint as print
from urllib import parse, request
import base64
import hashlib
import json
import os

mp3url = "http://m1.music.126.net/fMlgcT4mKUWxEzfsTZ-CNA==/5861496487693804.mp3"

data = request.urlopen(mp3url)

sound = pyglet.media.load(data.readall(), streaming=True)
sound.play()
pyglet.app.run()