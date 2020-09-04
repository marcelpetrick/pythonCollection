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

        # initialize the members
        self.path = 'temporaryFile.tmp'
        self.pattern = "0"
        self.repPattern = 0
        self.repsChunk = 0

        # access ui-members and change their attributes
        self.ui.baseDirLE.setText(self.path)
        self.ui.baseDirLE.setEnabled(True) # todo change this inside the ui file when also the "repeat infinite is done"
        self.ui.patternLE.setText("0") # or 🐈? does not work, because not in the range for a byte! 0..255
        self.ui.repsPatternLE.setText("2 ** 20")
        self.ui.repsChunkLE.setText("2 ** 10")
        self.slotValuesChanged() # called to make sure the currently shown size is correct; if setting would happen after the connects, this line could be saved. But then the valueChanged-slot is called three times ..

        # handling for user-input
        self.ui.runPB.clicked.connect(self.slotRunClicked) # start button
        self.ui.patternLE.textChanged.connect(self.slotValuesChanged)
        self.ui.repsPatternLE.textChanged.connect(self.slotValuesChanged)
        self.ui.repsChunkLE.textChanged.connect(self.slotValuesChanged)

    def slotValuesChanged(self):
        ''' Collect all values and multiply them and assign to the corresponding lineedit. '''

        self.collectAllInput()
        sizeInByte = len(self.pattern) * self.repPattern * self.repsChunk # maybe it is wrong, because the string won't be converted 1 to 1 into bytes, but ... who cares?

        self.ui.resultFileSizeLE.setText(self.stringifyByteValue(sizeInByte))

    def stringifyByteValue(self, number):
        prefixes = ['', 'K', 'M', 'G', 'T'] # what if bigger?
        numberOfOrder = 0
        while number > 1024:
            if numberOfOrder == len(prefixes) - 1:
                break
            number /= 1024
            numberOfOrder += 1

        prefixToUse = prefixes[numberOfOrder]

        resultString = str(number) + " " + prefixToUse + "Byte"
        return resultString

    def slotRunClicked(self):
        # prepare the input
        self.collectAllInput()

        # trigger creation
        self.groundSpace(self.path, self.pattern, self.repPattern, self.repsChunk)

    def collectAllInput(self):
        self.pattern = self.ui.patternLE.text() # use braces at the end to trigger Qt-item-method
        self.path = self.ui.baseDirLE.text()

        # todo the evals are really a killer. not that they crash while doing something like "2 1", but
        # also malicious actions are possible: https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
        # see additionally: https://realpython.com/python-eval-function/
        repsDefaultValue = 1

        try:
            repPattern = eval(self.ui.repsPatternLE.text())
        except SyntaxError:
            repPattern = repsDefaultValue
        if(not isinstance(repPattern, int)):
            repPattern = repsDefaultValue
        print(f"repPattern: {repPattern}") # todom remove
        self.repPattern = repPattern

        try:
            repsChunk = eval(self.ui.repsChunkLE.text())
        except SyntaxError:
            repsChunk = repsDefaultValue
        if(not isinstance(repsChunk, int)):
            repsChunk = repsDefaultValue
        print(f"repsChunk: {repsChunk}") # todom remove
        self.repsChunk = repsChunk

    def groundSpace(self, path = 'temporaryFile.tmp', pattern = "0", repsPattern = 0, repsChunk = 0):
        convertedContent = bytearray()
        for _ in range(repsPattern):
            convertedContent.extend(map(ord, pattern))

        with open(path, 'ba') as tempFile: # refer to this for the second param: https://docs.python.org/3/library/functions.html#open
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
