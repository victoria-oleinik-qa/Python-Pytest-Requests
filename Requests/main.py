import requests

response=requests.get('https://petstore.swagger.io/v2/pet/3')
print(response.text)

response=requests.post('https://petstore.swagger.io/v2/pet', json={
  "id": 666,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Max",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response=requests.put('https://petstore.swagger.io/v2/pet',json={
  "id": 666,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "ivi",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print(response.text)
