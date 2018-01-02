import requests
import datetime


def get_trending_repositories(top_size):
    days_amount = 7
    now = datetime.datetime.now()
    last_week = now.date() - datetime.timedelta(days=days_amount)

    response = requests.get(
        'https://api.github.com/search/repositories',
        params={
            'q': 'created:>={}'.format(str(last_week)),
            'sort': 'stars',
        },
    )
    repositories = response.json()['items'][:top_size]
    return repositories


def get_open_issues_amount(repo_owner, repo_name):
    response = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name),
        params={'state': 'open'},
    )
    return len(response.json())


if __name__ == '__main__':
    top_size_repo = 20
    repos = get_trending_repositories(top_size_repo)

    for index, repo in enumerate(repos, start=1):
        repo_owner = repo['owner']['login']
        repo_name = repo['name']
        repo_url = repo['html_url']
        issues_amount = get_open_issues_amount(repo_owner, repo_name)
        print(
            index,
            repo_url,
            ' ({} open issues)'.format(issues_amount),
        )
