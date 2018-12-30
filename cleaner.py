import os
import re

b = os.getcwd()
idx = 0
s = ""
with open(b+'/songs.txt','r') as f:
	for line in f:
		a = line
		a = a.replace("\"","")
		a = a.replace(",","")
		try:
			sp = a.index("(")
			if sp > 13:
				a = a[0:sp]+"\n"
		except ValueError:
			pass
		print(a)
		s+=a
with open(b+"/songs1.txt","w") as o:
	o.write(s)


