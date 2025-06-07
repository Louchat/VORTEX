# ==============================================================
# VORTEX - Custom Launcher Utility
# Developed by Louchatfluff
# Open-source on GitHub: https://github.com/Louchat/VORTEX
# ==============================================================

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
import getpass
import requests
from colorama import Fore, init

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize colorama
init(autoreset=True)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print(Fore.RED + "Restarting as admin...")
    params = ' '.join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, params, None, 1)
    sys.exit()


# Ask for the Windows username
os.system('title [LOCKED]:')
useer = os.getlogin()
def verify_user():
    user = getpass.getuser()
    print(Fore.GREEN + f"User found: {user}")
    print(Fore.YELLOW + "Is it correct?")
    print("1. Yes (unlock automatically)")
    print("2. No (unlock manually)")

    choice = input(Fore.RED + "Enter your choice (1/2): ").strip()

    while choice not in ["1", "2"]:
        choice = input("Invalid input. Please enter 1 or 2: ").strip()

    if choice == "1":
        print("Unlocking automatically...")
        time.sleep(1)  # Optional visual delay
        return user
    else:
        manual_user = input("Enter your username manually: ").strip()
        print(f"Manual unlock for user: {manual_user}")
        return manual_user

# Example usage :
current_user = verify_user()



os.system('title [UNLOCKED]                                                                          // WE LOVE CHEATING //') #Renome la fenetre par // WE LOVE CHEATING //


def get_github_version():
    try:
        url = "https://raw.githubusercontent.com/Louchat/VORTEX/main/version.txt"
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(Fore.RED + f"Error fetching GitHub version: {e}")
        return None


def get_latest_commit_date():
    # GitHub API to get the latest commit on the VORTEX.py file
    api_url = "https://api.github.com/repos/Louchat/VORTEX/commits?path=VORTEX.py&page=1&per_page=1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        if data:
            commit_date = data[0]['commit']['committer']['date']
            # Simple formatting, e.g. 2025-06-07T12:34:56Z -> 2025-06-07
            return commit_date.split("T")[0]
        else:
            return None
    except Exception as e:
        print(f"Error retrieving update date: {e}")
        return None


def update_vortex():
    repo_url = "https://raw.githubusercontent.com/Louchat/VORTEX/main/VORTEX.py"
    
    # Get the current script's directory (VORTEX.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create Update_Vortex folder if not exist
    update_folder = os.path.join(current_dir, "Update_Vortex")
    if not os.path.exists(update_folder):
        os.makedirs(update_folder)
    
    # Full path of the downloaded update file
    local_file = os.path.join(update_folder, "VORTEX.py")
    
    choice = input("Do you want to install the latest version of VORTEX? (y/n): ").strip().lower()
    if choice != 'y':
        print("Update cancelled.")
        return
    
    try:
        print("Downloading the latest version...")
        response = requests.get(repo_url)
        response.raise_for_status()
        
        with open(local_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Update successfully downloaded in: {local_file}")
        print("Restart the program to apply changes.")
    except Exception as e:
        print(f"Error during update: {e}")

def show_version_and_update():
    version = "9.5"  # Local version
    print(f"Current VORTEX version: {version}")

    

    last_update = get_latest_commit_date()
    if last_update:
        print(f"Last GitHub update date: {last_update}")
    else:
        print("Unable to retrieve last update date.")
    github_version = get_github_version()
    if github_version:
        print(f"Latest version on GitHub: {github_version}")
        if github_version != version:
            print(Fore.YELLOW + "An update is available!")
        else:
            print(Fore.GREEN + "You are up to date.")
    else:
        print(Fore.RED + "Could not check for the latest version.")
    update_vortex()



def execute_command():
    while True:
        print(Fore.YELLOW + "Enter the CMD command you want to execute:")
        cmd = input(Fore.CYAN + "> ")
        if cmd.lower() == 'exit':
            print(Fore.YELLOW + "Returning to main menu...\n")
            break
        if cmd.strip() == "":
            continue
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.stdout:
                print(Fore.GREEN + result.stdout)
            if result.stderr:
                print(Fore.RED + result.stderr)
            print(Fore.MAGENTA + "Command has been executed.")
        except Exception as e:
            print(Fore.RED + f"Error executing command: {e}")

        # Proposer le choix entre exécuter une autre commande ou revenir au menu principal
        while True:
            print(Fore.YELLOW + "\nChoose an option:")
            print(Fore.YELLOW + "1: Execute another command")
            print(Fore.YELLOW + "2: Go back to the main menu")
            choice = input(Fore.CYAN + "> ").strip()
            if choice == '1':
                break  # Sort de la boucle interne et revient au début pour une nouvelle commande
            elif choice == '2':
                print(Fore.YELLOW + "Returning to main menu...\n")
                return  # Quitte la fonction pour revenir au menu principal
            else:
                print(Fore.RED + "Invalid option, please choose 1 or 2.")


def disconnect_second_screen():
    print(Fore.YELLOW + "Disconnecting second screen...")
    subprocess.run(['DisplaySwitch.exe', '/external'])  # switch to single screen (to optimise graphics)
    print(Fore.GREEN + "Second screen disconnected.")


def reconnect_second_screen():
    print(Fore.YELLOW + "Reconnecting second screen...")
    subprocess.run(['DisplaySwitch.exe', '/extend'])  # switch to extended (to use both screens)
    print(Fore.GREEN + "Second screen reconnected in extended mode.")

def manage_second_screen():
    while True:
        print(Fore.GREEN + "What do you want to do with the second screen?")
        print(Fore.YELLOW + "1: Disconnect second screen")
        print(Fore.YELLOW + "2: Reconnect second screen")
        print(Fore.YELLOW + "3: Back to main menu")

        choice = input(Fore.CYAN + "Enter your choice (1-3): ")

        if choice == '1':
            disconnect_second_screen()  # Fonction that disconect second screen
            break  # Return to main menu after the action
        elif choice == '2':
            reconnect_second_screen()  # Fonction that reconect second screen
            break  # Return to main menu after the action
        elif choice == '3':
            print(Fore.YELLOW + "Going back to main menu...\n")
            break  # Retour au menu principal
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

def clean_disk():  # Clean TEMP folder without using Disk Cleanup
    temp_dir = os.getenv('TEMP')  # Get TEMP folder path
    print(Fore.YELLOW + f"Cleaning files in {temp_dir}...")

    try:
        # Delete all files and folders in the TEMP directory %TEMP%
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
        
        # Kill explorer.exe process using taskkill
        print(Fore.YELLOW + "Killing explorer.exe process...")
        subprocess.run("taskkill /f /im explorer.exe", shell=True)
        print(Fore.GREEN + "Explorer.exe has been terminated.")

    except Exception as e:
        print(Fore.RED + f"An error occurred while cleaning TEMP files: {e}")


# Function to set console window opacity
def set_opacity(opacity):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    alpha = int(255 * (opacity / 100))
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, 0x00000002)

# Function to hide the console and wait for reactivation
def wait_for_reactivation():

    hwnd = ctypes.windll.kernel32.GetConsoleWindow()

    # Hide window instead of minimizing
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

    print(Fore.CYAN + "\n[!] Program is now running in the background. Press '/' to reopen the menu.")
    while True:
        if keyboard.is_pressed('/'):
            # Restore the window
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            clear_console()
            print(Fore.GREEN + "Reopening launcher...")
            time.sleep(0.5)
            return
        time.sleep(0.1)

# Function to find Discord executable path
def find_discord_exe(useer):
    base_path = fr"C:\Users\{useer}\AppData\Local\Discord"
    for folder in os.listdir(base_path):
        if folder.startswith("app-"):
            path = os.path.join(base_path, folder, "Discord.exe")
            if os.path.isfile(path):
                return path
    return None

# Function to download and install an application
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
        },
        "Deezer":{
            "url": "https://www.deezer.com/desktop/download?platform=win32&architecture=x86",
            "file": "DeezerDesktopSetup_7.0.60.exe"
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

# Set window opacity
set_opacity(72)
clear_console()
print(Fore.MAGENTA + "// DEVELOPPED BY LOUCHATFLUFF //")
time.sleep(3)
print(Fore.RED + "THIS SOFTWARE IS FREE, IF YOU PAYED FOR IT: PLEASE RETURN IT")
time.sleep(5)
clear_console()
# Main menu
def main_menu():
    while True:
        print(Fore.GREEN + "What do u want to do:")
        print(Fore.YELLOW + "1: Open apps")
        print(Fore.YELLOW + "2: Optimise")
        print(Fore.YELLOW + "3: Install Apps")
        print(Fore.YELLOW + "4: Minimise")
        print(Fore.YELLOW + "5: Ping")
        print(Fore.YELLOW + "6: Manage second screen")
        print(Fore.YELLOW + "7: Execute CMD command")
        print(Fore.YELLOW + "8: Check latest github update")
        print(Fore.RED + "9: Close")
                

        main_choice = input(Fore.CYAN + "Enter your choice (1-8): ")

        
        
        if main_choice == '6':  # Option to disconnect second screen
            manage_second_screen()

        elif main_choice == '1':
            # Menu to open apps
            while True:
                print(Fore.YELLOW + "\nChoose an app to open:")
                print(Fore.CYAN + "1: Riot")
                print(Fore.CYAN + "2: Bloxstrap")
                print(Fore.CYAN + "3: Spotify")
                print(Fore.CYAN + "4: Discord")
                print(Fore.CYAN + "5: Lunar Client")
                print(Fore.CYAN + "6: Opera")
                print(Fore.CYAN + "7: Chrome")
                print(Fore.CYAN + "8: Deezer")
                print(Fore.YELLOW + "9: Menu")
                

                choice = input(Fore.CYAN + "Enter your choice (1-9): ")

                apps = {
                    '1': r"C:\Riot Games\Riot Client\RiotClientServices.exe",
                    '2': fr"C:\Users\{useer}\Documents\Bloxstrap-v2.9.0.exe",
                    '3': fr"C:\Users\{useer}\AppData\Roaming\Spotify\Spotify.exe",
                    '5': fr"C:\Users\{useer}\AppData\Local\Programs\Lunar Client\Lunar Client.exe",
                    '6': fr"C:\Users\{useer}\AppData\Local\Programs\Opera\opera.exe",
                    '7': fr"C:\Users\{useer}\AppData\Local\Programs\Google\Chrome\Application\chrome.exe",
                    '8': fr"C:\Users\{useer}\AppData\Local\Programs\deezer-desktop\Deezer.exe"
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

                elif choice == '9':                                                         #Fonction pr que le menu fonctione ce ptit FDP
                    print(Fore.YELLOW + "Going back to main menu...\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print(Fore.RED + "Invalid choice.")

        elif main_choice == '9':
            print(Fore.RED + "Closing the program...")
            os.system('cls')  # Clear screen (optional)
            sys.exit()

        elif main_choice == "7":    
            execute_command()

        elif main_choice == '2':
            # App optimization
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
            keyboard.read_event()  # Wait for user input before continuing

            clear_console()

        elif main_choice == '3':
            # Menu to install apps
            print(Fore.YELLOW + "Choose an app to install:")
            print(Fore.CYAN + "1: Google Chrome")
            print(Fore.CYAN + "2: Opera Browser")
            print(Fore.CYAN + "3: Roblox Player")
            print(Fore.CYAN + "4: Bloxstrap")
            print(Fore.CYAN + "5: Deezer")
            install_choice = input(Fore.CYAN + "Enter your choice (1-4): ")
            apps_map = {'1': 'chrome', '2': 'opera', '3': 'roblox', '4': 'bloxstrap','5': 'Deezer'}
            install_app(apps_map.get(install_choice, ''))

        elif main_choice == '4':
            # Minimize the program
            wait_for_reactivation()


        elif main_choice == 'admin.clear':
            clear_console()

        elif main_choice == 'admin':
            clear_console()
            print(Fore.RED + "You entered Admin commands tools:")
            print(Fore.MAGENTA + "Commands available:")
            print(" - admin.clear : clear the console")
            print(" - exit       : return to main menu")

            while True:
                cmd = input(Fore.CYAN + "admin> ").strip().lower()
                if cmd == 'admin.clear':
                    clear_console()
                elif cmd == 'exit':
                    clear_console()
                    break
                else:
                    print(Fore.YELLOW + f"Unknown command: {cmd}")

        elif main_choice == '8':
            clear_console()
            show_version_and_update()
            


        elif main_choice == '5':  # Ping option
            print(Fore.YELLOW + "Enter the website URL you want to visit:")
            website = input(Fore.CYAN + "Enter URL (example: https://www.google.com): ").strip()

            # Open the website in the default browser
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
