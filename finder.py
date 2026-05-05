import os
import time

def menu():
    os.system('clear')
    print("==============================================")
    print("    UNIVERSAL PERSON FINDER - MYANMAR         ")
    print("       (Comprehensive Edition v16.0)          ")
    print("==============================================")
    print("[1] Social Media Search (Name + City)")
    print("[2] NRC Deep Scan (PDFs & Official Data)")
    print("[3] Phone Number Search (Truecaller/Web)")
    print("[4] Full Myanmar Search (21 Regions & News)")
    print("[0] Exit")
    print("==============================================")

def run_full_search(name, phone, nrc, city):
    regions = [
        "YANGON", "MANDALAY", "BAGO", "AYEYARWADY", "MAGWAY", "SAGAING", "TANINTHARYI",
        "KACHIN", "KAYAH", "KAYIN", "CHIN", "MON", "RAKHINE", "SHAN", "NAYPYIDAW",
        "WA REGION", "KOKANG", "PALAUNG", "PA-O", "DANU", "NAGA"
    ]
    print(f"\n🚀 Full Myanmar Scanning for: {name}...")
    for region in regions:
        print(f"📡 Checking News & Data in {region}...")
        query = f'"{name}" {phone} {nrc} {region}'
        url = f"https://www.google.com/search?q={query}"
        print(f"✅ Result for {region}: {url}\n")
        time.sleep(0.2)
    input("\nFull Search Finished. Press Enter...")

def main():
    while True:
        menu()
        choice = input("SELECT SEARCH TYPE: ")
        if choice == '0': break

        if choice == '1':
            name = input("🔍 Name: ").upper()
            city = input("📍 City: ").upper()
            url = f"https://www.google.com/search?q=site:facebook.com OR site:tiktok.com \"{name}\" {city}"
            print(f"✅ Social Link: {url}")
            input("\nPress Enter...")

        elif choice == '2':
            nrc = input("🆔 NRC: ").upper()
            url = f"https://www.google.com/search?q=\"{nrc}\" OR filetype:pdf \"{nrc}\""
            print(f"✅ NRC Data: {url}")
            input("\nPress Enter...")

        elif choice == '3':
            phone = input("📱 Phone: ")
            url = f"https://www.google.com/search?q=\"{phone}\" OR \"09 {phone[2:]}\""
            print(f"✅ Phone Data: {url}")
            input("\nPress Enter...")

        elif choice == '4':
            name = input("🔍 Name: ").upper()
            phone = input("📱 Phone: ")
            nrc = input("🆔 NRC: ").upper()
            city = input("📍 City: ").upper()
            run_full_search(name, phone, nrc, city)

        else:
            print("❌ Invalid Choice!")
            time.sleep(1)

if __name__ == "__main__":
    main()
