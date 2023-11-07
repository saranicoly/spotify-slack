import requests

endpoint = "https://slack.com/api/users.profile.set"

new_status = {
    "profile": {
        "status_text": "Teste",
        "status_emoji": ":heart:",
        "status_expiration": 0
    }
}
headers = {f"Authorization": "Bearer your_user_token"}
headers["Content-Type"] = "application/json; charset=utf-8"
print(requests.post(endpoint, json=new_status, headers=headers).json())