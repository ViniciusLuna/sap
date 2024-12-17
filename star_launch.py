import pyautogui
import subprocess
import seletores
from time import sleep

# Vinicius Luna
# Utilizando biblioteca pyautogui

launch = subprocess.Popen(seletores.path_sap)
sleep(10)
launch.terminate()