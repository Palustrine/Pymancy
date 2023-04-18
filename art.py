import os
from ascii_magic import AsciiArt
from PIL import Image
from rich import print

# organise cards
# -- name, value, description, suit, type img
# -- convert images to ascii

# img.show()  - to display img

cards_folder = os.listdir(".\\cards")

# sort images to suits
for i in cards_folder:
    print(i)
    #major cards
    major_img = {}
    if i == "majors":
        majors_folder = os.listdir(".\\cards\\majors")
        for i in range(len(majors_folder)):
            img = Image.open(f".\\cards\\majors\\{majors_folder[i]}")
            # i gotta rethink this probably
            major_img = {"name": majors_folder[i], "value": int(majors_folder[i].strip(".png")), "img": img.filename}
            print(major_img)
    #minor cards
    elif i == "wands":
        wands_folder = os.listdir(".\\cards\\wands")
        for i in range(len(wands_folder)):
            img = Image.open(f".\\cards\\wands\\{wands_folder[i]}")
            wands_img = {"name": wands_folder[i], "value": wands_folder[i].strip(".png"), "img": img.filename}
            print(wands_img)
    elif i == "cups":
        cups_folder = os.listdir(".\\cards\\cups")
        for i in range(len(cups_folder)):
            img = Image.open(f".\\cards\\cups\\{cups_folder[i]}")
            cups_img = {"name": cups_folder[i], "value": cups_folder[i].strip(".png"), "img": img.filename}
            print(cups_img)
    elif i == "swords":
        swords_folder = os.listdir(".\\cards\\swords")
        for i in range(len(swords_folder)):
            img = Image.open(f".\\cards\\swords\\{swords_folder[i]}")
            swords_img = {"name": swords_folder[i], "value": swords_folder[i].strip(".png"), "img": img.filename}
            print(swords_img)
    elif i == "pentacles":

        pentacles_folder = os.listdir(".\\cards\\pentacles")
        for i in range(len(pentacles_folder)):
            img = Image.open(f".\\cards\\pentacles\\{pentacles_folder[i]}")
            pentacles_img = {"name": pentacles_folder[i], "value": pentacles_folder[i].strip(".png"), "img": img.filename}
            print(pentacles_img)
    else:
        print(":(")

def img_convert():
    convert = AsciiArt.from_image(f".\\cards\\pentacles\\{pentacles_folder[i]}")
    AsciiArt.to_terminal(convert)