import requests
import datetime


def get_trending_repositories(top_size):
    day_of_week = 7
    now = datetime.datetime.now()
    date_week_earlier = now.date() - datetime.timedelta(days=day_of_week)

    query = requests.get(
        'https://api.github.com/search/repositories',
        params={
            'q': 'created:>={}'.format(str(date_week_earlier)),
            'sort': 'stars',
        },
    )
    repositories = query.json()['items'][:top_size]
    return repositories


def get_open_issues_amount(repo_owner, repo_name):
    query = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(
            repo_owner, repo_name),
        params={'state': 'open'},
    )
    return len(query.json())


if __name__ == '__main__':
    top_size_repo = 20
    repos = get_trending_repositories(top_size_repo)

    list_repos = []
    for repo in repos:
        repo_owner = repo['owner']['login']
        repo_name = repo['name']
        repo_url = repo['html_url']
        issues_amount = get_open_issues_amount(repo_owner, repo_name)
        list_repos.append({'repo_url': repo_url, 'issues_data': issues_amount})

    for repo in list_repos:
        print(
            list_repos.index(repo) + 1,
            repo['repo_url'],
            repo['issues_data']
        )
