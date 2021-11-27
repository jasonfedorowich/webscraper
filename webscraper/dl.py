import uuid

import requests
import browser_cookie3

class CookieJar:
    def __init__(self):
        self.cj = None

    def from_chrome(self, file_name=None):
        self.cj = browser_cookie3.chrome(cookie_file=file_name)

    def from_firefox(self, file_name=None):
        self.cj = browser_cookie3.firefox(cookie_file=file_name)

    def set(self, cj):
        self.cj = cj


def dl_image_from_url(url, **kwargs):
    res = requests.request(method=kwargs.get('method', 'get'), url=url, headers=kwargs.get('headers', None), cookies=kwargs.get('cookies', CookieJar()).cj)
    if res.ok:
        fn = kwargs.get('file_name', str(uuid.uuid4()) + '.jpg')
        with open(fn, 'wb') as f:
            f.write(res.content)
    else:
        raise Exception(f'Bad response recieved with {res.status_code} and {res.content}')

def dl_video_from_url(url, **kwargs):
    res = requests.request(method=kwargs.get('method', 'get'), url=url, headers=kwargs.get('headers', None),
                           cookies=kwargs.get('cookies', CookieJar()).cj, stream=kwargs.get('stream', True))
    if res.ok:
        fn = kwargs.get('file_name', str(uuid.uuid4()) + '.mp4')
        with open(fn, 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

    else:
        raise Exception(f'Bad response recieved with {res.status_code} and {res.content}')