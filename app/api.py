import requests


def get_events(user_name: str) -> dict:
    
    # Fetch recent activity of the parsed username GitHub account 
    url = f"https://api.github.com/users/{user_name}/events/public"

    # Header requesting github api json format specifying version
    t_headers = {
        "Accept" : "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    # Assign response 
    response = requests.get(url, headers=t_headers)

    if response.ok:
        data = response.json()
        return data
    else:
        return  response.text


