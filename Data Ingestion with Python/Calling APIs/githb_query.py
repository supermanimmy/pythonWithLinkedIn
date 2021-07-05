"""Query GitHub API"""

from datetime import datetime
from urllib.request import urlopen
import json

def user_time(login):
    url = 'https://api.github.com/users/' + login
    resp = urlopen(url)
    reply = json.load(resp)
    # "2008-01-14T04:33:35Z", we trim the 'Z' with [:-1]
    ts = reply['created_at']
    created = datetime.fromisoformat(ts[:-1])
    print(created)
    return datetime.utcnow() - created

def user_update(login):
    url = 'https://api.github.com/users/' + login
    resp = urlopen(url)
    reply = json.load(resp)
    # "updated_at": "2008-01-14T04:33:35Z",
    ts = reply['updated_at']
    updated = datetime.fromisoformat(ts[:-1])
    print(updated)


def public_repos(login):
    url = 'https://api.github.com/users/' + login
    resp = urlopen(url)
    reply = json.load(resp)
    # "public_repos": 3,
    ts = reply['public_repos']
    updated = ts
    print(updated)


login = 'seird'

public_repos(login)