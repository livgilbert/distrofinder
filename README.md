# distrofinder

Early in development

## Usage

`python main.py list`: List info for all distros

`python main.py url -d <distros>`: Get latest download for distros. Distros can be specified by 

- the index provided by `list`    
- the name of the distro (will return all subversions)
- distro and subversion provided in `name:subversion` format  

There are also the `-m` (minimal) and `-t` (test) flags. The `-m` will print only the URLs (useful for piping to a file) and `-t` will make a network request to the file in order to determine if the link is valid. 

## Adding a distro

Add the file in the `distro_profiles` directory with a class that extends the `Distro` template.
The class needs to specify the `acquire_url` method which takes in the `subversion` parameter (as well as `this`). It should return a string.

The file also needs a function that returns an initialized instance of the class. Initialization takes 3 parameters: 
- `distro_title`: name of the distro
- `primary_url`: URL of the download page
- `subversions`: array of valid subversions of the distro 

## todo
- support downloading the torrents
- support querying older versions
- cache the responses of download pages when getting urls for multiple subversions
- improve output formatting
