

import requests

response = requests.get("https://api.github.com/users/octocat")
if response.status_code == 200:
    user = response.json()
    print(f"Name: {user['name']}")
    print(f"Public Repos: {user['public_repos']}")
else:
    print("API request failed.")
