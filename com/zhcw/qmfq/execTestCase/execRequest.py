import requests

def request_get(url,re_param,cookieVal):
    if cookieVal != "":
        r = requests.get(url,params=re_param,cookies = cookieVal)
    else:
        r = requests.get(url, params=re_param)

    return r

def request_post(url,re_param,cookieVal):
    if cookieVal != "":
        r = requests.post(url,data=re_param,cookies = cookieVal)
    else:
       r = requests.post(url,data=re_param)

    return r
