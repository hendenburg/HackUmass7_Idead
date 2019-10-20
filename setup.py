import subprocess
from datetime import date
from datetime import time
from datetime import datetime

to_upload = 'true'
paths = ""
digital_ocean_api_key = ""

print("Configuring IDead:")

question = input("\nDo you wish to delete or upload your files to a Digital Ocean VM in the case of your death: [Y] for upload, n to not: ")
if question is 'n' or question is 'N':
    to_upload = 'false'

paths = input("\nPlease provide a list of full file paths seperated by a colon, i.e. /usr/bin/:/etc/httdp: ")

digital_ocean_api_key = input("\nIf you have not created a digital ocean account already, please do so. Enter your API key here: ")

print("\nAssembling config file")
config = open("idead.config","w+")
config.write(f"to_upload={to_upload}\n")
config.write(f"paths={paths}\n")

print("Moving config file to ~Applications/idead/idead.config")
subprocess.call('mkdir ~/Applications/idead', shell=True)
subprocess.call('\mv ./idead.config ~/Applications/idead/idead.config', shell=True)

print("Moving launchd service to ~/Library/LaunchAgents/")
subprocess.call('chmod 664 ~/Library/LaunchAgents/xyz*', shell=True)
subprocess.call('\cp SystemConfigs/MacOS/xyz.idead.buttonwatch.plist ~/Library/LaunchAgents/xyz.idead.buttonwatch.plist', shell=True)
subprocess.call('\cp SystemConfigs/MacOS/xyz.idead.daemon.plist ~/Library/LaunchAgents/xyz.idead.daemon.plist', shell=True)

print("Loading up Launchd Agents")
subprocess.call('launchctl unload ~/Library/LaunchAgents/xyz.idead.buttonwatch.plist', shell=True)
subprocess.call('launchctl unload ~/Library/LaunchAgents/xyz.idead.daemon.plist', shell=True)
subprocess.call('launchctl load ~/Library/LaunchAgents/xyz.idead.buttonwatch.plist', shell=True)
subprocess.call('launchctl load ~/Library/LaunchAgents/xyz.idead.daemon.plist', shell=True)

print("Creating log file")
subprocess.call('touch idead.log', shell=True)
subprocess.call('chmod 777 idead.log', shell=True)
log = open("idead.log","a+")
now = datetime.now()
log.write("\n%s: System Initialized" % now.strftime("%c"))
subprocess.call('\mv idead.log ~/Applications/idead/idead.log', shell=True)


print("Moving scripts to ~/Applications/idead/")
subprocess.call('\cp SystemConfigs/idead_file_upload.py ~/Applications/idead/', shell=True)
subprocess.call('\cp SystemConfigs/idead_serial_monitor.py ~/Applications/idead/', shell=True)

print("Installing dependencies")
subprocess.call(f"echo {digital_ocean_api_key} | brew install doctl", shell=True)
subprocess.call(f"pip install --user pyserial", shell=True)