import requests

for i in range(1,8):
	url = 'https://swapi.co/api/films/' + str(i) 

	r = requests.get(url)



	#print(r)

	dici = r.json()

	print(dici['title'])