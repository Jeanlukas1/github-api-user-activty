import requests
import os

BASE_URL = "https://api.github.com"

TOKEN = os.getenv("GITHUB_TOKEN")

headers = {}
if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"


def get_commit_count(repo_name, before, head):
    url = f"{BASE_URL}/repos/{repo_name}/compare/{before}...{head}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    return data.get("total_commits")


def format_event(event):
    event_type = event.get("type")
    repo_name = event["repo"]["name"]

    if event_type == "PushEvent":
        payload = event["payload"]

        commits = payload.get("distinct_size")

        if not commits:
            before = payload.get("before")
            head = payload.get("head")

            if before and head:
                commits = get_commit_count(repo_name, before, head)

        if commits:
            return f"- Pushed {commits} commits to {repo_name}"
        else:
            return f"- Pushed commits to {repo_name}"

    elif event_type == "IssuesEvent":
        action = event["payload"].get("action")

        if action == "opened":
            return f"- Opened a new issue in {repo_name}"

    elif event_type == "WatchEvent":
        return f"- Starred {repo_name}"

    return None


def get_user_activity(username):
    url = f"{BASE_URL}/users/{username}/events"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erro: {response.status_code}")
        print(response.text)
        return

    events = response.json()

    count = 0
    for event in events:
        formatted = format_event(event)

        if formatted:
            print(formatted)
            count += 1

        if count == 5:
            break

user_name = "Jeanlukas1"
get_user_activity(user_name)