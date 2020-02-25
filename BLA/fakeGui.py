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

# description: two buttons in a layout
from PyQt5.QtWidgets import QApplication\
    , QWidget\
    , QPushButton\
    , QVBoxLayout \
    , QSpacerItem

app = QApplication([])
app.setApplicationName("my second PyQt app, lol")
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton("upper button"))
layout.addWidget(QPushButton("lower button"))
spacer = QSpacerItem(666, 1)
layout.addSpacerItem(spacer)
window.setLayout(layout)
window.show()
app.exec() # what is the difference to exec()?

#------------------------------------------------------

# exec versus exec_:
# https://www.learnpyqt.com/blog/pyqt5-vs-pyside2/#exec-or-exec_

#------------------------------------------------------

# https://machinekoder.com/pyqt-vs-qt-for-python-pyside2-pyside/

#------------------------------------------------------
