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

To find the correct coordinates for each title. the values are (left, top, width, height) of the timer region per title card. 

left == x coordinate  
top == y coordinate  
width == pixel distance to the right of the x coordinate  
height == pixel distance below the y coordinate.  

In this picture you if you put the mouseCoords.py value of your cursor in the top left you will have your x,y coordinates. Bottom right minus your x, y coordinates will give you width and height. 

![image](https://github.com/user-attachments/assets/5c7e9bb8-db74-404f-8e2b-f3e77bf77aba)

otherwise you just need the x, y coordinates of each click action. 

# Run Automation Script

_Note: make sure you edit the automation script to include the coordinates that match your setup. _

python .\vicePresidentAutomation.py

hit control + C to cancel
