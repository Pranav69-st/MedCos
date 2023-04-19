import requests

url = 'http://localhost:5000/predict'
data = {
    'Experience': 1.8,
    'Locality': 'Koramangala',
    'City': 'Bangalore',
    'Profile': 'Dentist',
    'Qualification': 'BDS'
}

r = requests.post(url, json=data)
print(r.json())
