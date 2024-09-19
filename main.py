from distro_profiles import resolve_requested_distros
import requests
import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser(
        prog="DistroFinder",
        description="Automatically find the latest URLs for linux distro ISOs",
        epilog=""
        )
parser.add_argument("action", choices=["list", "url"])
parser.add_argument("-d", "--distros", default="", required=False)
parser.add_argument("-m", "--minimal", action="store_true")
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()
requested_distros = args.distros.replace(" ", "").split(",")

if args.action == "list":
    tab = PrettyTable()
    tab.add_column("#", [])
    tab.add_column("Distro", [], align="r")
    tab.add_column("Subversion", [], align="l")
    tab.add_column("Download page", [], align="l")
    # for listing we want default to be all
    if requested_distros == [''] or len(requested_distros) == 0:
        requested_distros = ["all"]

    for (idx, distro, subver) in resolve_requested_distros(requested_distros):
        tab.add_row([idx, distro.distro_title, subver, distro.primary_url])
    print(tab)


elif args.action == "url":
    tab = PrettyTable()
    tab.add_column("#", [])
    tab.add_column("Distro", [], align="r")
    tab.add_column("Subversion", [], align="l")
    tab.add_column("Link", [], align="l")
    if args.test:
        tab.add_column("Status", [])
    for (idx, distro, subver) in resolve_requested_distros(requested_distros):
        try:
            url = distro.acquire_url(subver)
        except AttributeError as e:
            print("Error getting URL for ", f"{distro.distro_title}:{subver}")
            print("Encountered", e)
            continue

        if args.minimal:
            print(url)
        else:
            if args.test:
                url = distro.acquire_url(subver)
                res = requests.get(url)
                tab.add_row([idx, distro.distro_title, subver, url, res.status_code])
            else:
                tab.add_row([idx, distro.distro_title, subver, url])

    print(tab)
