#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.Qt import QDrag, QMimeData


class DragDrop(QtWidgets.QWidget):
    
    def __init__(self):
        super(DragDrop, self).__init__()
        self.content = None
        self.initUI()
        
    def initUI(self):      
        # set the text property of the widget we are inheriting
        self.content = "Drag from me or drop stuff into me."
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("'Drag'n Drop Demo")
        # widget should accept focus by click and tab key
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.show()

    def keyPressEvent(self, ev):
        self.content = ev.text()
        self.update()

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText(self.content)
            drag.setMimeData(mimeData)
            drag.setPixmap(iconPixmap)
            dropAction = drag.exec()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 32))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.content)        
        qp.end()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    dd = DragDrop()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
