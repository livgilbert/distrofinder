from distro_profiles.arch import arch
from distro_profiles.tails import tails
from distro_profiles.ubuntu import ubuntu
from distro_profiles.kali import kali

def get_distros():
    return [
            arch(),
            tails(),
            ubuntu(),
            kali()
            ]

def resolve_requested_distros(requested_distros):
    distros = get_distros()
    idx = 0
    for distro in distros:
        for subver in distro.subversions:
            if "all" in requested_distros or distro.distro_title in requested_distros or f"{distro.distro_title}:{subver}" in requested_distros or str(idx) in requested_distros:
                yield (idx, distro, subver)
            idx += 1
    return distros
