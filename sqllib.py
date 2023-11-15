import requests
url = 'http://192.168.1.150:1880/Update-Card'
myobj = {'somekey':'somevalue'}

x = requests.post(url,json=myobj)

print(x.text)