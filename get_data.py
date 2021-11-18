from github import Github
from rich import print

import time
from datetime import datetime
import os

end_time = time.time()
start_time = end_time - 86400


def check_query(library):
    t_query = f"{library} language:python created:2021-10-01..2021-10-03"
    result = g.search_repositories(t_query)
    print(f"{library} = {result.totalCount}")
    return result


with open("token.txt") as file_pointer:
    ACCESS_TOKEN = file_pointer.read()
    g = Github(ACCESS_TOKEN)

    for i in range(5):
        start_time_str = datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d")
        end_time_str = datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d")

        query = f"language:python created:{start_time_str}..{end_time_str}"
        print(query)
        end_time -= 86400
        start_time -= 86400

        result = g.search_repositories(query)
        print(result.totalCount)

        for repository in set(result):
            print(f"{repository.clone_url}")
            os.system(
                f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}"
            )
