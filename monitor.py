import psutil
import threading
import time

class Monitor:
    def __init__(self):
        self.is_monitoring = False

    def start_monitoring(self, callback):
        self.callback = callback
        self.is_monitoring = True
        self.thread = threading.Thread(target=self._monitor)
        self.thread.start()

    def stop_monitoring(self):
        self.is_monitoring = False

    def _monitor(self):
        while self.is_monitoring:
            data = {
                'Download': 'Download Progress: 100%\nDownload Speed: 10 MB/s',
                'Disk': f'Disk Usage: {psutil.disk_usage("/").percent}%',
                'CPU': f'CPU Usage: {psutil.cpu_percent()}%',
                'Memory': f'Memory Usage: {psutil.virtual_memory().percent}%',
                'Network': f'Network Usage: {psutil.net_io_counters().bytes_sent / 1024 / 1024:.2f} MB'
            }
            self.callback(data)
            time.sleep(1)
