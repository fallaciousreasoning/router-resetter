import requests

import router

def get_status():
    url = router.status_url()
    request_id = '1' # the router doesn't care but this has to be a thing
    response = requests.get(url, params={
            'RequestID':request_id
        })

    json = response.json()
    return 'connected' if json['Status'] == 'constWANConnected' else 'disconnected'

if __name__ == "__main__":
    print(get_status())