import requests

A = (requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBg33f-iEoZaA1wEVVqKiPquhdWacg3Dh0'))

print(A.json())