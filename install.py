### MADE BY ROOTWW https://github.com/r00tww/dots

# Import some libraries
import os, shutil, subprocess, sys

# These are required apps. This script is checking these executables.
APPS = ["i3", "unzip", "brave", "i3blocks", "alacritty", "nitrogen", "picom", "rofi", "spectacle"]

# These are .config directories. They're exist in project folder, script is copying these to your ~/.config directory.
DIRS = ["i3", "i3blocks", "alacritty", "rofi"]

# Only for project admin.
def initdirectories():
    for dir_name in DIRS:
        source_dir = os.path.expanduser(f"~/.config/{dir_name}")
        if os.path.isdir(source_dir):
            shutil.copytree(source_dir, dir_name, dirs_exist_ok=True)
            print(f"{source_dir} copied to {os.getcwd()}/{dir_name}.")
        else:
            print(f"{source_dir} does not exist, skipping.")

# Check programs
def checkprograms():
    print("* MISSING PROGRAMS")
    missing = False

    for app in APPS:
        if shutil.which(app) is None:
            print(f"{app} is not installed.")
            missing = True

    if missing:
        print("Some programs are missing. Please install them.")
        sys.exit(1)
    else:
        print("No missing programs found.")

# Copy files
def copyfiles():
    print("* COPYING FILES")

    for dir_name in DIRS:
        if os.path.isdir(dir_name):
            dest_dir = os.path.expanduser(f"~/.config/{dir_name}")
            shutil.copytree(dir_name, dest_dir, dirs_exist_ok=True)
            print(f"INFO: {dir_name} copied successfully.")
        else:
            print(f"{dir_name} does not exist, skipping.")


def installfonts():
    print("* JETBRAINSMONO FONT IS INSTALLING")
    url = "https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh"
    subprocess.run(["bash", "-c", f"curl -fsSL {url} | bash"], check=True)
def main():
    if len(sys.argv) > 1 and sys.argv[1] == "i":
        initdirectories()
    else:
        checkprograms()
        copyfiles()
        installfonts()

if __name__ == "__main__":
    main()