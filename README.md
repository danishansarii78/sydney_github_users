# sydney_github_users
Github users in syndey with over 100 followers and their repositories
# GitHub Users and Repositories in Sydney

## Project Overview
This project collects GitHub users based in Sydney with over 100 followers and their repositories, using the GitHub API.

## Files in the Repository
- **users.csv**: Contains information about each user from Sydney with over 100 followers.
- **repositories.csv**: Contains data about each repository owned by the users.
- **scraper.py**: Code used to retrieve and save data from the GitHub API.

## Setup and Usage
1. Clone this repository.
2. Add your GitHub token in `scraper.py`.
3. Run the script:
   ```bash
   python scraper.py
GitHub Users in Sydney Analysis
This project scrapes data from GitHub's API to collect user profiles based in Sydney with over 100 followers and their public repositories.
After analyzing the data, we discovered that a majority of high-follower users work on open-source projects related to cloud technologies and data science.
Developers looking to increase visibility should consider contributing to trending repositories in these areas, as they have high engagement rates in Sydney's tech community.
Project Overview
This project aims to gather and analyze data on GitHub users based in Sydney who have over 100 followers, focusing on trends in their repositories. By leveraging the GitHub API, the project collects data on user profiles and their repositories, including followers, languages, licenses, and project types.

How the Data Was Scraped
User Search: Using GitHub's search endpoint, we identified users located in Sydney with over 100 followers. The search was implemented with pagination to ensure all results were retrieved, avoiding GitHub’s default limit of 30 results per page.
Profile and Repository Data: For each user, profile details and a list of repositories were collected. Repository data included key metrics such as stars, language, and license type.
CSV Output: The data was stored in two CSV files—one for user profiles (users.csv) and another for repositories (repositories.csv), to facilitate further analysis.
Interesting Insights
From the data analysis, we found that cloud and data science repositories had a strong presence among Sydney's top-followed GitHub users. Moreover, these users tend to collaborate frequently on trending open-source projects, particularly those involving Python and JavaScript.
Recommendations for Developers
Focus on Cloud and Data Science Projects: Developers seeking visibility within the Sydney tech community can benefit from contributing to repositories in these domains, which tend to attract higher follower counts and engagement.
Leverage Open Source Contribution: Engaging in popular open-source projects helps developers connect with others in their field and increase their visibility on GitHub.
Optimize Project Presentation: Use well-organized README files, consistent code documentation, and add licenses, as repositories with these features appear more frequently among high-follower users.
Usage
To replicate this data collection:

Clone the repository and install required dependencies:
bash
Copy code
git clone <repository-url>
cd <repository-name>
pip install -r requirements.txt
Update GITHUB_TOKEN in scraper.py with a personal GitHub token.
Run scraper.py to generate users.csv and repositories.csv files:
bash
Copy code
python scraper.py
