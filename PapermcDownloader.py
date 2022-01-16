#!/usr/bin/python
import requests
import json
from colorama import init
from colorama import Fore, Back, Style

def main():
    init()
    
    request = requests.get("https://papermc.io/api/v2/projects/paper")
    versions = request.json()
    versions = versions["versions"]
    
    for i in range(len(versions)):
        print(Fore.GREEN + "["+str(i)+"] " + Fore.WHITE + versions[i])

    v = input("Choose your desired version: ")
    if v.isnumeric() == False:
        print(Fore.RED + "ERROR: Type the version number")
        exit()

    v = int(v)  
    if v > len(versions) or v < 0:
        print(Fore.RED + "ERROR: Invalid version!")
        exit()    

    version = versions[v]
    print(Fore.BLUE + "Choosed version: " + version)

    request = requests.get("https://papermc.io/api/v2/projects/paper/versions/" + version)
    builds = request.json()
    builds = builds["builds"]

    for i in range(len(builds)):
        print(Fore.GREEN + "["+str(i)+"] " + Fore.WHITE  + str(builds[i]))

    b = input("Choose your desired build: ")
    if b.isnumeric() == False:
        print(Fore.RED + "ERROR: Type build number")
        exit()

    b = int(b)
    if b > len(builds) or b < 0:
        print(Fore.RED + "ERROR: Invalid number!")
        exit()

    build = str(builds[b])
    print(Fore.BLUE + "Choosed build: " + build)

    paperFileName = "paper-"+version+"-"+build+".jar"
    url = "https://papermc.io/api/v2/projects/paper/versions/"+version+"/builds/"+build+"/downloads/"+paperFileName
    print(Fore.YELLOW + "Generated URL: " + url)
    print(Fore.GREEN + "Downloading " + paperFileName + "...")

    download = requests.get(url, allow_redirects=True)
    open(paperFileName, "wb").write(download.content)

    print("Download finished")    

if __name__ == "__main__":
    main()
