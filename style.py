class Color:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    purple = '\033[95m'
    cyan = '\033[96m'
    light_green = '\033[1;32m'
    grey = '\033[90m'
    light_gray = '\033[1;37;40m'
    end = '\033[0m'

class Textstyle:
    bold = '\033[1m'
    negative = '\033[7m'
    underlined = '\033[4m'
    dim = '\033[2m'

def configure_textstyle(text:str, farbe:str, style:str)-> None:
    farb_code = getattr(Color, farbe.lower(), "")
    style_code = getattr(Textstyle, style.lower(), "")

    print(f"{style_code}{farb_code}{text}{Color.end}",end="")


def visual_test(farbe:str)-> None:  #um schnell die Farben in den verschieden Textstyles zu testen
    farb_code = getattr(Color, farbe.lower(), "")

    print(f"{farb_code}farbe{Color.end}\n"
          f"{farb_code}{Textstyle.underlined}underlined{Color.end}\n"
          f"{farb_code}{Textstyle.bold}bold{Color.end}\n"
          f"{farb_code}{Textstyle.negative}negative{Color.end}")