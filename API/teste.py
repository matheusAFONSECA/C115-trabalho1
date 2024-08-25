import requests

number = 2  # The number you want to send

data = {'escolha': number}
response = requests.post('http://localhost:5000/phase', json=data)

print(response.text)  # Print the response from the server
