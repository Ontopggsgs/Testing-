import requests
import time
import sys
import os
from PIL import Image
from colorama import Fore, Style, init

init()

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

GIF_URL = "https://media1.tenor.com/m/En4BFk4ihwgAAAAC/yay-yeah.gif"
GIF_FILENAME = "hacker.gif"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def ascii_frame(image, width=40):
    image = image.convert("L")  # grayscale
    w, h = image.size
    aspect_ratio = h / w
    new_height = int(aspect_ratio * width * 0.55)
    image = image.resize((width, new_height))

    pixels = image.getdata()
    chars = "@%#*+=-:. "  # from dark to light
    new_pixels = [chars[pixel * len(chars) // 256] for pixel in pixels]
    lines = [
        "".join(new_pixels[i:i+width])
        for i in range(0, len(new_pixels), width)
    ]
    return "\n".join(lines)

def download_gif(url, filename):
    if os.path.exists(filename):
        return
    try:
        print(BLUE + f"Downloading GIF animation..." + RESET)
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(GREEN + "Download complete.\n" + RESET)
    except Exception as e:
        print(RED + f"Failed to download GIF: {e}" + RESET)
        sys.exit(1)

def play_gif_ascii(path, loops=3, delay=0.1, width=50):
    try:
        gif = Image.open(path)
    except Exception as e:
        print(RED + f"Could not load GIF: {e}" + RESET)
        return

    frames = []
    try:
        while True:
            frames.append(ascii_frame(gif.convert("RGBA"), width))
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass

    for _ in range(loops):
        for frame in frames:
            clear()
            print(CYAN + frame + RESET)
            time.sleep(delay)

download_gif(GIF_URL, GIF_FILENAME)
play_gif_ascii(GIF_FILENAME)

clear()

banner = CYAN + r"""
 __     ___      _              _       
 \ \   / (_) ___| |_ ___  _ __ (_) ___  
  \ \ / /| |/ __| __/ _ \| '_ \| |/ _ \ 
   \ V / | | (__| || (_) | |_) | | (_) |
    \_/  |_|\___|\__\___/| .__/|_|\___/ 
                           |_|  
                     created by zitsuro
""" + RESET

def typewrite(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if text.endswith("\n"):
        sys.stdout.flush()

print(banner)

typewrite(BLUE + "Loading modules, trying not to break anything", speed=0.03)
for _ in range(6):
    time.sleep(0.4)
    sys.stdout.write(".")
    sys.stdout.flush()
time.sleep(0.3)
print("\n")

scan_steps = [
    "Warming up the internet hamsters",
    "Pretending to look important",
    "Talking to IP servers politely",
    "Convincing API to cooperate",
    "Preparing results like a gourmet chef"
]

for step in scan_steps:
    typewrite(YELLOW + step + "..." + RESET + "\n", speed=0.05)
    time.sleep(0.6)

print()

ip = input(CYAN + "Enter the target IP address: " + RESET).strip()

if not ip:
    print(RED + "No IP entered. I can't read your mind yet." + RESET)
    exit()

typewrite(BLUE + "\nSearching for location. Please hold while I do magic.\n" + RESET, speed=0.04)
time.sleep(1)

try:
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    data = response.json()

    if "error" in data:
        typewrite(RED + f"Great. The API said no: {data.get('reason', 'Unknown error')}\n" + RESET, speed=0.04)
        exit()

    typewrite(GREEN + "\n===== RESULTS =====\n" + RESET, speed=0.05)
    for k, v in [
        ("IP", data.get('ip')),
        ("Country", data.get('country_name')),
        ("City", data.get('city')),
        ("Region", data.get('region')),
        ("ISP", data.get('org')),
        ("Coordinates", f"{data.get('latitude')}, {data.get('longitude')}")
    ]:
        typewrite(f"{k}: {v}\n", speed=0.03)
        time.sleep(0.2)
    typewrite(GREEN + "====================\n" + RESET, speed=0.05)

except Exception as e:
    typewrite(RED + f"Something went wrong. Blame the universe: {e}\n" + RESET, speed=0.04)
