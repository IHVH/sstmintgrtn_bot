import requests

OWNER = "IHVH"
REPO = "OEMIB_PI01_19_TBOT"
URL = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

HEADER = {"Accept":"application/vnd.github+json", 
          "X-GitHub-Api-Version": "2022-11-28" } 

PARAM = {"per_page":5, "page":1}

response = requests.get(URL, params=PARAM, headers=HEADER)

if(response.ok):
    resp = response.json()
    
    for issue in resp:
        
        html = issue["html_url"]
        title = issue["title"]
        body = issue["body"]
        user = issue["user"]
        login = user["login"]
        print(f"{login} \n{title} \n{body} \n{html}")
    
else:
    print(response)
    print(response.text)