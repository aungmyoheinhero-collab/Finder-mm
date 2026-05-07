import os, sys, time, json, base64, uuid, subprocess, socket

# requests library check
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# Colors
G, R, B, Y, C, W = "\033[1;32m", "\033[1;31m", "\033[1;34m", "\033[1;33m", "\033[1;36m", "\033[1;37m"

def banner():
    os.system('clear')
    print(f"""{C}
    ╔════════════════════════════════════════╗
    ║      EDY ULTIMATE - PREMIUM EDITION    ║
    ╚════════════════════════════════════════╝{W}
    DEV   : {G}AungMyoHein{W}
    GGMU  : {R}Manchester United Fan 🔴{W}
    ------------------------------------------""")

def generate_vmess(bug, ip):
    v2_json = {
        "v": "2", "ps": f"EDY-FREE-{bug}",
        "add": ip, "port": "80", "id": str(uuid.uuid4()),
        "aid": "0", "scy": "auto", "net": "ws",
        "type": "none", "host": bug, "path": "/", "tls": "none"
    }
    js_str = json.dumps(v2_json)
    return "vmess://" + base64.b64encode(js_str.encode('ascii')).decode('ascii')

# --- Choice 1: IP Checker ---
def cf_ip_checker():
    banner()
    print(f"{C}[*] Cloudflare IP Speed Checker...{W}\n")
    targets = ["104.16.10", "104.17.10", "104.18.10", "172.67.73", "104.21.10"]
    for subnet in targets:
        for i in range(1, 10):
            ip = f"{subnet}.{i}"
            print(f"{W}[Testing] {ip}...", end="\r")
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                if sock.connect_ex((ip, 80)) == 0:
                    print(f"{G}[FOUND] {ip:<15} | Port 80 Open{W}")
                sock.close()
            except: continue
    input(f"\n{Y}Press Enter to return...{W}")

# --- Choice 2: Improved Bug Hunter (More Reliable) ---
def bug_scanner_gen():
    banner()
    target = input(f"{Y}[?] Enter Domain (eg. mytel.com.mm): {W}")
    cf_ip = input(f"{Y}[?] Enter Fast CF IP (Default: 104.18.10.1): {W}") or "104.18.10.1"
    
    print(f"\n{C}[*] Fetching Hosts and Scanning...{W}\n")
    print(f"{'HOST':<35} | {'CODE':<5} | {'RESULT'}")
    print("-" * 60)
    
    subs = []
    # Method 1: crt.sh (with longer timeout)
    try:
        res = requests.get(f"https://crt.sh/?q=%25.{target}&output=json", timeout=25)
        if res.status_code == 200:
            subs = list(set([item['common_name'] for item in res.json()]))
    except:
        pass

    # Method 2: Hackertarget (Backup if crt.sh fails)
    if not subs:
        try:
            res = requests.get(f"https://api.hackertarget.com/hostsearch/?q={target}", timeout=15)
            for line in res.text.split('\n'):
                if ',' in line: subs.append(line.split(',')[0])
        except:
            pass

    if not subs:
        print(f"{R}[!] Error: Could not fetch subdomains. Check Internet!{W}")
    else:
        subs = list(set(subs)) # Remove duplicates
        for host in subs:
            if "*" in host or "@" in host: continue
            try:
                # Fast Status Check
                r = requests.get(f"http://{host}", timeout=2, allow_redirects=False)
                status = r.status_code
                
                if status in [200, 101, 301, 302]:
                    res_txt = f"{G}WORKING!{W}" if status in [200, 101] else f"{Y}REDIRECT{W}"
                    print(f"{W}{host:<35} | {status:<5} | {res_txt}")
                    if status in [200, 101]:
                        print(f"{C}[V2RAY] {generate_vmess(host, cf_ip)}{W}\n")
                else:
                    print(f"{W}{host:<35} | {status:<5} | {R}FAILED{W}")
            except:
                print(f"{W}{host:<35} | {'ERR':<5} | {R}DOWN{W}")
                continue
    
    input(f"\n{G}Scan Complete! Press Enter to return...{W}")

def main():
    while True:
        banner()
        print(f"{G}[1]{W} Cloudflare IP Checker")
        print(f"{G}[2]{W} Advanced Bug Scanner & V2Ray Gen")
        print(f"{G}[3]{W} Manual V2Ray Link Generator")
        print(f"{R}[0]{W} Exit")
        
        choice = input(f"\n{C}Edy Choice > {W}")
        if choice == '1': cf_ip_checker()
        elif choice == '2': bug_scanner_gen()
        elif choice == '3':
            banner()
            bug = input(f"{Y}Enter Bug: {W}"); ip = input(f"{Y}Enter CF IP: {W}")
            print(f"\n{G}[+] Link:{W}\n{C}{generate_vmess(bug, ip)}{W}")
            input("\nEnter to return...")
        elif choice == '0': break

if __name__ == "__main__":
    main()
