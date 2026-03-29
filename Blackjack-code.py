import pyautogui
import pytesseract
import time
import re
import keyboard
from PIL import Image
 
def try_find_button(button_image):
    try:
        button = pyautogui.locateOnScreen(button_image, confidence=0.8)
        return button
    except pyautogui.ImageNotFoundException:
        return None




def bet():
    button = try_find_button('bet_button.png')
    if button:
        center = pyautogui.center(button)
        pyautogui.moveTo(center.x, center.y)
        pyautogui.click(clicks=2)

def gamble():
    # Take the screenshot
    im1 = pyautogui.screenshot(region=(800,790, 90, 40))

    # Run OCR on the screenshot to extract text
    extracted_text = pytesseract.image_to_string(im1)
    print(extracted_text)
    # Find and print only the score number
    match = re.search(r'Score[:\s]+(\d+)', extracted_text, re.IGNORECASE)
    if match:
        score = int(match.group(1))
        print("Score:", score)

        if score >= 18:
            button = try_find_button('stand_button.png')
            if button:
                center = pyautogui.center(button)
                pyautogui.moveTo(center.x, center.y)
                pyautogui.click()
        else:
            button = try_find_button('hit_button.png')
            if button:
                center = pyautogui.center(button)
                pyautogui.moveTo(center.x, center.y)
                pyautogui.click()
    else:
        print("Score not found")


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("you got 3 seconds")
time.sleep(3)



while True:
    if keyboard.is_pressed('esc'):  # kill switch
        print("Stopped by user")
        sys.exit()

    bet()
    gamble()


