from datetime import datetime
import time

import restart
import status

class Watcher:
    def __init__(self, check_rate=30, restart_rate=120):
        """Initializes a new watcher"""

        self.check_rate = check_rate
        self.restart_rate = 120

    def run(self):
        self.last_restart = None
        
        while True:
            self.last_check = datetime.now()

            s = status.get_status()

            to_sleep = max(self.check_rate - (datetime.now() - self.last_check).seconds, 0)
            time.sleep(to_sleep)

w = Watcher(5)
w.run()
