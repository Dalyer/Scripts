# organize.py

import os
import eyed3

dirname = os.getcwd()

files = os.listdir()
songs = []
folderDir = []
#detect the file types
#sort into seasons for mp4/mkv files
#work with the stats of albums and such

for file in files:
	if file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.m4a'):
		songs.append(file)

# for song in mp3s:
# 	audiofile = eyed3.load(song)
# 	
audiofile = eyed3.load(songs[0])
audiofile.tag.album = u"Dear Agony"
audiofile.tag.save()
print(audiofile.tag.album)
