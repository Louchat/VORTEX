import ctypes
import time
import shutil
import os
import subprocess
import urllib.request
import keyboard
import win32gui
import win32con
import sys
import webbrowser
from colorama import Fore, init

# Initialisation de colorama
init(autoreset=True)

# Vérifie si l'utilisateur a les droits administrateur
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Si pas administrateur, redémarre le script en mode administrateur
if not is_admin():
    print(Fore.RED + "Restarting as admin...")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

# Demande le nom d'utilisateur de Windows
os.system('title [LOCKED]:')
useer = input("The program is locked, Please enter your Windows username: ").strip()

os.system('title [UNLOCKED]                                                                          // WE LOVE CHEATING //') #Renome la fenetre par // WE LOVE CHEATING //

def disconnect_second_screen():
    print(Fore.YELLOW + "Disconnecting second screen...")
    subprocess.run(['DisplaySwitch.exe', '/external'])  # Cela bascule l'affichage sur un seul écran (l'écran principal)
    print(Fore.GREEN + "Second screen disconnected.")


def reconnect_second_screen():
    print(Fore.YELLOW + "Reconnecting second screen...")
    subprocess.run(['DisplaySwitch.exe', '/extend'])  # Basculer en mode étendu (pour utiliser les deux écrans)
    print(Fore.GREEN + "Second screen reconnected in extended mode.")

def manage_second_screen():
    while True:
        print(Fore.GREEN + "What do you want to do with the second screen?")
        print(Fore.YELLOW + "1: Disconnect second screen")
        print(Fore.YELLOW + "2: Reconnect second screen")
        print(Fore.YELLOW + "3: Back to main menu")

        choice = input(Fore.CYAN + "Enter your choice (1-3): ")

        if choice == '1':
            disconnect_second_screen()  # Fonction pour déconnecter le second écran
            break  # Retour au menu principal après l'action
        elif choice == '2':
            reconnect_second_screen()  # Fonction pour reconnecter le second écran
            break  # Retour au menu principal après l'action
        elif choice == '3':
            print(Fore.YELLOW + "Going back to main menu...\n")
            break  # Retour au menu principal
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

def clean_disk():  # Nettoyage du dossier TEMP sans l'outil Disk Cleanup
    temp_dir = os.getenv('TEMP')  # Récupère le chemin du dossier TEMP
    print(Fore.YELLOW + f"Cleaning files in {temp_dir}...")

    try:
        # Supprimer tous les fichiers et dossiers dans le dossier %TEMP%
        for root, dirs, files in os.walk(temp_dir, topdown=False):
            for name in files:
                try:
                    file_path = os.path.join(root, name)
                    os.remove(file_path)
                except Exception as e:
                    print(Fore.RED + f"Error deleting file {file_path}: {e}")
            for name in dirs:
                try:
                    dir_path = os.path.join(root, name)
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(Fore.RED + f"Error deleting directory {dir_path}: {e}")

        print(Fore.GREEN + "Temporary files deleted successfully.")

    except Exception as e:
        print(Fore.RED + f"An error occurred while cleaning TEMP files: {e}")


# Fonction pour régler l'opacité de la fenêtre de la console
def set_opacity(opacity):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    alpha = int(255 * (opacity / 100))
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, 0x00000002)

# Fonction pour cacher la fenêtre et attendre la réactivation
def wait_for_reactivation():

    hwnd = ctypes.windll.kernel32.GetConsoleWindow()

    # Cacher la fenêtre au lieu de la minimiser
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

    print(Fore.CYAN + "\n[!] Program is now running in the background. Press '/' to reopen the menu.")
    while True:
        if keyboard.is_pressed('/'):
            # Restaurer la fenêtre
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.GREEN + "Reopening launcher...")
            time.sleep(0.5)
            return
        time.sleep(0.1)

# Fonction pour trouver le chemin de Discord
def find_discord_exe(useer):
    base_path = fr"C:\Users\{useer}\AppData\Local\Discord"
    for folder in os.listdir(base_path):
        if folder.startswith("app-"):
            path = os.path.join(base_path, folder, "Discord.exe")
            if os.path.isfile(path):
                return path
    return None

# Fonction pour télécharger et installer une application
def install_app(app_name):
    apps = {
        "chrome": {
            "url": "https://dl.google.com/chrome/install/375.126/chrome_installer.exe",
            "file": "chrome_installer.exe"
        },
        "opera": {
            "url": "https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes",
            "file": "OperaSetup.exe"
        },
        "roblox": {
            "url": "https://www.roblox.com/fr/download/client?os=win",
            "file": "RobloxPlayerInstaller.exe"
        },
        "bloxstrap": {
            "url": "https://github.com/bloxstraplabs/bloxstrap/releases/download/v2.9.0/Bloxstrap-v2.9.0.exe",
            "file": "Bloxstrap-v2.9.0.exe"
        }
    }

    if app_name in apps:
        data = apps[app_name]
        print(Fore.CYAN + f"Downloading {app_name} installer...")
        urllib.request.urlretrieve(data["url"], data["file"])
        print(Fore.CYAN + "Download complete!")

        print(Fore.CYAN + "Running the installer...")
        subprocess.run([data["file"]])

        os.remove(data["file"])
        print(Fore.CYAN + "Installer removed after installation.")
    else:
        print(Fore.RED + "Unknown app.")

# Réglage de l'opacité de la fenêtre
set_opacity(72)
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.MAGENTA + "// DEVELOPPED BY LOUCHATFLUFF //")
time.sleep(3)
print(Fore.RED + "THIS SOFTWARE IS FREE, IF YOU PAYED FOR IT: PLEASE RETURN IT")
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')

# Menu principal
def main_menu():
    while True:
        print(Fore.GREEN + "What do u want to do:")
        print(Fore.YELLOW + "1: Open apps")
        print(Fore.YELLOW + "2: Optimise")
        print(Fore.YELLOW + "3: Install Apps")
        print(Fore.YELLOW + "4: Minimise")
        print(Fore.YELLOW + "5: Ping")
        print(Fore.YELLOW + "6: Manage second screen")
        print(Fore.RED + "7: Close")

        main_choice = input(Fore.CYAN + "Enter your choice (1-6): ")

        
        
        if main_choice == '6':  # Option pour déconnecter le second écran
            manage_second_screen()

        elif main_choice == '1':
            # Menu pour ouvrir des apps
            while True:
                print(Fore.YELLOW + "\nChoose an app to open:")
                print(Fore.CYAN + "1: Riot")
                print(Fore.CYAN + "2: Bloxstrap")
                print(Fore.CYAN + "3: Spotify")
                print(Fore.CYAN + "4: Discord")
                print(Fore.CYAN + "5: Lunar Client")
                print(Fore.CYAN + "6: Opera")
                print(Fore.CYAN + "7: Chrome")
                print(Fore.YELLOW + "8: Menu")

                choice = input(Fore.CYAN + "Enter your choice (1-8): ")

                apps = {
                    '1': r"C:\Riot Games\Riot Client\RiotClientServices.exe",
                    '2': fr"C:\Users\{useer}\Documents\Bloxstrap-v2.9.0",
                    '3': fr"C:\Users\{useer}\AppData\Roaming\Spotify\Spotify.exe",
                    '5': fr"C:\Users\{useer}\AppData\Local\Programs\Lunar Client\Lunar Client.exe",
                    '6': fr"C:\Users\{useer}\AppData\Local\Programs\Opera\opera.exe",
                    '7': fr"C:\Users\{useer}\AppData\Local\Programs\Google\Chrome\Application\chrome.exe",
                }

                if choice == '4':
                    # Ouvre Discord
                    discord_path = find_discord_exe(useer)
                    if discord_path:
                        print(Fore.GREEN + "Opening Discord...")
                        subprocess.Popen([discord_path])
                    else:
                        print(Fore.RED + "Discord not found.")
                elif choice in apps:
                    print(Fore.GREEN + f"Opening app {choice}...")
                    subprocess.Popen([apps[choice]])
                elif choice == '8':
                    print(Fore.YELLOW + "Going back to main menu...\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print(Fore.RED + "Invalid choice.")

        elif main_choice == '7':
            print(Fore.RED + "Closing the program...")
            os.system('cls')  # Vider l'écran (facultatif)
            sys.exit()

        elif main_choice == '2':
            # Optimisation des apps
            print(Fore.GREEN + "Optimising your system...")
            clean_disk()
            processes = ["steam.exe", "opera.exe", "sunshine.exe", "sunshinesvc.exe", "Spotify.exe", "discord.exe"]

            for proc in processes:
                print(Fore.CYAN + f"Trying to close {proc}...")
                exit_code = os.system(f"taskkill /f /im {proc}")
                if exit_code != 0:
                    print(Fore.RED + f"[FAIL] Failed to close {proc}. Maybe try running this script as administrator.")
                else:
                    print(Fore.GREEN + f"[OK] {proc} closed successfully.")
                time.sleep(0.5)

            print(Fore.GREEN + "Done.\n")
            print(Fore.YELLOW + "Press Enter to continue...")
            keyboard.read_event()  # Attend une touche pour continuer, après l'optimisation

            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_choice == '3':
            # Menu pour installer des apps
            print(Fore.YELLOW + "Choose an app to install:")
            print(Fore.CYAN + "1: Google Chrome")
            print(Fore.CYAN + "2: Opera Browser")
            print(Fore.CYAN + "3: Roblox Player")
            print(Fore.CYAN + "4: Bloxstrap")
            install_choice = input(Fore.CYAN + "Enter your choice (1-4): ")
            apps_map = {'1': 'chrome', '2': 'opera', '3': 'roblox', '4': 'bloxstrap'}
            install_app(apps_map.get(install_choice, ''))

        elif main_choice == '4':
            # Minimise le programme
            wait_for_reactivation()


        elif main_choice == '9':
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_choice == '5':  # Option "Ping"
            print(Fore.YELLOW + "Enter the website URL you want to visit:")
            website = input(Fore.CYAN + "Enter URL (example: https://www.google.com): ").strip()

            # Ouvrir le site web dans le navigateur par défaut
            if website:
                print(Fore.GREEN + f"Opening website: {website}")
                webbrowser.open(website)
            else:
                print(Fore.RED + "Invalid URL. Please try again.")

        else:
            print(Fore.RED + "Invalid choice.")

# Lancer le menu principal
while True:
    main_menu()
