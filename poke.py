import requests

for i in range(1,152):
	url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
	r = requests.get(url)
	poke = r.json()
	if poke['name'][0] == 'm':
		print(poke['name'])
