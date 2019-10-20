import subprocess

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
subprocess.call('mv ./idead.config ~/Applications/idead/idead.config', shell=True)

print("Moving launchd service to ~/Library/LaunchAgents/")
subprocess.call('cp ./System\ Configs/MacOS/xyz.idead.buttonwatch.plist ~/Library/LaunchAgents/xyz.idead.buttonwatch.plist', shell=True)
subprocess.call('cp ./System\ Configs/MacOS/xyz.idead.daemon.plist ~/Library/LaunchAgents/xyz.idead.daemon.plist', shell=True)

print("Loading up Launchd Agents")
subprocess.call('launchctl load ~/Library/LaunchAgents/xyz.idead.buttonwatch.plist', shell=True)
subprocess.call('launchctl load ~/Library/LaunchAgents/xyz.idead.daemon.plist', shell=True)

print("Moving scripts to ~/Applications/idead/")
subprocess.call('cp ./System\ Configs/idead.sh ~/Applications/idead/', shell=True)
subprocess.call('cp ./System\ Configs/idead_button_press.sh ~/Applications/idead/', shell=True)

print("Installing dependencies")
subprocess.call(f"echo {digital_ocean_api_key} | brew install doctl", shell=True)
subprocess.call(f"pip install --user pyserial", shell=True)