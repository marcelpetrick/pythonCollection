# ah, the include problem again ..
from . import GolBoard

gol = GolBoard()
# Traceback (most recent call last):
#   File "C:/Users/mpe/Desktop/MarcelsFolder/coding/pythonCollection/MarcelsGameOfLife/GolInterface.py", line 2, in <module>
#     from . import GolBoard
# ImportError: cannot import name 'GolBoard' from '__main__' (C:/Users/mpe/Desktop/MarcelsFolder/coding/pythonCollection/MarcelsGameOfLife/GolInterface.py)