import os, sys, requests

URL = "https://aru-test-center-search.collegeboard.org/prod/test-centers?date=2026-12-05&country=MN"
HEADERS = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}

centers = requests.get(URL, headers=HEADERS, timeout=20).json()
open_now = [c["name"] for c in centers if c.get("seatAvailability")]
print("open:", open_now)

if open_now:
    requests.post(
        f"https://api.telegram.org/bot{os.environ['BOT_TOKEN']}/sendMessage",
        data={"chat_id": os.environ["CHAT_ID"],
              "text": "SAT seat open (Dec 5): " + ", ".join(open_now)},
    )
