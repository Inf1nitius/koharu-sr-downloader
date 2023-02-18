import urllib.request


def get_images():
    with open("id.txt", "r") as ids:
        for id in ids:
            while len(id.strip()) < 5:
                id = f"0{id.strip()}"
            urllib.request.urlretrieve(
                f"https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srimages/sr_icon_l_60{id}.png",
                f"sr_icon_l_60{id}.png",
            )
            urllib.request.urlretrieve(
                f"https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srimages/sr_icon_l_61{id}.png",
                f"sr_icon_l_61{id}.png",
            )
            urllib.request.urlretrieve(
                f"https://raw.githubusercontent.com/Nayuta-Kani/SAOIF-Skill-Records-Database/master/srgachas/gacha_60{id}.png",
                f"sr_gacha_60{id}.png",
            )


if __name__ == "__main__":
    get_images()
