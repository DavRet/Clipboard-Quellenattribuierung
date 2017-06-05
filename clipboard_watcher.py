import time
import threading
import csv

from PyQt5.QtWidgets import QApplication

app = QApplication(["", ""])
clipboard = app.clipboard()
mimeData = clipboard.mimeData()


def printClipboardData(clipboard_content):
    print(str(mimeData.urls()))
    print(clipboard_content)

    with open('clipboard_monitor.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)

        row = [clipboard_content] + [str(mimeData.formats())]

        for f in mimeData.formats():
            print("---- %s ----" % f)
            data = str(mimeData.data(f))
            row.append(f)
            row.append(data)

            if len(data) > 100:
                print(data[:100] + " [...]")
            else:
                print(data)
            print("")

        writer.writerow(row)


class ClipboardWatcher(threading.Thread):
    def __init__(self, callback, pause=5.):
        super(ClipboardWatcher, self).__init__()
        self._callback = callback
        self._pause = pause
        self._stopping = False

    def run(self):
        recent_value = ""
        while not self._stopping:
            tmp_value = clipboard.text()
            if tmp_value != recent_value:
                recent_value = tmp_value
                self._callback(recent_value)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True


def main():
    watcher = ClipboardWatcher(printClipboardData, 5.)
    watcher.start()
    while True:
        try:
            print("Waiting for changed clipboard...")
            time.sleep(10)
        except KeyboardInterrupt:
            watcher.stop()
            break


if __name__ == "__main__":
    main()
