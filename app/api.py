import requests


def get_events(user_name: str) -> dict:
    
    '''Fetch recent activity of the specified GitHub user '''
    url = f"https://api.github.com/users/{user_name}/events"

    t_headers = {
        "Accept" : "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url, headers=t_headers)
    print("Status Code:", response.status_code)

    if response.ok:
        data = response.json()
        return data
    else:
        return  response.text