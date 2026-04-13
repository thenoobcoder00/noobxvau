import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
import time
import sys
import os
import random
import warnings
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Ignore SSL warnings
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

visited = set()

# ======================
# ROTATING USER-AGENTS
# ======================
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0",
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Cache-Control": "no-cache",
    }

# ======================
# SESSION WITH RETRIES
# ======================
def get_session_with_retries():
    session = requests.Session()
    retries = Retry(
        total=3,                     # সর্বমোট ৩ বার রিট্রাই
        backoff_factor=1,            # 1, 2, 4 সেকেন্ড দেরি
        status_forcelist=[500, 502, 503, 504, 429],  # এই স্ট্যাটাসে রিট্রাই
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# ======================
# COLOR STYLE
# ======================
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

# ======================
# ANIMATION FUNCTIONS
# ======================
def type_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading(text):
    for _ in range(3):
        sys.stdout.write(f"\r{text}.  ")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{text}.. ")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{text}...")
        sys.stdout.flush()
        time.sleep(0.3)
    print()

# ======================
# BANNER
# ======================
os.system("clear")
print(MAGENTA + BOLD + r"""
                                        
▗▄ ▗▖ ▗▄▖  ▗▄▖ ▗▄▄▖ ▗▄ ▄▖▗▖ ▗▖  ▄  ▗▖ ▗▖
▐█ ▐▌ █▀█  █▀█ ▐▛▀▜▌ █▄█ ▝█ █▘ ▐█▌ ▐▌ ▐▌
▐▛▌▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ ▐█▌  █ █  ▐█▌ ▐▌ ▐▌
▐▌█▐▌▐▌ ▐▌▐▌ ▐▌▐███   █   █ █  █ █ ▐▌ ▐▌
▐▌▐▟▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ ▐█▌  ▐█▌  ███ ▐▌ ▐▌
▐▌ █▌ █▄█  █▄█ ▐▙▄▟▌ █ █  ▐█▌ ▗█ █▖▝█▄█▘
▝▘ ▀▘ ▝▀▘  ▝▀▘ ▝▀▀▀ ▝▀ ▀▘ ▝▀▘ ▝▘ ▝▘ ▝▀▘ 
                                        
                                        
""" + RESET)

print(CYAN + BOLD + "[ DEVELOPER  ] " + RESET + YELLOW + "noobxvau")
print(CYAN + BOLD + "[ TEAM       ] " + RESET + YELLOW + "noob hacker BD")
print(CYAN + BOLD + "[ YOUTUBE    ] " + RESET + YELLOW + "The noob coder\n")

type_print(BLUE + BOLD + "[ SYSTEM INITIALIZING ]" + RESET)
loading("Booting modules")
type_print(GREEN + BOLD + "[ OK ] Scanner Ready\n" + RESET)

# ======================
# PARAMETER & FORM FUNCTIONS
# ======================
def find_url_params(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    if params:
        print(GREEN + BOLD + "\n[+] URL Parameters Found:" + RESET)
        for k, v in params.items():
            print(YELLOW + f"   -> {k} = {v[0]}" + RESET)

def find_forms(url):
    session = get_session_with_retries()
    try:
        headers = get_random_headers()
        r = session.get(url, headers=headers, timeout=20, verify=False)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        forms = soup.find_all("form")
        if forms:
            print(GREEN + BOLD + f"\n[+] Forms Detected: {len(forms)}" + RESET)
        for form in forms:
            action = form.get("action")
            method = form.get("method", "GET").upper()
            action_url = urljoin(url, action)
            print(CYAN + BOLD + "\n--- FORM TARGET ---" + RESET)
            print(YELLOW + f"Action : {action_url}")
            print(f"Method : {method}" + RESET)
            inputs = form.find_all("input")
            for inp in inputs:
                name = inp.get("name")
                typ = inp.get("type")
                if name:
                    print(GREEN + f"Input -> {name} ({typ})" + RESET)
    except requests.exceptions.SSLError:
        print(RED + BOLD + "[!] SSL Error - Try disabling verify" + RESET)
    except requests.exceptions.ConnectionError as e:
        print(RED + BOLD + f"[!] Connection failed: {e}" + RESET)
    except requests.exceptions.Timeout:
        print(RED + BOLD + "[!] Request timeout" + RESET)
    except requests.exceptions.HTTPError as e:
        print(RED + BOLD + f"[!] HTTP {e.response.status_code} - Blocked" + RESET)
    except Exception as e:
        print(RED + BOLD + f"[!] Form parsing failed: {e}" + RESET)

# ======================
# CRAWLER WITH RETRY & DELAY
# ======================
def crawl(url, depth=1):
    if depth == 0 or url in visited:
        return
    visited.add(url)

    type_print(CYAN + BOLD + f"\n[ SCANNING ] {url}" + RESET, 0.01)
    find_url_params(url)
    find_forms(url)

    # Random delay to avoid rate limiting (2-5 seconds)
    delay = random.uniform(2, 5)
    time.sleep(delay)

    session = get_session_with_retries()
    try:
        headers = get_random_headers()
        r = session.get(url, headers=headers, timeout=20, verify=False)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all("a", href=True)
        for link in links:
            new_url = urljoin(url, link["href"])
            if urlparse(new_url).netloc == urlparse(url).netloc:
                crawl(new_url, depth - 1)
    except requests.exceptions.ConnectionError as e:
        print(RED + BOLD + f"[!] Crawl blocked (ConnectionError): {e}" + RESET)
    except requests.exceptions.Timeout:
        print(RED + BOLD + "[!] Crawl timeout" + RESET)
    except requests.exceptions.HTTPError as e:
        print(RED + BOLD + f"[!] HTTP {e.response.status_code} - Access denied" + RESET)
    except Exception as e:
        print(RED + BOLD + f"[!] Crawl error: {e}" + RESET)

# ======================
# MAIN
# ======================
target = input(GREEN + BOLD + "TARGET >>> " + RESET)
loading("Connecting to target")
crawl(target, depth=2)
type_print(GREEN + BOLD + "\n[✓] SCAN COMPLETE" + RESET)
type_print(CYAN + BOLD + "[ SESSION TERMINATED ]" + RESET)