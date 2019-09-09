# rename.py
# This script uses mp3-tagger to fix the meta data on mp3 files that
# cause mp3 players to wrongly categorize albums

# REQUIREMENTS:

# INSTRUCTIONS:
# Put this file in the same directory as the shows
# Make sure that songs are in an album directory that is in an artist directory
# run the script


import os

dirname = os.getcwd()
files = os.listdir(dirname)
suffix = ""
episodes = []

for file in files:
    if file.endswith('.mp4'):
        episodes.append(file)
        suffix = '.mp4'
    if file.endswith('.mkv'):
        episodes.append(file)
        suffix = '.mkv'

print("Working..")

for episode in episodes:
    src = dirname + "/" + episode
    proper_title = ""
    episode = episode.split('.')
    for i in episode:
        if i == 'Futurama':
            pass
        elif i == '720p' or i == '1080p':
            proper_title += i
            break
        else:
            proper_title += i + " "
    proper_title += suffix
    dst = dirname + "/" + proper_title
    os.rename(src, dst)

print("Done")
