# rename.py
# This script uses to mp3-tagger to fix the meta data on mp3 files that
# cause mp3 players to wrongly categorize albums

# REQUIREMENTS:
# Install mp3-tagger at:

# INSTRUCTIONS:
# Put this file in the same directory as the songs
# Make sure that songs are in an album directory that is in an artist directory
# run the script


import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

dirname = os.getcwd()
files = os.listdir(dirname)

dir_list = dirname.split('\\')
album_name = dir_list[-1]
artist_name = dir_list[-2]

songs = []
for file in files:
	if file.endswith('.mp3'):
		songs.append(file)

print("Working..")

for song_path in songs:
	audio_file = MP3File(song_path)
	audio_file.set_version(VERSION_BOTH)
	audio_file.album = album_name
	audio_file.artist = artist_name
	audio_file.band = artist_name
	audio_file.save()

print("Done")
