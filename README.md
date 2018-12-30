# APMigrater
Your guide for moving your music from Apple Music to Spotify (without the annoying Apple Music API)

*Disclaimer: this tutorial requires the use of a Mac computer. Without one, you'll have to find a way to copy your entire songlist into a text file. If you can do this without copy and paste, using this tutorial probably isn't worth your time anyway.*

## Directions

1. Download this repository onto your computer
2. Open Apple Music. Click one song, and use shift to select all songs in library (or all songs you want to move). Click command-C to copy them.
3. Open your favorite text editor in the directory where this repo is downloaded. This can be Sublime, Atom, etc. Just not vi. If you went to open vi, open the door to your bathroom instead, and please take a long look in the mirror.
4. Paste into your text editor, and save it as apmusic.txt. Overwrite if prompted.
5. In command line, run the command "python -V" to determine your python version. If the number starts with two, pull yourself from under the weight of your own misery and update your python to anything past version 3.
6. Use the command "python3 maker.py" to clean up your song titles. Your songs1.txt file should now only contain song and arist names, seperated by "---"
7. Create a spotify developer account. It's really easy. Just look up the phrase "Create a spotify developer account"
8. Create a new app on that account. Call it whatever you want, and say it's a desktop app
9. Once finished with set-up, click "edit settings". We only really care about the redirect URI. If you already have a redirect URI in mind, enter that here, and in adder.py at the redirect_url parameter. If not, just enter http://localhost:3000/ in the spotify settings. This is the default URI in adder.py and will work just fine. Save the changes [to both].
9. Copy your client_id and client_secret into your adder.py file on your computer into their respective variables (Command-F is your friend here)
9. Copy your spotify username into the username variable.
10. In your spotify, create or find the private playlist you want to add songs to.\* Copy and paste its name into the "playlist_name" variable in adder.py
11. In the URL of that playlist (you may have to use spotify in your browser for this), copy the string after the final slash. It should probably look something like *4TDOprH7yaCBiz81JGcxWI*. Paste it into the playlist_id variable in adder.py
12. In commandline, run "pip install spotipy". Troubleshoot as (hopefully not) needed
12. Command-F for the tilde (~) character in adder.py. None should remain now.
12. The current code will add your first 1000 songs. Edit the final lines as needed (in increments of 100--Spotify won't take more) to make it work for more songs.
13. Run adder.py with "python3 adder.py". THIS WON'T WORK YET - it's time for authentification!
14. On the web page that displays, hit agree.
15. The next page will look like an error. It probably isn't. Copy that entire URL and paste it into the prompt displayed on your command line (if you're not being prompted for a URL, something's gone wrong) and hit enter
16. Things should be running now. This may take a while. Double checking means that with the artist & song parameters given, no songs were found, so it's just checking with the song name. If no number is displayed before moving on to the next song, no song was found for that data. Its data will be stored in orphans.txt
17. That's it, folks! If you've got any errors, look 'em up, and if you can't figure them out, leave me a comment on here. Hopefully though, when you check your playlist (a refresh is sometimes necessary) it should have all of your songs minus the orphans. The orphan rate is only about 2% though, so they shouldn't be too bad to add manually. The mis-hit rate is <1%, these should be minimal as well.


Hope this helped!





\* If you're working with a public playlist, change the "playlist-modify-private" in adder.py to "playlist-modify-public"


