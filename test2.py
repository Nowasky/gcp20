import requests
r = requests.get('http://169.254.169.254')
print(r.content)
