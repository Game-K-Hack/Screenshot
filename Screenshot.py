#######################################################################################################################
##        _____                        _  __      ##        _____                              _           _         ##
##       / ____|                      | |/ /      ##       / ____|                            | |         | |        ##
##      | |  __  __ _ _ __ ___   ___  | ' /       ##      | (___   ___ _ __ ___  ___ _ __  ___| |__   ___ | |_       ##
##      | | |_ |/ _` | '_ ` _ \ / _ \ |  <        ##       \___ \ / __| '__/ _ \/ _ \ '_ \/ __| '_ \ / _ \| __|      ##
##      | |__| | (_| | | | | | |  __/ | . \       ##       ____) | (__| | |  __/  __/ | | \__ \ | | | (_) | |_       ##
##       \_____|\__,_|_| |_| |_|\___| |_|\_\      ##      |_____/ \___|_|  \___|\___|_| |_|___/_| |_|\___/ \__|      ##
##                                                ##                                                                 ##
#######################################################################################################################
##                                                                                                                   ##
##      Détecte si la touche "Imprime écran" est enfoncer et prend un screenshot pour l'enregistrer dans :           ##
##      "D:\Pictures\Screenshot\"                                                                                    ##
##                                                                                                                   ##
#######################################################################################################################

from pynput.keyboard import Key, Listener
import pyautogui
import datetime

#######################################################################################################################

def on_press(key):
    if key == Key.print_screen:
        myScreenshot = pyautogui.screenshot()
        date = datetime.datetime.now()
        screenshot_date = (str(date.day) + "-" + str(date.month) + "-" + str(date.year) + " " + str(date.hour) + "-" + str(date.minute) + "-" + str(date.second))
        myScreenshot.save("D:\Pictures\Screenshot\screenshot " + str(screenshot_date) + ".png")

#######################################################################################################################

with Listener(on_press=on_press) as listener:
    listener.join()