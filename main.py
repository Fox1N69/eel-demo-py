import eel
import pyautogui
from models.product import showallprod

eel.init('interface')


@eel.expose
def fetchalldata():
    select_reg = showallprod()
    eel.action_out(select_reg)




eel.start('index.html',
          size=pyautogui.size())
