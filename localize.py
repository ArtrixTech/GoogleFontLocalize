import requests
from cut_string import cut_string


class Font:
    def __init__(self, family, file_name, download_addr):
        self.file_name = file_name
        self.font_family = family
        self.download_address = download_addr


def err_handle(response):
    if "Missing font family" in response:
        print("    ERROR: The target font family is not exist. Plz check the pronunciation of font-name.")
        return False
    return True


url_base = "https://fonts.googleapis.com/css?family="
font_family = input("Please input the font family you wanna localize:\n")

resp = requests.get(url_base + font_family).text
if err_handle(resp):
    all_fonts = []
    dest_dir = input("Please input the local resource destination directory:\n")

    blocks = resp.split(";")
    index = 0
    for item in blocks:
        if "url" in item:
            download_item = cut_string(item, "url(", ")")
            expand_name = download_item.split(".")[-1]

            all_fonts.append(Font(font_family, font_family + "_" + str(index) +"."+ expand_name, download_item))

    for font in all_fonts:
        font_file_name = font.file_name
        font_download_address=font.download_address
        
