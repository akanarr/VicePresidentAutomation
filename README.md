# Vice President Automation For Last War
Python automated Vice President role for Last War

# Python Script Setup
The Python script must be started while in the captiol title screen and includes the added benefit of dismissing players after they have been in a role for 6+ minutes. However, setting up the script requires configuring screen coordinates to match your specific system. A helper script, mouseCords.py, has been added to help you find the x, y coordinates of your setup. 

# Install python and the package reqirements

Install Python 3.12.7

  1. download and unzip the repo
  2. run the following command:
     pip install -r requirements.txt


# How to Find Screen Coordinates

mouseCoords.py
This script prints the current cursor position every 3 seconds. Use it to find the coordinates of specific screen elements:

python .\mouseCoords.py

hit ctrl + C to cancel

# Run Automation Script

_Note: make sure you edit the automation script to include the coordinates that match your setup. _

python .\vicePresidentAutomation.py

hit control + C to cancel
