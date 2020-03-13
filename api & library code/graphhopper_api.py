import requests
from pprint import pprint

# current co-ordinates
cx=19.185206
cy=72.975723
# goal co-ordinates
gx=19.179911
gy=72.980190
r = requests.get("https://graphhopper.com/api/1/route?point="+str(cx)+","+str(cy)+"&point="+str(gx)+","+str(gy)+"&vehicle=foot&locale=en&calc_points=true&key=apikey")
pprint(r.json())
data = r.json()

direction = []
length = len(data['paths'][0]['instructions'])
print("length= ",length)

for i in range(0,length):
	direction.append(data['paths'][0]['instructions'][i]['sign'])

print(direction)
