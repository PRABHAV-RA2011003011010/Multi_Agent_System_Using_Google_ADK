import requests

ACCESS_TOKEN = "LINKEDIN_ACCESS_TOKEN"   # Do NOT hardcode in real apps

url = "https://api.linkedin.com/v2/shares/1234"
params = {
    "projection": "(id,owner)"
}

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0"
}

response = requests.get(url, headers=headers, params=params)

print("Status:", response.status_code)
print("Response:", response.json())
