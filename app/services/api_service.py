import requests

BASE_URL = "https://api.github.com"
import requests

BASE_URL = "https://api.github.com"

def get_repos_info(owner: str):
    response = requests.get(f"{BASE_URL}/users/{owner}/events").json()

    push_events = [e for e in response if e.get("type") == "PushEvent"]

    for event in push_events:
        repo_name = event["repo"]["name"]
        commit_sha = event["payload"]["head"]

        commit_url = f"{BASE_URL}/repos/{repo_name}/commits/{commit_sha}"
        commit_data = requests.get(commit_url).json()

        commits_quantity = len(commit_data)
        
        print(f"- Pushed {commits_quantity} commits to {repo_name}")

user_name = "Jeanlukas1"
get_repos_info(user_name)
