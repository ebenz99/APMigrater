import sys
import spotipy
import spotipy.util as util
import os

p = os.getcwd()

scope = 'playlist-modify-private'

username = '~'

token = util.prompt_for_user_token(username,scope,client_id='~',client_secret='~',redirect_uri='http://localhost:3000/')

songs = []
notDone = []

if token:
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	with open(p+"/songs1.txt","r") as infile:
		counter = 0
		for line in infile:
			if counter == 0:
				playlist_name = "~"
				counter+=1
				continue
			else:
				l = line.split("---")
				try:
					artistName = l[0]
					trackName = l[1]
				except IndexError:
					print(l)
					continue
				q = "artist:"+artistName+" track:"+trackName
				print(q)
				res = sp.search(q, type="track", limit=5)
				try:
					a = (res['tracks']['items'][0])
					print(counter)
					counter+=1
					songs.append(a['uri'])
				except IndexError:
					print("DOUBLE CHECKING")
					q = "track:"+trackName
					res = sp.search(q, type="track", limit=5)
					try:
						a = (res['tracks']['items'][0])
						print(counter)
						counter+=1
						songs.append(a['uri'])
					except IndexError:
						notDone.append(q)

	with open('tracks.txt','w') as of:
		for s in songs:
			of.write(s+"\n")
	with open('orphans.txt','w') as ef:
		for s in notDone:
			ef.write(s)
	print(songs)
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[0:100])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[100:200])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[200:300])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[300:400])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[500:600])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[600:700])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[700:800])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[800:900])
	sp.user_playlist_add_tracks(username, playlist_id="4TDOprH7yaCBiz81JGcxWI", tracks=songs[900:1000])




				


