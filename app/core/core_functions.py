from app.core.api import get_events
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict


BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data.json"
file_path_txt = BASE_DIR / "activity.txt"

def init_struct():  #Initialize activity dict from existing json or create new dict instance

    if file_path.exists() :
            with open(file_path, "r") as f:
                activity_from_json = json.load(f)
                
                activity = defaultdict(lambda: defaultdict(lambda: {"id": set(), "repo": None}))

                for k, v in activity_from_json.items():
                    for a, b in v.items():
                        activity[k][a]["id"] = set(b["id"])
                        activity[k][a]["repo"] = b["repo"]

            return activity
                
    else:
        return defaultdict(lambda: defaultdict(lambda: { "id": set(), "repo": None }))



def process_events(username: str)  -> None: #Process api response data per required fields and save to json

    activity = init_struct()
    events = get_events(username)

    if events:
        
        for event in events:
            event_type = event.get("type")
            event_date = event.get("created_at")
            event_id = event.get("id")
            event_repo = event.get("repo")
            
            if not event_type or not event_date or not event_id:
                continue

            date = datetime.fromisoformat(event_date.replace("Z", "")).date()
            
            activity[str(date)][event_type.lower()]["id"].add(event_id)
            activity[str(date)][event_type.lower()]["repo"] = event_repo

            activity_to_json = { 
                                k: {
                                    a: { "id": list(b["id"]),"repo": b["repo"]}
                                    for a, b in v.items()
                                    }
                                for k, v in activity.items()
                                }

        with open(file_path, "w") as f:
            json.dump(activity_to_json, f, indent=4)
        
        return activity

    else:
        return print(f"Invalid_username: {username}")



def filter_events(event_type: str , username: str) -> None: # filter and display processed data 
     
     activity = process_events(username)
     
     for k,v in activity.items():
          for a,b in v.items():
            if event_type == "all":
                 print(f"{k} : ({len(b['id'])}) {a} in {b['repo']['name']}")
            else:
                 if a == event_type:
                      print(f"{k} : ({len(b['id'])}) {a} in {b['repo']['name']}")
            
