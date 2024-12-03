import pyautogui
import time
import re   
import pytesseract
from PIL import Image
import cv2
import numpy as np

# NOTE: Start script on server's position selection screen. 
# NOTE: if conquerors buff is enabled, scroll down before running.
# NOTE: Update all the coordinates for your screen setup. 

# Function to convert HH:mm:ss to total minutes
def time_to_minutes(time_str):
    hours, minutes, _ = map(int, time_str.split(':'))
    return hours * 60 + minutes


def text_sanitization(time_str):
    if not time_str:
        return ''
    if time_str[:3].isdigit():
        time_str = time_str[1:] # Remove extra leading digit
    parts = time_str.split(':')
    if len(parts) > 2 and len(parts[2]) > 2:
        parts[2] = parts[2][:2]  # Remove extra trailing digit
    return ':'.join(parts)

def remove_stale_roles(left, top, width, height, message, x, y):
    # Define the region to capture (left, top, width, height)
    region = (left, top, width, height)
    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region)
    # Convert the screenshot to a format suitable for pytesseract
    screenshot_rgb = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)

    # Define OCR configuration options
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789:'

    # Extract text with custom configuration
    text = text_sanitization(pytesseract.image_to_string(screenshot_rgb, config=custom_config))
    # Use regular expression to find time strings in HH:mm:ss format
    pattern = r'\b\d{2}:\d{2}:\d{2}\b'
    matches = re.findall(pattern, text)
    # Threshold in minutes
    threshold_minutes = 6
    if matches is None:
        print(f"{message} Screenshot returned NULL list.")
    elif not matches:
        print(f"{message} Screenshot returned no matches. Text: {text}")
    else:
        # Threshold in minutes
        total_minutes = time_to_minutes(matches[0])
        if total_minutes >= threshold_minutes:
            print(f"{matches[0]} {message} is greater than {threshold_minutes} minutes.")
            pyautogui.click(x, y) # click given title card
            time.sleep(.6)
            pyautogui.click(2025, 1200) # click dismiss
            time.sleep(.6)
            pyautogui.click(2040, 760) # click Confirm
            time.sleep(.6)
            # exit position card
            exitX = 2130
            exitY = 90
            pyautogui.click(exitX, exitY)
            time.sleep(.6)
            pyautogui.click(exitX, exitY)
            time.sleep(.6)
        else:
            print(f"{message} is less than {threshold_minutes} minutes.")


def refresh_positions():
    # Click back arrow button to exit position card screen
    pyautogui.click(1840, 1330)
    time.sleep(1.3)
    
	# Click back into capitol
    pyautogui.click(2360, 980)
    time.sleep(1)
    
	# Scroll down to re-center screen
    pyautogui.moveTo(2208, 582)
    pyautogui.mouseDown()
    pyautogui.moveTo(2208, 330, duration=0.5)
    
	# Release the mouse button
    pyautogui.mouseUp()
    time.sleep(.3)
	
def approve_applicant_list(x, y):
    # Click the position card from given coordinates.
    # click the approve button location a few times. Then exit out of the position card.
    clickSeconds1 = .65
    clickSeconds2 = .35

    # click position card
    pyautogui.click(x, y)
    time.sleep(clickSeconds1)
    
	# click "list" button
    listX = 2450 
    listY = 1170
    pyautogui.click(listX, listY)
    time.sleep(clickSeconds1)
    
	# scrolls up twice to avoid approving players lower in the queue
    pyautogui.moveTo(2175, 375)
    pyautogui.mouseDown()
    pyautogui.moveTo(2175, 975, duration=0.15)
    pyautogui.mouseUp()
    time.sleep(.15)
    pyautogui.moveTo(2175, 375)
    pyautogui.mouseDown()
    pyautogui.moveTo(2175, 975, duration=0.18)
    pyautogui.mouseUp()
    time.sleep(.3)
    # click approve
    approveX = 2342
    approveY = 350
    for i in range(3):
        pyautogui.click(approveX, approveY)
        time.sleep(clickSeconds2)
    # exit position card
    exitX = 2130
    exitY = 90
    pyautogui.click(exitX, exitY)
    time.sleep(clickSeconds2)
    pyautogui.click(exitX, exitY)
    time.sleep(clickSeconds1)
    return True

def main():
    # Conquerors Buff includes two additional position cards. Set to False if conquerors buff is disabled.
    conquerorsBuff = False
    
	
	 # coordinates is an x,y of the center of a title card.
	 # staleRoleCoordinates is (left, top, width, height) cordinates to which this program screenshots the timer of as well as the x, y coords of the position title to click on.
    if conquerorsBuff:
        coordinates = [
            (2109, 441), # Military Commander !!needs updated!! 
            (2316, 425), # Administration Commander !!needs updated!!
            (2175, 720), # Secretary of Strategy
            (2400, 720), # Secretary of Security
            (1950, 950), # Secretary of Development
            (2175, 950), # Secretary of Science
            (2400, 950)  # Secretary of Interior
			# Note, a player liking the bot's profile makes a permanent screen appear. This may be exitited via the "Awesome" button.
        ]
		
        staleRoleCoordinates = [
            (2083, 485, 77, 24, 'Military Commander', 2109, 441), #needs updated!!
            (2293, 485, 77, 24, 'Administrative Commander', 2316, 425), #needs updated!!
			(2135, 780, 105, 27, 'Secretary of Strategry', 2175, 720),
            (2365, 780, 105, 27, 'Secretary of Security', 2400, 720),
            (1910, 1075, 105, 27, 'Secretary of Development', 1950, 950),
            (2135, 1075, 105, 27, 'Secretary of Science', 2175, 950),
			(2365, 1075, 105, 27, 'Secretary of Interior', 2400, 950)
        ]
    else:
        coordinates = [
            (2175, 720), # Secretary of Strategy
            (2400, 720), # Secretary of Security
            (1950, 950), # Secretary of Development
            (2175, 950), # Secretary of Science
            (2400, 950)  # Secretary of Interior	
        ]
        staleRoleCoordinates = [
			(2135, 780, 105, 27, 'Secretary of Strategry', 2175, 720),
            (2365, 780, 105, 27, 'Secretary of Security', 2400, 720),
            (1910, 1075, 105, 27, 'Secretary of Development', 1950, 950),
            (2135, 1075, 105, 27, 'Secretary of Science', 2175, 950),
			(2365, 1075, 105, 27, 'Secretary of Interior', 2400, 950)
        ]
    time.sleep(5) # giving time to get screen ready
    i = 9
    j = 0
	
    while True:
        i += 1
        j += 1
        # Iterate through the positions and approve all
		# TODO - use pytesseract to detect a new application and then run approve_applicant_list for that applied to title
        for x, y in coordinates:
            action = approve_applicant_list(x, y)
        # Every 5 runs, refresh the title screen and remove titles positions older than 6 minutes
        if i % 5 == 0:
            refresh_positions()
            # Iterate through positions to check for stale activity
            for left, top, width, height, message, x, y in staleRoleCoordinates:
                remove_stale_roles(left, top, width, height, message, x, y)
        if (j == 1):
            print(f"script has ran {j} time")
        else:
            print(f"script has ran {j} times")
			
		
        time.sleep(4) # giving operator time to stop the script

# Do not remove
if __name__ == "__main__":
    main()
