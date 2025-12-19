from app.api import get_events
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

file_path = Path("./data.json")


#Initialize activity dict from existing json or create new dict instance
if file_path.exists() :
        with open(file_path, "r") as f:
            activity_from_json = json.load(f)
            activity = {k: { a: set(b) for a,b in v.items()} for k,v in activity_from_json.items()}
            
else:
        activity = defaultdict(lambda: defaultdict(set))

#Process api response data per required fields and save to json

def process_events(username: str)  -> None:

    events = get_events(username)

    if events:
        
        for event in events:
            event_type = event.get("type")
            event_date = event.get("created_at")
            event_id = event.get("id")
            
            if not event_type or not event_date or not event_id:
                continue

            date = datetime.fromisoformat(event_date.replace("Z", "")).date()
            
            activity[str(date)][event_type.lower()].add(event_id)

        activity_to_json = {k: { a: list(b) for a,b in v.items()} for k,v in activity.items()}


        with open(file_path, "w") as f:
            json.dump(activity_to_json, f, indent=4)

    else:
        print(f"Invalid_username: {username}")

# filter and display processed data 

def filter_events(event_type: str) -> None:
     
     for k,v in activity.items():
          for a,b in v.items():
            if event_type == "all":
                 print(f"{k} : ({len(b)}) {a}")
            else:
                 if a == event_type:
                      print(f"{k} : ({len(b)}) {a}")
            
