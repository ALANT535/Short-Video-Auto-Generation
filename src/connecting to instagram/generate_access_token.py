import requests
from requests.auth import HTTPBasicAuth


# Call thIS function to get a new access token
def get_new_access_token(APP_KEY , APP_SECRET , REFRESH_TOKEN):
    url = "https://api.dropbox.com/oauth2/token"
    
    params = {
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN
    }

    auth = HTTPBasicAuth(APP_KEY, APP_SECRET)
    
    response = requests.post(url, data=params, auth=auth)

    # Got the new access token
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        print("New access token:", access_token)
        return access_token
    else:
        print("Failed to refresh token:", response.json())
        return None

# sample usage
# get_new_access_token(APP_KEY , APP_SECRET , REFRESH_TOKEN)