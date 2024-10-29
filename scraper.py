import requests
import csv
import os

# Set up API constants
GITHUB_API_URL = "https://api.github.com"
HEADERS = {"Authorization": "Bearer YOUR_GITHUB_TOKEN"}  # Replace with your GitHub token

# Define output CSV filenames
USERS_CSV = "users.csv"
REPOS_CSV = "repositories.csv"

# Step 1: Fetch users based in Sydney with over 100 followers
def fetch_users(location="Sydney", min_followers=100):
    url = f"{GITHUB_API_URL}/search/users?q=location:{location}+followers:>{min_followers}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  # Ensure we handle errors
    return response.json().get("items", [])

# Step 2: Fetch repositories for each user
def fetch_repositories(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

# Step 3: Write data to CSV
def write_users_csv(users):
    with open(USERS_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["login", "id", "node_id", "avatar_url", "gravatar_id", "url", "html_url", "followers_url", "following_url", "gists_url", "starred_url", "subscriptions_url", "organizations_url", "repos_url", "events_url", "received_events_url", "type", "site_admin", "score"])
        for user in users:
            writer.writerow([
                user.get("login", ""),
                user.get("id", ""),
                user.get("node_id", ""),
                user.get("avatar_url", ""),
                user.get("gravatar_id", ""),
                user.get("url", ""),
                user.get("html_url", ""),
                user.get("followers_url", ""),
                user.get("following_url", ""),
                user.get("gists_url", ""),
                user.get("starred_url", ""),
                user.get("subscriptions_url", ""),
                user.get("organizations_url", ""),
                user.get("repos_url", ""),
                user.get("events_url", ""),
                user.get("received_events_url", ""),
                user.get("type", ""),
                str(user.get("site_admin", "")).lower(),
                user.get("score", ""),
            ])

def write_repositories_csv(repositories):
    with open(REPOS_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "node_id", "name", "full_name", "private", "owner_login", "html_url", "description", "fork", "url", "created_at", "updated_at", "pushed_at", "homepage", "size", "stargazers_count", "watchers_count", "language", "forks_count", "open_issues_count", "license", "forks", "open_issues", "watchers", "default_branch"])
        for repo in repositories:
            writer.writerow([
                repo.get("id", ""),
                repo.get("node_id", ""),
                repo.get("name", ""),
                repo.get("full_name", ""),
                str(repo.get("private", "")).lower(),
                repo.get("owner", {}).get("login", ""),
                repo.get("html_url", ""),
                repo.get("description", ""),
                str(repo.get("fork", "")).lower(),
                repo.get("url", ""),
                repo.get("created_at", ""),
                repo.get("updated_at", ""),
                repo.get("pushed_at", ""),
                repo.get("homepage", ""),
                repo.get("size", ""),
                repo.get("stargazers_count", ""),
                repo.get("watchers_count", ""),
                repo.get("language", ""),
                repo.get("forks_count", ""),
                repo.get("open_issues_count", ""),
                repo.get("license", {}).get("name", "") if repo.get("license") else "",
                repo.get("forks", ""),
                repo.get("open_issues", ""),
                repo.get("watchers", ""),
                repo.get("default_branch", ""),
            ])

# Main function to run the script
def main():
    users = fetch_users()
    write_users_csv(users)
    all_repositories = []
    for user in users:
        repos = fetch_repositories(user["login"])
        all_repositories.extend(repos)
    write_repositories_csv(all_repositories)

if __name__ == "__main__":
    main()

