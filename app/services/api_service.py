import requests

BASE_URL = "https://api.github.com"

def get_last_commit(owner: str):
    response = requests.get(f"{BASE_URL}/users/{owner}/events").json()

    push_events = [e for e in response if e.get("type") == "PushEvent"]

    if not push_events:
        print("Nenhum push encontrado")
        return

    event = push_events[0]  # último push

    repo_name = event["repo"]["name"]
    before = event["payload"]["before"]
    head = event["payload"]["head"]

    compare_url = f"{BASE_URL}/repos/{repo_name}/compare/{before}...{head}"
    compare_data = requests.get(compare_url).json()

    commits_quantity = compare_data.get("total_commits", 0)

    print(f"- Pushed {commits_quantity} commits to {repo_name}")


user_name = "Jeanlukas1"
get_last_commit(user_name)