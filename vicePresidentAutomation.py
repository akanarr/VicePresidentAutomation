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

### Hardcoded Mouse Coordinates ###

# click "list" button
listX = 1560 
listY = 1180
# scroll up to top of application list
scrollX = 1280
scrollY = 300
scrollY2 = 1100
# Click Green Check Mark to Accept Application
AcceptX = 1452
AcceptY = 347
# exit position card
exitX = 1250
exitY = 80
# exit capitol room
capitolExitX = 950
capitolExitY = 1325
# enter capitol room
capitolEnterX = 1500
capitolEnterY = 980
# Scroll down to re-center screen
recenterX = 935
recenterY = 1000
recenterY2 = 450
# Click "Dismiss" button
dismissX = 1165
dismissY = 1195
# Click "Confirm" dismissal button
confirmX = 1153
confirmY = 763
### End of Hardcoded Mouse Coordinates ####


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
            # click given title card
            pyautogui.click(x, y) 
            time.sleep(.6)
            # click dismiss
            pyautogui.click(dismissX, dismissY) 
            time.sleep(.6)
            # click Confirm
            pyautogui.click(confirmX, confirmY) 
            time.sleep(.6)
            # exit position card
            pyautogui.click(exitX, exitY)
            time.sleep(.6)
            pyautogui.click(exitX, exitY)
            time.sleep(.6)
        else:
            print(f"{message} is less than {threshold_minutes} minutes.")


def refresh_positions():
    # Click back arrow button to exit position card screen
    pyautogui.click(capitolExitX, capitolExitY)
    time.sleep(1.3)
    
	# Click back into capitol
    pyautogui.click(capitolEnterX, capitolEnterY)
    time.sleep(1)
    
	# Scroll down to re-center screen
    pyautogui.moveTo(recenterX, recenterY)
    pyautogui.mouseDown()
    pyautogui.moveTo(recenterX, recenterY2, duration=0.5)
    
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
    pyautogui.click(listX, listY)
    time.sleep(clickSeconds1)
    
	# scrolls up twice to avoid approving players lower in the queue
    pyautogui.moveTo(scrollX, scrollY)
    pyautogui.mouseDown()
    pyautogui.moveTo(scrollX, scrollY2, duration=0.15)
    pyautogui.mouseUp()
    time.sleep(.15)
    pyautogui.moveTo(scrollX, scrollY)
    pyautogui.mouseDown()
    pyautogui.moveTo(scrollX, scrollY2, duration=0.18)
    pyautogui.mouseUp()
    time.sleep(.3)
    # click accept application
    for i in range(3):
        pyautogui.click(AcceptX, AcceptY)
        time.sleep(clickSeconds2)
    # exit position card
    pyautogui.click(exitX, exitY)
    time.sleep(clickSeconds2)
    pyautogui.click(exitX, exitY)
    time.sleep(clickSeconds1)
    return True

def main():
    # Conquerors Buff includes two additional position cards. Set to False if conquerors buff is disabled.
    conquerorsBuff = True
    
	
	 # coordinates is an x,y of the center of a title card.
	 # staleRoleCoordinates is (left, top, width, height) coordinates to which this program screenshots the timer of as well as the x, y coords of the position title to click on.
    if conquerorsBuff:
        coordinates = [
            (1095, 392), # Military Commander !!needs updated!! 
            (1387, 389), # Administration Commander !!needs updated!!
            (1260, 927), # Secretary of Strategy
            (1487, 929), # Secretary of Security
            (1030, 1075), # Secretary of Development
            (1260, 1075), # Secretary of Science
            (1490, 1075)  # Secretary of Interior
			# Note, a player liking the bot's profile makes a permanent screen appear. This may be exitited via the "Awesome" button.
        ]
		
        staleRoleCoordinates = [
            #(1090, 592, 105, 25, 'Military Commander', 1095, 392), 
            (1354, 592, 105, 25, 'Administrative Commander', 1387, 389), 
			(1222, 887, 105, 25, 'Secretary of Strategry', 1260, 927),
            (1450, 887, 105, 25, 'Secretary of Security', 1487, 929),
            (994, 1179, 105, 25, 'Secretary of Development', 1030, 1075),
            (1222, 1179, 105, 25, 'Secretary of Science', 1260, 1075),
			(1450, 1179, 105, 25, 'Secretary of Interior', 1490, 1075)
        ]
    else:
        coordinates = [
            (1260, 927), # Secretary of Strategy
            (1487, 929), # Secretary of Security
            (1030, 1075), # Secretary of Development
            (1260, 1075), # Secretary of Science
            (1490, 1075)  # Secretary of Interior
        ]
        staleRoleCoordinates = [
			(1222, 887, 105, 25, 'Secretary of Strategry', 1260, 927),
            (1450, 887, 105, 25, 'Secretary of Security', 1487, 929),
            (994, 1179, 105, 25, 'Secretary of Development', 1030, 1075),
            (1222, 1179, 105, 25, 'Secretary of Science', 1260, 1075),
			(1450, 1179, 105, 25, 'Secretary of Interior', 1490, 1075)
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
			
		
        time.sleep(20) # giving operator time to stop the script

# Do not remove
if __name__ == "__main__":
    main()
