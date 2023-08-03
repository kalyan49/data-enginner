import requests
#connect with fake rest api(search in internet for copying link
response=requests.get('https://jsonplaceholder.typicode.com/comments')
print(response)
if (response.status_code==200):
   print('connection success')
else:
   print('connection fail')
print(response.text)