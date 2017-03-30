router_url = "http://router/"

reset_endpoint = "ut_reset.html"
restart_endpoint = "setup.cgi"
status_endpoint = "BelkinAPI/DBWANStatus"

def reset_url():
    return router_url + reset_endpoint

def restart_url():
    return router_url + restart_endpoint

def status_url():
    return router_url + status_endpoint
