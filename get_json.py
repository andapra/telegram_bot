import os, shutil
import json

class jsonFile():
    def __init__(self, data, filename) -> None:
        self.data = data
        self.filename = filename

    def output(self):
        with open(self.filename, 'w', encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)