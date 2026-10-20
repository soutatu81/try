import os, json, datetime, pathlib, requests

WOEID_JAPAN = 23424856
url = f"https://api.x.com/2/trends/by/woeid/{WOEID_JAPAN}"
headers = {"Authorization": f"Bearer {os.environ['X_BEARER_TOKEN']}"}

r = requests.get(url, headers=headers, timeout=30)
r.raise_for_status()

now = datetime.datetime.now(datetime.timezone.utc)
record = {"fetched_at": now.isoformat(), "data": r.json()}

path = pathlib.Path("logs") / f"{now:%Y-%m-%d}.jsonl"
path.parent.mkdir(exist_ok=True)
with path.open("a", encoding="utf-8") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
