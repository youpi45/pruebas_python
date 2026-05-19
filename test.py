import requests

r = requests.get("https://httpbin.org/get")

print ("codigo de estado:", r.status_code)

