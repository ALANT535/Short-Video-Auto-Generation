import requests

def get_long_lived_page_access_token(app_scoped_user_id, long_lived_user_access_token):
    url = f"https://graph.facebook.com/v21.0/{app_scoped_user_id}/accounts"
    params = {
        "access_token": long_lived_user_access_token
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        print(data)
        
        # Extract page information
        page_tokens = {
            page['id']: page['access_token'] for page in data.get('data', [])
        }
        
        if not page_tokens:
            print("No pages found or no access tokens retrieved.")
        
        return page_tokens
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching the long-lived Page Access Token:", e)
        return None