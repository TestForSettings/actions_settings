#pip install pygithub

from github import Github
import yaml
from pprint import pprint
import os


# GITHUB_API_URL = "https://api.github.com/"
# ORG_NAME = "TestForSettings"

file = open("Token.txt", "r")
token = file.readline()

file.close()

TOKEN = os.environ["API_TOKEN"]
# First create a Github instance:
# using an access token
g = Github(token)

# Here I will save the names of the repos that have as a topic "testing"
repo_names = []
# print(repo_names)
with open("settings.yaml", "r") as file:
    target_settings = yaml.load(file, Loader=yaml.FullLoader)

for repo in g.get_user().get_repos():
    # print(repo.name)
    for topic in repo.topics:
        if topic == 'testing':
            # repo_names.append(repo.name)
            print(repo.name + ' is updating...\n')
            # repo.edit(has_wiki=False)
            for key in target_settings:
                # print(key)
                # print(target_settings[key])
                repo.edit(**target_settings)
                if key == list(target_settings.keys())[-1]:
                    print(key + ' is updated\n')
                else:
                    print(key + ' is updated')