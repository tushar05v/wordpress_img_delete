# Delete WordPress Media using REST API

This repository contains a Python script to delete all image files from a WordPress account using the WordPress REST API. The script fetches all media items and deletes the ones with a MIME type starting with `image/`.

---

## Prerequisites

To use this script, ensure you have:

1. **Python Installed**: Version 3.6 or above.
2. **Application Password**: Set up an application password for your WordPress account.
3. **Requests Library**: Install it using:
   ```bash
   pip install requests
   ```

---

## How It Works

1. **Authentication**: The script uses HTTP Basic Authentication with your WordPress username and application password.
2. **Fetch Media**: Fetches all media items using the WordPress REST API.
3. **Delete Media**: Deletes items with a MIME type starting with `image/` permanently.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```

---

## Usage

1. Open the script and replace the placeholder values:

   - `wordpress_url`: Your WordPress site URL.
   - `username`: Your WordPress username.
   - `password`: Your WordPress application password.

2. Run the script:

   ```bash
   python delete_wordpress_media.py
   ```

---

## Code Example

Here’s the main logic of the script:

```python
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
```

---

## Notes

- **Force Deletion**: The `force=true` parameter ensures that the items are permanently deleted.
- **Pagination**: The script handles pagination to fetch more than 100 media items if necessary.
- **Error Handling**: The script prints error messages if the API fails.

---

## Disclaimer

Use this script carefully. Deleting media files is a permanent action and cannot be undone. Ensure you have a backup of your media files if necessary.

