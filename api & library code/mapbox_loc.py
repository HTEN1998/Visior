import mapbox 

gc = mapbox.Geocoder(access_token = "pk.eyJ1IjoibGxoYXJpc2hsbCIsImEiOiJjazQ4NDJiN3YwNDhyM25wcjNiYXE4amtiIn0.GnNhtTCRQktOCNmS4WI9LQ")

response = gc.forward("Chester ,NJ")

#file = open("locations.json","w+")
res = response.json()

#file.write(res)
#file.close()

print(res)