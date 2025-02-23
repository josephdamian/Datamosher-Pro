#Automatic Setup for Datamosher-Pro
#Author: Akash Bora

#Importing some built in modules
import subprocess
import sys
import time
import os
from zipfile import ZipFile

try:
    import pkg_resources
except ImportError:
    if sys.platform.startswith("win"):
        subprocess.call('python -m pip install setuptools', shell=True)
    else:
        subprocess.call('python3 -m pip install setuptools', shell=True)
    import pkg_resources
    
DIRPATH = os.path.dirname(os.path.realpath(__file__))

#Checking the required folders
folders= ["Assets","FFglitch","DatamoshLib","pymosh"]
missingfolder=[]
for i in folders:
    if not os.path.exists(i):
        missingfolder.append(i)
if missingfolder:
    print("These folder(s) not available: "+str(missingfolder))
    print("Download them from the repository properly")
    sys.exit()
else:
    print("All folders available!")

#Checking required modules
required = {'imageio', 'imageio-ffmpeg', 'numpy', 'customtkinter', 'pillow', 'requests', 'packaging'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
missingset=[*missing,]

#Download the modules if not installed
if missing:
    res = input("Some modules are not installed... \n do you want to download and install them now? (Y/N): ")
    while not ((res=="Y") or (res=="y") or (res=="N") or (res=="n")):
        print("Please choose a valid option!")
        res = input("Some modules are not installed... \n do you want to download and install them now? (Y/N): ")
    if res=="Y" or res=="y":
        try:
            print("Installing modules...")
            for x in range(len(missingset)):
                y=missingset[x]
                if sys.platform.startswith("win"):
                    subprocess.call('python -m pip install '+y, shell=True)
                else:
                    subprocess.call('python3 -m pip install '+y, shell=True)
        except:
            print("Unable to download! \nThis are the required ones: "+str(required)+"\nUse 'pip install module_name' to download the modules one by one.")
            time.sleep(3)
            sys.exit()
    elif res=="N" or res=="n":
        print("Without the modules you can't open this program. Please install them first! \nThis are the required one: "+str(required)
              +"\nUse 'pip install module_name' to download modules one by one manually.")
        time.sleep(3)
        sys.exit()       
else:
    print("All required modules installed!")

#Check FFglitch Status
def checkffglitch():
    print("Checking FFglitch:")
    print("Running ffgac...")
    ffgac = os.path.join(DIRPATH,"FFglitch","ffgac")
    ffedit = os.path.join(DIRPATH,"FFglitch","ffedit")
  
    try:
        subprocess.Popen(f'"{ffgac}" -version', shell=True)
    except:
        print("permission denied! Please give permission to ffgac!")
        
    time.sleep(1)
    print("Running ffedit...")
    try: 
        subprocess.Popen(f'"{ffedit}" -version', shell=True)
    except:
        print("permission denied! Please give permission to ffedit!")
    time.sleep(1)
    print("Done...")
    
#Download ffglitch if not available
if (os.path.exists(os.path.join("FFglitch","ffgac")) or
    os.path.exists(os.path.join("FFglitch","ffgac.exe"))) and (os.path.exists(os.path.join("FFglitch","ffedit"))
                                                               or os.path.exists(os.path.join("FFglitch","ffedit.exe"))):
    checkffglitch()
else:
    print("ffgac/ffedit not found inside ffglitch folder, you cannot run the ffglitch modes without these programs")
    res2 = input("Do you want to download ffglitch modes? (Y/N): ")
    while not ((res2=="Y") or (res2=="y") or (res2=="N") or (res2=="n")):
        print("Please choose a valid option!")
        res2 = input("Do you want to download ffglitch now? (Y/N): ")
        
    if res2=="Y" or res2=="y":
        print("Downloading FFglitch... (size: approx 17MB)")
        if sys.platform.startswith("win"): #download ffglitch for windows
            URL = "https://github.com/Akascape/FFglitch-0.9.3-executables/releases/download/zip-packages/ffglitch-0.9.3-win64.zip"
        elif sys.platform.startswith("linux"): #download ffglitch for linux
            URL = "https://github.com/Akascape/FFglitch-0.9.3-executables/releases/download/zip-packages/ffglitch-0.9.3-linux64.zip"
        else: #download ffglitch for mac
            URL = "https://github.com/Akascape/FFglitch-0.9.3-executables/releases/download/zip-packages/ffglitch-0.9.3-mac64.zip"
        try:
            try:
                import requests
                response = requests.get(URL)
                open(os.path.join("FFglitch","ffglitch.zip"), "wb").write(response.content)
            except:
                print("Unable to download ffglitch from site, try again running this setup!")
                print("Check your connection or download it manually from: | https://github.com/Akascape/FFglitch-0.9.3-executables |")
                print("Paste the files (ffgac and ffedit) inside FFglitch folder.")
                time.sleep(3)
                sys.exit()
            time.sleep(1)
            print("Exctracting the files...")
            try:
                with ZipFile(os.path.join('FFglitch','ffglitch.zip'), 'r') as zip: 
                    zip.extractall('FFglitch/')
            except:
                print("Failed to extract ffglitch.zip, please extract it manually in the FFglitch folder.")
                time.sleep(3)
                sys.exit()
            if os.path.exists(os.path.join("FFglitch","ffgac")) or os.path.exists(os.path.join("FFglitch","ffgac.exe")):
                os.remove(os.path.join("FFglitch","ffglitch.zip"))
            time.sleep(1)
            checkffglitch()
            print("FFglitch setup complete!")
        except:
            print("Something went wrong!")
    elif res2=="N" or res2=="n":
        print("ffglitch modes cannot run without ffgac and ffedit packages, download them manually and paste them inside the FFglitch folder.")

#Everything done!
print("Setup Complete!")
time.sleep(5)
sys.exit()
