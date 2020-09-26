import requests

res = requests.get('https://www.teamonepanama.com')


# Make a request to 
# Store the result in 'res' variable
txt = res.text
status = res.status_code
# print the result
print(txt)
print(status)