import argparse
from app.api import get_events
#import json
from pathlib import Path

file_path = Path("./app/data.json")

def main():
    parser = argparse.ArgumentParser(description="Github-User-Activity - fetch user activity and display it in the terminal")
    parser.add_argument("username", help="Provide GitHub username as an argument")
    args = parser.parse_args()

    user_data = get_events(args.username)
    print(f"{user_data}")

    '''
    if "error" in user_data:
        print(f"error: {user_data}")
    else:
        with open(file_path, "w") as f:
                json.dump(user_data, f, indent=4)
'''