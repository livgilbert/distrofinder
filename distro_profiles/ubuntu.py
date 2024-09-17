from distro_profiles.Distro import Distro
import requests
import re

class Ubuntu(Distro):
    def acquire_url(this, subversion:str):
        html = requests.get(this.primary_url).text
        if subversion == "desktop":
            pattern = r'href="(https://releases.ubuntu.com/\d+.\d+/ubuntu-\d+.\d+.\d+-desktop-amd64.iso.torrent)"'
        elif subversion == "server":
            pattern = r'href="(https://releases.ubuntu.com/\d+.\d+/ubuntu-\d+.\d+.\d+-live-server-amd64.iso.torrent)"'
        else:
            raise ValueError
        match = re.search(pattern, html)
        return match.group(1)
        
def ubuntu():
    return Ubuntu("ubuntu", "https://ubuntu.com/download/alternative-downloads", ["desktop", "server"])
