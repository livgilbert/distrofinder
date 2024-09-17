from distro_profiles.Distro import Distro
import requests
import re

class Kali(Distro):
    def acquire_url(this, subversion:str):
        html = requests.get(this.primary_url).text
        if subversion == "main":
            pattern = r'https://cdimage.kali.org/kali-\d{4}.\d/kali-linux-\d{4}.\d-installer-amd64.iso.torrent'
        elif subversion == "everything":
            pattern = r'https://cdimage.kali.org/kali-\d{4}.\d/kali-linux-\d{4}.\d-installer-everything-amd64.iso.torrent'
        elif subversion == "live_main":
            pattern = r'https://cdimage.kali.org/kali-\d{4}.\d/kali-linux-\d{4}.\d-live-amd64.iso.torrent'
        elif subversion == "live_everything":
            pattern = r'https://cdimage.kali.org/kali-\d{4}.\d/kali-linux-\d{4}.\d-live-everything-amd64.iso.torrent'
        else:
            raise ValueError
        match = re.search(pattern, html)
        return match.group(0)
        
def kali():
    return Kali("kali", "https://www.kali.org/get-kali", ["main", "everything", "live_main", "live_everything"])
