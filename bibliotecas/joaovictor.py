import pyfiglet
from colorama import *
init(autoreset=True)

# text = "Cabareh do Jose"
# ascii_art = pyfiglet.figlet_format(text, font="slant")
# print(Fore.MAGENTA + ascii_art)

lis = ['cabare do jose','Carro do jose','Careca do jose']

ascii_art = pyfiglet.figlet_format(lis, font='slant')

print(Fore.CYAN + ascii_art)