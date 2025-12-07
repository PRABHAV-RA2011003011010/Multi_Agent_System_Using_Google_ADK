import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
REDIRECT_URI = os.getenv("LINKEDIN_REDIRECT_URI")
AUTH_CODE = os.getenv("LINKEDIN_AUTH_TOKEN")

url = "https://www.linkedin.com/oauth/v2/accessToken" 


data = { 

    "grant_type": "authorization_code", 

    "code": AUTH_CODE, 

    "redirect_uri": REDIRECT_URI, 

    "client_id": CLIENT_ID, 

    "client_secret": CLIENT_SECRET 

} 

 

response = requests.post(url, data=data) 

print(response.json()) 

 