import requests
import router

def restart():
    """Restarts the router"""
    url = router.restart_url()
    data = {
        'todo': 'save',
        'flush_to_page': 0,
        'this_file': 'ut_reset.html',
        'next_file': '000-Dashboard.htm',
        'message': ''
    }

    response = requests.post(url, data)

if __name__ == '__main__':
    restart()
