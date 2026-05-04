import os
import sys
import time

# စာသားအရောင်များ (ပိုလန်းအောင်လို့ပါ)
R = '\033[31m' # အနီ
G = '\033[32m' # အစိမ်း
Y = '\033[33m' # အဝါ
W = '\033[0m'  # အဖြူ

def banner():
    os.system('clear')
    print(f"""
{G}###########################################
#                                         #
#      WELCOME TO [EdyHacker] TOOL      #
#      -----------------------------      #
#   Created by: EdyHacker                 #
#   Version   : 1.0                       #
#                                         #
###########################################{W}
    """)

def menu():
    print(f"{Y}[1]{W} Bypass Link (နမူနာ)")
    print(f"{Y}[2]{W} Web Scanner (နမူနာ)")
    print(f"{Y}[3]{W} Tool ကို ပိတ်ရန်")
    print("")

def start_bypass():
    target = input(f"{G}[+]{W} Target Link ကို ထည့်ပါ: ")
    print(f"{Y}[*]{W} {target} ကို စတင်စစ်ဆေးနေပါပြီ...")
    # ဒီနေရာမှာ တကယ့် bypass code တွေ ထည့်ရမှာပါ
    time.sleep(3)
    print(f"{G}[√]{W} လုပ်ဆောင်ချက် ပြီးမြောက်ပါပြီ။")

def main():
    while True:
        banner()
        menu()
        choice = input(f"{G}ရွေးချယ်မှုအမှတ်စဉ်နှိပ်ပါ >> {W}")
        
        if choice == '1':
            start_bypass()
            input("\nဆက်သွားရန် Enter ခေါက်ပါ...")
        elif choice == '2':
            print(f"{Y}[*]{W} Scanner စတင်နေပါပြီ...")
            time.sleep(2)
            input("\nဆက်သွားရန် Enter ခေါက်ပါ...")
        elif choice == '3':
            print(f"{R}Tool ကို ပိတ်လိုက်ပါပြီ။ သာယာသောနေ့လေးဖြစ်ပါစေ!{W}")
            sys.exit()
        else:
            print(f"{R}မှားယွင်းနေပါသည်။ ပြန်ရွေးပေးပါ။{W}")
            time.sleep(1)

if __name__ == "__main__":
    main()
