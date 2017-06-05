#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication

app = QApplication(["",""])
clipboard = app.clipboard()
mimeData = clipboard.mimeData()

print("Current clipboard offers formats: " + str(mimeData.formats()))


for f in mimeData.formats():
    print("---- %s ----" % f)
    data = str(mimeData.data(f))
    if len(data) > 100:
        print(data[:100] + " [...]")
    else:
        print(data)
    print("")



