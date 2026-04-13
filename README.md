╔══════════════════════════════════════════════════════════╗
║        ADVANCED WEB PARAMETER & FORM SCANNER             ║
╚══════════════════════════════════════════════════════════╝

> A powerful Python-based web crawler with stealth features
> like rotating user-agents, retry system, and smart delays.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[✓] URL Parameter Detection  
[✓] Advanced HTML Form Extraction  
[✓] Input Field Enumeration  
[✓] Form Action & Method Detection  
[✓] Internal Link Crawling (Depth Based)  
[✓] Rotating User-Agent System  
[✓] Auto Retry (Handles 429, 500, 503, etc.)  
[✓] Random Delay (Anti-Rate-Limit)  
[✓] SSL Warning Bypass  
[✓] Clean Hacker-Style Terminal UI  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠 REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Python 3 must be installed.

Install dependencies:

pip install requests  
pip install beautifulsoup4  
pip install urllib3  

OR install all at once:

pip install requests beautifulsoup4 urllib3  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 INSTALLATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Clone the repository:

git clone https://github.com/your-username/advanced-scanner.git  

Move into the directory:

cd advanced-scanner  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▶️ USAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run the tool:

python scanner.py  

Enter your target:

TARGET >>> https://example.com  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 HOW IT WORKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1] Accepts target URL  
[2] Extracts query parameters from URL  
[3] Sends request using random User-Agent  
[4] Parses HTML content  
[5] Finds all forms on page  
[6] Extracts:
     - Form action URL  
     - Method (GET/POST)  
     - Input fields  
[7] Crawls internal links recursively  
[8] Uses retry system if blocked or failed  
[9] Applies random delay (2–5 sec) to avoid detection  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚙ CONFIGURATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Change crawling depth:

crawl(target, depth=2)

Increase for deeper scanning  
Decrease for faster results  


Modify delay range:

random.uniform(2, 5)

Change values to control speed vs stealth  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡 STEALTH FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Rotates multiple User-Agents  
- Retries failed requests automatically  
- Handles HTTP errors (429, 500, etc.)  
- Random delay to reduce detection risk  
- Ignores SSL certificate warnings  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠ DISCLAIMER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This tool is created for EDUCATIONAL PURPOSES ONLY.

Unauthorized scanning is illegal.

You are responsible for your own actions.
The developer will not be held liable for misuse.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👨‍💻 AUTHOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Developer : noobxvau  
Team      : noob hacker BD  
YouTube   : The noob coder  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ SUPPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If you like this tool:

[★] Star the repository  
[★] Share with others  
[★] Follow for more tools  


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 VERSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Version : 2.0 (Advanced Stealth Edition)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
