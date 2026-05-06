import os, requests, json

url = f"{os.getenv('SN_INSTANCE')}/api/now/table/incident"
auth = (os.getenv("SN_USER"), os.getenv("SN_PASS"))

params = {"sysparm_limit": 100}

res = requests.get(url, auth=auth, params=params)
data = res.json()["result"]

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/incidents.json", "w") as f:
    json.dump(data, f, indent=2)

print("Fetched incidents")