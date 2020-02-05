from mapbox import Directions,Geocoder
from geojson import Point
import mapbox


#help(Directions)
gc =Geocoder(access_token = "pk.eyJ1IjoibGxoYXJpc2hsbCIsImEiOiJjazQ4NDJiN3YwNDhyM25wcjNiYXE4amtiIn0.GnNhtTCRQktOCNmS4WI9LQ")
src = Point((19.191253, 72.976295))
des = Point((19.190995, 72.966744))

source = {
'type' : 'Feature' , 
'properties' : {'name' : 'Source'} , 
'geometry' : {
	 'type' : "Point",
	 'coordinates' : [19.191253, 72.976295]
}
}


destn = {
'type' : 'Feature' , 
'properties' : {'name' : 'Destnation'} , 
'geometry' : {
	 	 'type' : "Point",
	 'coordinates' : [19.190995, 72.966744]
}
}
print(source)
print(destn)
service = Directions() 
resp = service.directions([source,destn], "mapbox/driving")
print(resp.status_code)

directions_ = resp.geojson() 


print(f"done {directions_}")