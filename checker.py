import requests
url = input(str("What's the site url?: "))
r = requests.get(url)

if r.status_code == 200:
	print( "Site is alive." )
else:
	print( "Site isnt' alive" )
