import argparse
from app.api import get_events
import json
from pathlib import Path
from datetime import datetime

file_path = Path("./data.json")

if file_path.exists() :
    with open(file_path, "r") as f:
        activity = json.load(f)
else:
    activity = {}


def main():
    parser = argparse.ArgumentParser(description="Github-User-Activity - fetch user activity and display it in the terminal")
    parser.add_argument("username", help="Provide GitHub username as an argument")
    args = parser.parse_args()

    events = get_events(args.username)
    
    if events:
        
        for event in events:
            event_type = event.get("type")
            event_date = event.get("created_at")
            
            if not event_type or not event_date:
                continue

            date = datetime.fromisoformat(event_date.replace("Z", "")).date()
            
            if str(date) not in activity :
                activity[str(date)] = {}
            
            if event_type not in activity[str(date)]:
                activity[str(date)][event_type] = 1
            else:
                activity[str(date)][event_type] += 1

            with open(file_path, "w") as f:
                json.dump(activity, f, indent=4)
    else:
        print(f"Invalid_username: {args.username}")
  
 
        
