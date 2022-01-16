import requests
import json

def main():
    request = requests.get("https://papermc.io/api/v2/projects/paper")
    versions = request.json()
    
    for v in versions["versions"]:
        print(v)

if __name__ == "__main__":
    main()
