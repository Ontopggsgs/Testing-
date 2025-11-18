import requests

import time

import sys

import os

from colorama import Fore, Style, init

init(autoreset=True)

RED = Fore.RED

GREEN = Fore.GREEN

BLUE = Fore.BLUE

CYAN = Fore.CYAN

YELLOW = Fore.YELLOW

MAGENTA = Fore.MAGENTA

WHITE = Fore.WHITE

LIGHT_RED = Fore.LIGHTRED_EX

LIGHT_GREEN = Fore.LIGHTGREEN_EX

LIGHT_BLUE = Fore.LIGHTBLUE_EX

RESET = Style.RESET_ALL

SPINNER = ['|', '/', '-', '\\']

def clear():

    os.system("cls" if os.name == "nt" else "clear")

def typewrite(text, speed=0.03):

    for char in text:

        sys.stdout.write(char)

        sys.stdout.flush()

        time.sleep(speed)

    if text.endswith("\n"):

        sys.stdout.flush()

def blink_text(text, color=YELLOW, speed=0.08, duration=1.0):

    start_time = time.time()

    while time.time() - start_time < duration:

        sys.stdout.write(color + text + RESET)

        sys.stdout.flush()

        time.sleep(speed)

        sys.stdout.write(' ' * len(text))

        sys.stdout.flush()

        time.sleep(speed)

    print()

def loading_spinner_dynamic(message=""):

    start_time = time.time()

    duration = 2.0

    

    while time.time() - start_time < duration:

        color = [CYAN, LIGHT_BLUE, MAGENTA, WHITE][int((time.time() * 15) % 4)]

        sys.stdout.write('\r' + color + f"[{SPINNER[int(time.time() * 10) % 4]}] {message}..." + RESET)

        sys.stdout.flush()

        time.sleep(0.06)

    

    sys.stdout.write('\r' + ' ' * (len(message) + 15) + '\r')

    sys.stdout.flush()

def progress_scan_v2(steps):

    total_steps = len(steps)

    bar_length = 40

    

    for i, step in enumerate(steps):

        typewrite(MAGENTA + step + "\n", speed=0.03)

        

        filled_length = int(bar_length * (i + 1) // total_steps)

        bar = LIGHT_GREEN + '█' * filled_length + RESET + BLUE + '▓' * (bar_length - filled_length)

        

        sys.stdout.write(f'\rSCANNING: |{bar}| {(i + 1)}/{total_steps} ')

        sys.stdout.flush()

        time.sleep(0.5)

    

    print()

def print_header_v2(title):

    border_char = "#"

    border = border_char * (len(title) + 10)

    typewrite(f"\n{RED}{border}\n", speed=0.01)

    typewrite(f"{LIGHT_RED}{border_char}{WHITE} {title} {LIGHT_BLUE}{border_char}{RESET}\n", speed=0.01)

    typewrite(f"{RED}{border}\n", speed=0.01)

def processing_simulation(duration=1.0):

    start_time = time.time()

    colors = [GREEN, LIGHT_GREEN, CYAN, LIGHT_BLUE]

    

    while time.time() - start_time < duration:

        color = colors[int((time.time() * 20) % len(colors))]

        sys.stdout.write('\r' + color + "PROCESSING CORE DATA... " + Style.BRIGHT + "⚡" + RESET)

        sys.stdout.flush()

        time.sleep(0.04)

    

    sys.stdout.write('\r' + ' ' * 40 + '\r')

    sys.stdout.flush()

def print_map_load():

    typewrite(BLUE + "\n--- Rendering Map Tile Set ---" + RESET)

    map_chars = ['#', '@', '%', '&', '*', '+', '=', '-', '.']

    for i in range(30):

        char = map_chars[i % len(map_chars)]

        color = [CYAN, LIGHT_BLUE][i % 2]

        sys.stdout.write(color + char + RESET)

        sys.stdout.flush()

        time.sleep(0.02)

    typewrite(GREEN + "\nMap Loaded (Simulated)." + RESET)

# --- Možnosti 2, 3, 4 (Zůstávají stejné) ---

def network_test_simulation(targets):

    print_header_v2("NETWORK CONNECTIVITY TEST")

    typewrite(BLUE + "Pinging multiple targets simultaneously...\n" + RESET, speed=0.03)

    

    for target in targets:

        latency = f"{time.time() % 100:.2f}ms"

        if float(latency[:-3]) > 50.0:

            status_color = RED

            status_text = "FAIL"

        else:

            status_color = LIGHT_GREEN

            status_text = "OK"

            

        typewrite(f"{YELLOW}Target: {target:<20} | {status_color}Latency: {latency:<8} | {status_color}Status: {status_text}\n", speed=0.01)

        time.sleep(0.2)

    

    print_header_v2("TEST COMPLETE")

def dns_lookup_simulation(hostnames):

    print_header_v2("DNS RESOLUTION TEST")

    typewrite(BLUE + "Resolving hostnames...\n" + RESET, speed=0.03)

    

    for host in hostnames:

        ip_part1 = int(time.time() * 100) % 255

        ip_part2 = int(time.time() * 50) % 255

        simulated_ip = f"192.{ip_part1}.{ip_part2}.1"

        

        ipv6_part = hex(int(time.time() * 10000))[2:6]

        simulated_ipv6 = f"2001:db8::{ipv6_part}"

        

        typewrite(f"{YELLOW}Host: {host:<20} | {LIGHT_GREEN}A: {simulated_ip:<15} | {CYAN}AAAA: {simulated_ipv6}\n", speed=0.01)

        time.sleep(0.4)

        

    print_header_v2("DNS RESOLUTION COMPLETE")

def port_scan_simulation(ip):

    print_header_v2(f"PORT SCAN ON {ip}")

    typewrite(BLUE + "Scanning common ports...\n" + RESET, speed=0.03)

    

    common_ports = [21, 22, 23, 80, 443, 3389]

    

    for port in common_ports:

        is_open = (port % 2 == 0)

        

        if is_open:

            status_color = GREEN

            status_text = "OPEN"

        else:

            status_color = RED

            status_text = "CLOSED"

            

        typewrite(f"Port {port:<5} -> {status_color}{status_text:<6}\n", speed=0.05)

        time.sleep(0.3)

        

    print_header_v2("PORT SCAN FINISHED")

# --- MOŽNOST 5: SIMULACE BRUTE FORCE (VIZUÁLNÍ) ---

def brute_force_simulation(target):

    print_header_v2(f"BRUTE FORCE SIMULATION ON: {target}")

    typewrite(RED + "WARNING: This is a purely visual simulation. No actual login attempts are made.\n" + RESET, speed=0.02)

    time.sleep(1)

    

    attempts = 0

    max_attempts = 50

    

    while attempts < max_attempts:

        attempts += 1

        import random

        import string

        chars = string.ascii_letters + string.digits

        password = ''.join(random.choice(chars) for _ in range(8))

        

        status_color = YELLOW

        status_text = "Trying..."

        

        if attempts == 40:

            status_color = LIGHT_GREEN

            status_text = "SUCCESS!"

            typewrite(f"Credentials found: USER: admin | PASS: {password}\n", speed=0.05)

            break

        

        typewrite(f"Attempt {attempts:02d}/{max_attempts} | Trying: {password:<10} | {status_color}{status_text}\n", speed=0.01)

        time.sleep(0.05)

        

    if attempts >= max_attempts:

        typewrite(RED + "\nBrute force simulation ended: Max attempts reached.\n" + RESET)

        

    print_header_v2("SIMULATION ENDED")


def run_ip_lookup():

    scan_steps = [

        "Validating network handshake",
        "Querying geolocation database",
        "Extracting metadata payload"

    ]

    progress_scan_v2(scan_steps)

    ip = input(CYAN + "Target IP Address > " + RESET).strip()

    if not ip:

        blink_text(RED + "ERROR: No IP provided. Aborting.", duration=2.0, speed=0.05)

        return

    typewrite(BLUE + "\nExecuting IP lookup sequence...\n" + RESET, speed=0.04)

    try:

        response = requests.get(f"http://ipinfo.io/{ip}/json")

        data = response.json()

        if "error" in data or "bogon" in data:

            blink_text(RED + f"Lookup Failed: IP {ip} is private or invalid.", duration=2.5, speed=0.05)

            return

        processing_simulation(1.5) 

        

        print_header_v2("GEOLOCATION REPORT")

        output_data = [

            ("IP", data.get('ip')),
            ("City", data.get('city')),
            ("Region", data.get('region')),
            ("Country", data.get('country')),
            ("ISP/Org", data.get('org')),
            ("Timezone", data.get('timezone')),
            ("ASN", data.get('asn')),
            ("Coordinates", data.get('loc')) 

        ]

        

        for k, v in output_data:

            typewrite(f"{YELLOW}{k:<12}:{RESET} {WHITE}{v}\n", speed=0.005)

            time.sleep(0.1)

        print_map_load()

        print_header_v2("MISSION COMPLETE")

        blink_text(GREEN + "\nData acquisition successful.", duration=2.5, speed=0.07)

    except Exception as e:

        blink_text(RED + f"CRITICAL FAILURE: {e}", duration=3.0, speed=0.05)

def run_network_test():

    targets = [

        "8.8.8.8",
        "1.1.1.1",
        "192.168.1.1",
        "google.com"

    ]

    network_test_simulation(targets)

    time.sleep(1)

    

    print_header_v2("CONNECT WITH ME")

    typewrite(CYAN + "Instagram: " + RESET, speed=0.01)

    blink_text("zitsurias_", color=MAGENTA, duration=1.5, speed=0.07)

    

    typewrite(CYAN + "TikTok:    " + RESET, speed=0.01)

    blink_text("cauahojnevimsebik", color=WHITE, duration=1.5, speed=0.07)

    

    time.sleep(0.5)

    blink_text(LIGHT_GREEN + "\nAll tests concluded.", duration=2.0, speed=0.07)


# --- HLAVNÍ MENU ---

def main_menu():

    clear()

    

    banner_top = CYAN + r"""

 __     ___      _              _       

 \ \   / (_) ___| |_ ___  _ __ (_) ___  

  \ \ / /| |/ __| __/ _ \| '_ \| |/ _ \ 

   \ V / | | (__| || (_) | |_) | | (_) |
    \_/  |_|\___|\__\___/| .__/|_|\___/ 

                           |_|  

"""

    print(banner_top)

    

    author_line = (

        MAGENTA + "           created by zitsuro" + RESET + 

        WHITE + " | " + Style.BRIGHT + YELLOW + "zijuvpritomnosti DISCORD!!" + RESET

    )

    typewrite(author_line, speed=0.04)

    

    typewrite(YELLOW + "\nInitializing Core Systems..." + RESET, speed=0.03)

    blink_text("SYSTEM ONLINE", color=LIGHT_GREEN, duration=1.2, speed=0.07)

    loading_spinner_dynamic("Loading modules")

    print_header_v2("TOOL SELECTION")

    

    print(f"1. {GREEN}IP Geolocation Lookup (ipinfo.io)")

    print(f"2. {LIGHT_BLUE}Network Connectivity Test (Simulated Ping)")

    print(f"3. {CYAN}DNS Record Lookup (Simulated)")

    print(f"4. {MAGENTA}Port Scanner (Simulated)")

    print(f"5. {RED}DDos Attack  # atím nefunkční")

    

    choice = input(CYAN + "\nSelect option (1-5): " + RESET).strip()

    

    if choice == '1':

        run_ip_lookup()

    elif choice == '2':

        run_network_test()

    elif choice == '3':

        hostnames = ["www.seznam.cz", "github.com", "localhost"]

        dns_lookup_simulation(hostnames)

    elif choice == '4':

        ip_for_scan = input(CYAN + "Enter target IP for Port Scan > " + RESET).strip()

        if ip_for_scan:

            port_scan_simulation(ip_for_scan)

        else:

            blink_text(RED + "IP required for Port Scan.", duration=1.5, speed=0.05)

    elif choice == '5':

        # BEZPEČNOSTNÍ OCHRANA: Zobrazí error a vrátí se do menu

        clear()

        print_header_v2("SECURITY PROTOCOL ALERT")

        blink_text(RED + "ACCESS DENIED: Malicious activity detected.", duration=3.0, speed=0.1)

        typewrite(YELLOW + "\nThis function is disabled due to ethical constraints and security policies.\n", speed=0.02)

        time.sleep(2)

        input(CYAN + "Press Enter to return to menu...")

        main_menu() # Rekurzivní volání pro návrat do menu

        return # Ukončí aktuální volání main_menu

    else:

        blink_text(RED + "Invalid selection. Exiting.", duration=2.0, speed=0.05)

        sys.exit() # Ukončí program, pokud je volba úplně mimo rozsah

    # Po dokončení akce (1-4) se vrátíme do menu

    if choice in ('1', '2', '3', '4'):

        input(CYAN + "\nPress Enter to return to menu...")

        main_menu()


if __name__ == "__main__":

    main_menu()    return "\n".join(lines)

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
