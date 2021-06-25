import pyfiglet
import os
import glob
import getpass
import subprocess
import time
from pathlib import Path
from colorama import init
from colorama import Fore, Back, Style
init(convert=True)
heartbeateffect = 0
def AcceptNetworkConnection():
     netsh = subprocess.Popen("netsh interface set interface "+ '"' + MainNetworkInterface +'"' +" ENABLED", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
     output =  netsh.communicate()
def DropNetworkConnection():
     netsh = subprocess.Popen("netsh interface set interface "+ '"' + MainNetworkInterface +'"' +" DISABLED", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
     output =  netsh.communicate()
while(1):
    ascii_banner = pyfiglet.figlet_format("Virtuosus")
    print(Fore.LIGHTBLUE_EX + ascii_banner)
    print(Fore.LIGHTMAGENTA_EX + "~Log-based OpenVPN Killswitch // Created by Nemesis0U \n \n")
    print(Fore.LIGHTWHITE_EX)
    try:
           with open('DefaultNetworkInterface.txt') as f:
              data = f.readlines()
           f.close()
           MainNetworkInterface = ''.join(data)
           AcceptNetworkConnection()
           print(Fore.LIGHTYELLOW_EX ,"Selected network interface: " , MainNetworkInterface)
           print(Fore.LIGHTWHITE_EX)
    except:
          createfile = open("DefaultNetworkInterface.txt", "a")
          print(Fore.LIGHTYELLOW_EX)
          os.system("netsh interface show interface")
          print(Fore.LIGHTCYAN_EX,"Enter the network interface that connects you to the internet(not VPN's interface)\n")
          MainNetworkInterface = input("Network Interface Name: ")
          createfile.truncate(0)
          createfile.writelines(MainNetworkInterface)
          createfile.close()
          AcceptNetworkConnection()
          os.system('cls' if os.name == 'nt' else 'clear')
          ascii_banner = pyfiglet.figlet_format("Virtuosus")
          print(Fore.LIGHTBLUE_EX + ascii_banner)
          print(Fore.LIGHTMAGENTA_EX + "~Log-based OpenVPN Killswitch // Created by Nemesis0U \n \n")
          print(Fore.LIGHTYELLOW_EX ,"Selected network interface: " , MainNetworkInterface)
          print(Fore.LIGHTWHITE_EX)
    print("Please enter your log file path of vpn you are using\n")
    username = str(getpass.getuser())
    slash = "\\"
    logdirectory = (r"C:\Users" + slash + username + slash + "OpenVPN\log" + slash)
    availablefiles = '\n'.join(glob.glob(logdirectory + "*.log"))
    print("Using default directory:" , logdirectory)
    print("\nAvailable log files: \n \n", availablefiles , "\n\n")
    OpenVPNLogfilePath = input("Log File of your VPN: ")
    OpenVPNLogfilePath = OpenVPNLogfilePath.replace("\\\\","\\")
    try:
        while(1):
                time.sleep(0.250)
                with open(OpenVPNLogfilePath) as f:
                    readlogfile = f.readlines()
                    f.close()
                data = ''.join(readlogfile)
                fopen = open(OpenVPNLogfilePath.replace("\\\\","\\"),mode='r')
                fread = fopen.readlines()
                for line in fread:
                    if "connection established with [AF_INET]" in line:
                        ConnectedServer = str(line.replace("connection established with [AF_INET]"," "))
                        ConnectedServer = ConnectedServer[20:]
                if("Connection reset, restarting" in data or "[soft,connection-reset] received, process restarting" in data or "Closing TUN/TAP interface" in data or "SIGUSR1[soft,server-pushed-connection-reset]" in data):
                       os.system('cls' if os.name == 'nt' else 'clear')
                       ascii_banner = pyfiglet.figlet_format("Virtuosus")
                       print(Fore.LIGHTBLUE_EX + ascii_banner)
                       print(Fore.LIGHTMAGENTA_EX + "~Log-based OpenVPN Killswitch // Created by Nemesis0U \n \n")
                       print(Fore.WHITE)
                       print("VPN Name: ", Path(OpenVPNLogfilePath).stem)
                       print("\nConnected Server: ", ConnectedServer)
                       print(Fore.LIGHTRED_EX, "VPN Heartbeat: Dead ____")
                       DropNetworkConnection()
                       warning = input("Your network connection has been blocked, restart the killswitch or enable your network interface manually in order to get it back.")
                       exit()
                elif("Initialization Sequence Completed" in data):
                       os.system('cls' if os.name == 'nt' else 'clear')
                       ascii_banner = pyfiglet.figlet_format("Virtuosus")
                       print(Fore.LIGHTBLUE_EX + ascii_banner)
                       print(Fore.LIGHTMAGENTA_EX + "~Log-based OpenVPN Killswitch // Created by Nemesis0U \n \n")
                       print(Fore.WHITE)
                       print("VPN Name: ", Path(OpenVPNLogfilePath).stem)
                       print("\nConnected Server: ", ConnectedServer)
                       if(heartbeateffect == 0):
                           heartbeateffect = 1
                           print(Fore.LIGHTGREEN_EX, "VPN Heartbeat: Alive _____")
                       elif(heartbeateffect == 1):
                           heartbeateffect = 2
                           print(Fore.LIGHTGREEN_EX, "VPN Heartbeat: Alive _/\___")
                       elif(heartbeateffect == 2):
                           heartbeateffect = 0
                           print(Fore.LIGHTGREEN_EX, "VPN Heartbeat: Alive ___/\_")
    except Exception as e:
        print(e)
    wait = input("Press any key to continue")
    os.system('cls' if os.name == 'nt' else 'clear')