import requests

import router

disconnected_status = 'constWANNotConnected'
connected_status = 'constWANConnected'

def get_status():
    url = router.status_url()
    request_id = '1' # the router doesn't care but this has to be a thing
    try:
        response = requests.get(url, params={
                'RequestID':request_id
            })

        if not response.status_code == 200:
            return "disconnected"

        json = response.json()
        if json['Status'] == 'constWANConnected':
            return 'connected'
        else:
            return 'disconnected'
    except:
        return 'down'

if __name__ == "__main__":
    print(get_status())