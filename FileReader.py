import os
import time


class FileReader:
    # Read a file dynamically as it expands
    def follow_file(self, file) -> str:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
