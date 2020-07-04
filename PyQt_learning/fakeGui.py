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

# description: first simple example

# from PyQt5.QtWidgets import QApplication, QLabel
#
# label = QLabel("ja, super")
# label.show()
# app.exec_()
#------------------------------------------------------

def firstPyQtGui():
    # description: two buttons in a layout
    from PyQt5.QtWidgets import QApplication\
        , QWidget\
        , QPushButton \
        , QVBoxLayout \
        , QSpacerItem \
        , QSpacerItem \
        , QLCDNumber \
        , QSlider
    from PyQt5.QtCore import Qt # for the orientation

    app = QApplication([])
    app.setApplicationName("my second PyQt app, lol")
    window = QWidget()
    layout = QVBoxLayout()

    # add the widgets
    upperButton = QPushButton("upper button")
    layout.addWidget(upperButton)
    lowerButton = QPushButton("lower button")
    layout.addWidget(lowerButton)

    lcd = QLCDNumber() # research: how to hand over the parent for widget at PyQt?
    layout.addWidget(lcd)
    #upperButton.clicked.connect(lcd.display("1"))
    slider = QSlider(Qt.Horizontal)
    layout.addWidget(slider)
    slider.valueChanged.connect(lcd.display)

    # just make it a bit wider -  else the window's title is cut
    spacer = QSpacerItem(666, 1)
    layout.addSpacerItem(spacer)
    window.setLayout(layout)
    # execute
    window.show()
    app.exec() # what is the difference to exec()?

#------------------------------------------------------

# exec versus exec_:
# https://www.learnpyqt.com/blog/pyqt5-vs-pyside2/#exec-or-exec_

#------------------------------------------------------

# https://machinekoder.com/pyqt-vs-qt-for-python-pyside2-pyside/

#------------------------------------------------------


#-------------------------

# ### execution ###
if __name__ == "__main__":
    firstPyQtGui()

#-------------------------
