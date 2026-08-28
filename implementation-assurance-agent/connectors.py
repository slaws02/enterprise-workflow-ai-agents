import json
from pathlib import Path

BASE=Path(__file__).parent / "data"

def _load(name):
    with open(BASE / name, "r", encoding="utf-8") as f:
        return json.load(f)

def get_client(): return _load("client.json")
def get_journey_tests(): return _load("journey_tests.json")
