import urllib.request

ids = open('id.txt','r')

image = 'https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srimages/sr_icon_l_60'
evolve = 'https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srimages/sr_icon_l_61'
gacha = 'https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srgachas/gacha_60'

for id in ids:
    while len(id.strip()) < 5:
        id = f'0{id.strip()}'
    urllib.request.urlretrieve(f'{image}{id}.png', f'sr_icon_l_60{id}.png')
    urllib.request.urlretrieve(f'{evolve}{id}.png', f'sr_icon_l_61{id}.png')
    urllib.request.urlretrieve(f'{gacha}{id}.png', f'sr_gacha_60{id}.png')