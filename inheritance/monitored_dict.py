from datetime import datetime
import time


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp("MonitoredDict created")

    def log_timestamp(self, message):
        t = datetime.now().strftime('%H:%M:%S.%f')
        self.log.append(f"{t} {message}")

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp(f"value for key [{key}] retrieved")
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp(f"value for key [{key}] set")


md = MonitoredDict()
time.sleep(1)
md[1] = 10
time.sleep(1)
md[2] = 11

print(md)
print()
print("\n".join(md.log))

