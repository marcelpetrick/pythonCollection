# idea: create files with random binary content (written to disk) - see how much throughput is possible

# todo:
# * gui (see mockup)
# * give option to write until disk full or "leave 100 MiB free"?; repeat option? one file or several files (uuid based?)

#-----------------------------

def groundSpace(pattern = "0", repsPattern = 0, repsChunk = 0):

    convertedContent = bytearray()
    for _ in range(repsPattern):
        convertedContent.extend(map(ord, pattern))
    #byteArray = bytearray(convertedContent)
    with open('temporaryFile.tmp', 'ba') as tempFile: # refer to this for the second param: https://docs.python.org/3/library/functions.html#open
        for _ in range(repsChunk):
            tempFile.write(convertedContent)
            print(".")
        print("groundSpace successfully run once")

#-----------------------------

# I am impressed: writes 8 GiB in some seconds ... can be maybe improved
# Benchmarks over several seconds on Win10; checked via TaskManager
# Samsung SSD 960 EVO 500GB achieves just 300 MB/s continuous
# sk hynix BC501 256 GB: 160 MB/s
# while True:
#     groundSpace()

#-----------------------------

# failure is reported like this
# ..
# one GB written
# one GB written
# Traceback (most recent call last):
#   File "C:/Users/husband-boy/Desktop/coding/pythonCollection/GroundSpace/groundSpace.py", line 23, in <module>
#     while True:
#   File "C:/Users/husband-boy/Desktop/coding/pythonCollection/GroundSpace/groundSpace.py", line 13, in groundSpace
#     tempFile.write(byteArray)
# OSError: [Errno 28] No space left on device
#
# Process finished with exit code 1

#---------------

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore

#---------------

# ui-file converted by pyuic5: see https://www.riverbankcomputing.com/static/Docs/PyQt5/designer.html for more info
# $ pyuic5 frontend.ui > ui_frontend.py
from ui_frontend import Ui_frontend # PyCharm will mark this as unresolvable reference, but it works

class GroundSpaceGUI(QDialog):
    def __init__(self):
        super(GroundSpaceGUI, self).__init__() # call inherited classes' ctor

        print("class GroundSpaceGUI()")

        self.ui = Ui_frontend()
        self.ui.setupUi(self)

        # remove the "What's this"-ui-item
        self.setWindowFlags(self.windowFlags() # reuse initial flags
            & ~QtCore.Qt.WindowContextHelpButtonHint
            #& QtCore.Qt.CustomizeWindowHint # not needed, this would just mingle with the dialog-settings (-> wrong!)
        )

        # access ui-members and change their attributes
        #self.ui.baseDirLE.setText(".")
        self.ui.patternLE.setText("0") # or 🐈? does not work, because not in the range for a byte! 0..255
        self.ui.repsPatternLE.setText("2 ** 20")
        self.ui.repsChunkLE.setText("2 ** 10")
        self.slotValuesChanged() # make sure the currently shown size is correct

        # handling for user-input
        self.ui.runPB.clicked.connect(self.slotRunClicked) # start button
        self.ui.patternLE.textChanged.connect(self.slotValuesChanged)
        self.ui.repsPatternLE.textChanged.connect(self.slotValuesChanged)
        self.ui.repsChunkLE.textChanged.connect(self.slotValuesChanged)

    def slotValuesChanged(self):
        print("slotValuesChanged")
        # todo collect values and multiply them and then assign to the lineedit

        self.ui.resultFileSizeLE.setText("1234 fake")

    def slotRunClicked(self):
        # prepare the input
        pattern = self.ui.patternLE.text() # use braces at the end

        repPattern = eval(self.ui.repsPatternLE.text())
        if(not isinstance(repPattern, int)):
            repPattern = 0
        print(f"repPattern: {repPattern}")

        repsChunk = eval(self.ui.repsChunkLE.text())
        if(not isinstance(repsChunk, int)):
            repsChunk = 0
        print(f"repsChunk: {repsChunk}")

        # trigger creation
        self.groundSpace(pattern, repPattern, repsChunk)

    def groundSpace(self, pattern = "0", repsPattern = 0, repsChunk = 0):
        convertedContent = bytearray()
        for _ in range(repsPattern):
            convertedContent.extend(map(ord, pattern))

        with open('temporaryFile.tmp', 'ba') as tempFile: # refer to this for the second param: https://docs.python.org/3/library/functions.html#open
            for i in range(repsChunk):
                tempFile.write(convertedContent)
                self.ui.progressBar.setValue(100 * i / repsChunk)

        self.ui.progressBar.setValue(100)

#---------------

# now following the clean approach: https://stackoverflow.com/a/37907101/1694302
def makeGui():
    app = QApplication(sys.argv)
    window = GroundSpaceGUI()

    window.show()
    sys.exit(app.exec_())

#---------------

makeGui()
