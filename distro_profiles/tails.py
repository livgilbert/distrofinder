from distro_profiles.Distro import Distro
import requests
import re

class Tails(Distro):
    def acquire_url(this, subversion:str="main"):
        html = requests.get(this.primary_url).text
        pattern = r'href="\s+(https://tails.net/torrents/files/tails-amd64-\d.\d.img.torrent)\s+"'
        match = re.search(pattern, html)
        return match.group(1)

def tails():
    return Tails("tails", "https://tails.net/install/download/index.en.html", ["main"])
