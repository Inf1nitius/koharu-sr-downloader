from git import Repo
import jinja2
import random
import time


def get_id_updated():
    repo = Repo(".")
    assert not repo.bare
    commit = next(repo.iter_commits(paths="id.txt", max_count=1))
    return commit.committed_date

def id_pad(id):
    while len(id) < 5:
        id = f"0{id}"
    return id


def get_url():
    with open("id.txt", "r") as ids:
        ids = ids.readlines()
        if time.time() - get_id_updated() <= 86400:
            latest_sr = id_pad(ids[-1].strip())
            return f"https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srimages/sr_icon_l_60{latest_sr}.png"
        else:    
            random_sr = id_pad(random.choice(ids).strip())
            return f"https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srimages/sr_icon_l_6{random.choice((0,1))}{random_sr}.png"

def update_README():
    with open("TEMPLATE.md", "r", encoding="utf-8") as TEMPLATE:
        template = jinja2.Template(TEMPLATE.read())
        open("README.md", "w", encoding="utf-8").write(
            template.render(id_updated=get_id_updated(), url=get_url())
        )


if __name__ == "__main__":
    update_README()
