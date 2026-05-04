import requests

url = input("Enter website URL: ")

try:
    r = requests.get(url, timeout=5)
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        print("Website is UP ✅")
    else:
        print("Website might have issues ⚠️")
except Exception as e:
    print("Error:", e)
