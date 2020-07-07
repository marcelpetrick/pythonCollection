# author mail@marcelpetrick.it
# license: GPLv3.0

#------------------------------------------------------

# upgrade pip:
# $ python -m pip install --upgrade pip
# install PyQt in the latest version: 5.14 for me
# pip install PyQt5

#------------------------------------------------------

# follows https://build-system.fman.io/pyqt5-tutorial

#------------------------------------------------------

def firstPyQtGui():
    # description: two buttons in a layout
    from PyQt5.QtWidgets import QApplication \
        , QWidget\
        , QPushButton \
        , QVBoxLayout \
        , QHBoxLayout \
        , QSpacerItem \
        , QSpacerItem \
        , QLCDNumber \
        , QSlider
    from PyQt5.QtCore import Qt # for the orientation

    app = QApplication([])
    app.setApplicationName("my second PyQt app, lol")
    window = QWidget()

    # add the widgets
    verticalLayoutButtons = QVBoxLayout()
    upperButton = QPushButton("upper button")
    verticalLayoutButtons.addWidget(upperButton)
    lowerButton = QPushButton("lower button")
    verticalLayoutButtons.addWidget(lowerButton)

    verticalLayoutSlider = QVBoxLayout()
    lcd = QLCDNumber() # research: how to hand over the parent for widget at PyQt?
    verticalLayoutSlider.addWidget(lcd)
    slider = QSlider(Qt.Horizontal)
    verticalLayoutSlider.addWidget(slider)
    slider.valueChanged.connect(lcd.display)
    # just make it a bit wider -  else the window's title is cut
    spacer = QSpacerItem(666, 1)
    verticalLayoutSlider.addSpacerItem(spacer)

    # put both layouts into a new one
    horizontalLayout = QHBoxLayout()
    horizontalLayout.addLayout(verticalLayoutButtons)
    horizontalLayout.addLayout(verticalLayoutSlider)
    window.setLayout(horizontalLayout)

    # execute
    window.show()
    app.exec() # what is the difference to exec()?

#------------------------------------------------------

# exec versus exec_:
# https://www.learnpyqt.com/blog/pyqt5-vs-pyside2/#exec-or-exec_

#------------------------------------------------------

# https://machinekoder.com/pyqt-vs-qt-for-python-pyside2-pyside/

#------------------------------------------------------


#------------------------------------------------------

# ### execution ###
if __name__ == "__main__":
    firstPyQtGui()

#------------------------------------------------------
