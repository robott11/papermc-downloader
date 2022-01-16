import requests
import json

def main():
    request = requests.get("https://papermc.io/api/v2/projects/paper")
    versions = request.json()
    versions = versions["versions"]
    
    for i in range(len(versions)):
        print("("+str(i)+") " + versions[i])

    v = input("Choose your desired version: ")
    if v.isnumeric() == False:
        print("ERRO: Type the version number")
        exit()

    v = int(v)  
    if v > len(versions) or v < 0:
        print("ERRO: Invalid version!")
        exit()    

    version = versions[v]
    print("Choosed version: " + version)

    request = requests.get("https://papermc.io/api/v2/projects/paper/versions/" + version)
    builds = request.json()
    builds = builds["builds"]

    for i in range(len(builds)):
        print("("+str(i)+") " + str(builds[i]))

    b = input("Choose your desired build: ")
    if b.isnumeric() == False:
        print("ERRO: Type build number")
        exit()

    b = int(b)
    if b > len(builds) or b < 0:
        print("ERRO: Invalid number!")
        exit()

    build = str(builds[b])
    print("Choosed build: " + build)

    paperFileName = "paper-"+version+"-"+build+".jar"
    url = "https://papermc.io/api/v2/projects/paper/versions/"+version+"/builds/"+build+"/downloads/"+paperFileName
    print("Downloading " + paperFileName + "...")

    download = requests.get(url, allow_redirects=True)
    open(paperFileName, "wb").write(download.content)

    print("Download finished")    

if __name__ == "__main__":
    main()
