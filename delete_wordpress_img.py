import requests
from requests.auth import HTTPBasicAuth

# Replace these with your WordPress credentials and URL
wordpress_url = "https://example.com" # Replace this with your WordPress URL
username = "your_username"  # Replace this with your WordPress username
password = "your wordpress Application Password"  # Replace this with your WordPress Application Password

# WordPress REST API endpoint for media
media_endpoint = f"{wordpress_url}/wp-json/wp/v2/media"

# Authenticate using HTTP Basic Authentication
auth = HTTPBasicAuth(username, password)

# Fetch all media items
def get_all_media():
    media = []
    page = 1

    while True:
        response = requests.get(f"{media_endpoint}?per_page=100&page={page}", auth=auth)
        if response.status_code != 200:
            print(f"Failed to fetch media. HTTP Status Code: {response.status_code}")
            break
        
        data = response.json()
        if not data:
            break

        media.extend(data)
        page += 1

    return media

# Delete media items
def delete_media(media_items):
    for item in media_items:
        media_id = item['id']
        if 'mime_type' in item and item['mime_type'].startswith('image/'):

            delete_url = f"{media_endpoint}/{media_id}?force=true"  # 'force=true' ensures permanent deletion
            
            response = requests.delete(delete_url, auth=auth)
            if response.status_code == 200:
                print(f"Deleted media ID: {media_id}")
            else:
                print(f"Failed to delete media ID: {media_id}. HTTP Status Code: {response.status_code}")

# Main logic
if __name__ == "__main__":
    print("Fetching all media items...")
    media_items = get_all_media()

    if media_items:
        print(f"Found {len(media_items)} media items. Deleting...")
        delete_media(media_items)
    else:
        print("No media items found.")


