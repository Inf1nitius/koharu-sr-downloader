import jinja2
import random

README = open('README.md','w', encoding="utf-8")

with open('id.txt','r') as ids:
    ids = ids.readlines()
    lines = len(ids)
    random_sr = ids[random.randint(1,lines-1)].strip()
    while len(random_sr.strip()) < 5:
        random_sr = f'0{random_sr.strip()}'
    url = f"https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srimages/sr_icon_l_60{random_sr}.png"

with open("TEMPLATE.md", "r", encoding="utf-8") as TEMPLATE:
    template = jinja2.Template(TEMPLATE.read())
    README.write(template.render(url=url))