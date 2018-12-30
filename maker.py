import os
import re

b = os.getcwd()
idx = 0
s = ""
with open(b+'/apmusic.txt','r') as f:
	for line in f:
		a = line.split('\t')
		#print(a)
		print(a[0],a[3])
		s+=a[3] + '---' + a[0] + "\n"

with open(b+"/songs.txt","w") as o:
	o.write(s)