from datetime import datetime
import time

import restart
import status

class Watcher:
    def __init__(self, check_rate=30, max_restart_rate=180):
        """Initializes a new watcher"""

        self.check_rate = check_rate
        self.max_restart_rate = max_restart_rate
        self.last_check = None

    def run(self):
        """Begins running the watcher (witch will run forever)"""
        while True:
            print("Checking...")
            self.last_check = datetime.now()
            till_next_check = self.check_rate

            current_status = status.get_status()

            # if we aren't connected, restart the router
            if current_status == "disconnected":
                till_next_check = self.max_restart_rate
                restart.restart()
                print("Restarted!")

            to_sleep = max(till_next_check - (datetime.now() - self.last_check).seconds, 0)
            time.sleep(to_sleep)

w = Watcher(10)
w.run()
