import requests
import urllib3
from bs4 import BeautifulSoup
from PIL import Image
from io import StringIO
from io import open as iopen
import json

def extract_data():
    headers = {
        'Referer': 'https://my.nu.edu.kz/.PhoneBookPortlet/PhoneBookPortletRedirectServlet',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
    }
    payload = {
        'username': '',
        'organisationNumber': 'KS_ZUP_NU1',
        'organisationName': 'Назарбаев Университет',
        'departments': '',
        'linkSelected': '',
        'schoolVal': 'SSH',
        'school': 'School of Sciences and Humanities',
        'courses': 'Year 4',
        'usertype': 'Students',
        'maxRows': '25'
    }
    url = 'https://my.nu.edu.kz/.PhoneBookPortlet/UsernameServlet'
    r = requests.post(url, data=payload, headers=headers)

    json_data = r.json()

    data = json_data[0]['rows']

    for item in data:
        uid = item['userid']
        url_photo = 'https://my.nu.edu.kz/.PhoneBookPortlet/UsernameServlet?type=getphoto&uid=' + str(uid)
        headers_photo = {
            'Referer': 'https://my.nu.edu.kz/.PhoneBookPortlet/PhoneBookPortletRedirectServlet',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
        }
        payload_photo = {
            'type': 'getphoto',
            'uid': uid
        }
        r_photo = requests.get(url_photo, headers=headers_photo, params=payload_photo)
        filename = str(uid) + '.jpg'

        with iopen(filename, 'wb') as file:
            file.write(r_photo.content)

extract_data()



