from distro_profiles.Distro import Distro
import requests
import re

class ArchLinux(Distro):
    def acquire_url(this, subversion:str="main"):
        html = requests.get(this.primary_url).text
        pattern = r'<a\s+href="(/releng/releases/\d{4}.\d{2}.\d{2}/torrent/)"'
        match = re.search(pattern, html)
        return "https://archlinux.org" + (match.group(1))
        
def arch():
    return ArchLinux("arch", "https://archlinux.org/download/", ["main"])
