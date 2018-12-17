from github import Github
import time
import random

g = Github("9aac0471762807ba57074c6fc6b1404ecfa3b96a")

#for repo in g.get_user().get_repos():
#    print(repo)


def repoBoi(g, r, sleepTime):
    return g.get_repo(r)

content = ""
with open("repolist.txt") as f:
    content = f.readlines()

content = [s.strip() for s in content]

gamerepos = [g.get_repo(r) for r in content[1:10]]

for game in gamerepos:
    print(game.language)
