class Distro:
    def __init__(this, distro_title: str, primary_url: str, subversions: list[str]): 
        this.distro_title = distro_title
        this.primary_url = primary_url
        this.subversions = subversions

    def download_file(this, subversion: str) -> str:
        try:
            url:str = this.acquire_url(subversion)
            return url

        except Exception as e:
            print(f"Error dowloading distro {this.distro_title} ({subversion})")
            raise e
