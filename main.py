from distro_profiles import resolve_requested_distros
import requests
import argparse

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
    # for listing we want default to be all
    if requested_distros == [''] or len(requested_distros) == 0:
        requested_distros = ["all"]

    for (idx, distro, subver) in resolve_requested_distros(requested_distros):
        print(idx, f"{distro.distro_title}:{subver}", distro.primary_url, sep="\t")

    idx = 0

elif args.action == "url":
    for (idx, distro, subver) in resolve_requested_distros(requested_distros):
        if args.minimal:
            print(distro.acquire_url(subver))
        else:
            if args.test:
                url = distro.acquire_url(subver)
                res = requests.get(url)
                print(res.status_code, end=" ")
            print(f"{idx}", f"{distro.distro_title}:{subver}", distro.acquire_url(subver), sep="\t")
