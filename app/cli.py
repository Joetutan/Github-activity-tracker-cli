import argparse
from app.core_functions import process_events, filter_events


def main():
    parser = argparse.ArgumentParser(description="Github-User-Activity - fetch user activity and display it in the terminal")
    
    parser.add_argument("username", help="Provide GitHub username as an argument")

    parser.add_argument("event_type",nargs="?",default="all",help="optional event type filter")
    
    
    args = parser.parse_args()
    
    process_events(args.username)
    filter_events(args.event_type)

    

    
