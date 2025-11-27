import argparse

def main():
    parser = argparse.ArgumentParser(description="Github-User-Activity - fetch user activity and display it in the terminal")
    parser.add_argument(name= "username", help= "Provide GitHub username as an argument")
    args = parser.parse_args()