#!/usr/bin/env python3
"""Salva il token Instagram nei secret del repo GitHub, senza mostrarlo a schermo.

Chiede il token (non si vede mentre lo incolli), legge user_id e username da
Instagram, poi imposta i secret IG_ACCESS_TOKEN e IG_USER_ID con la CLI `gh`.
Il token non viene scritto in nessun file.

Uso (dalla radice di wine-life):
  python pubblicazione/imposta_token.py
"""
import getpass
import json
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = "carnedasosa/wine-life-instagram"
API = "https://graph.instagram.com/v23.0"

token = getpass.getpass("Incolla il token e premi Invio (non si vede): ").strip()
if not token:
    sys.exit("Nessun token inserito.")

url = f"{API}/me?" + urllib.parse.urlencode({"fields": "user_id,username", "access_token": token})
try:
    with urllib.request.urlopen(url, timeout=30) as r:
        me = json.load(r)
except urllib.error.HTTPError as e:
    sys.exit(f"Instagram ha rifiutato il token ({e.code}). Rigeneralo e riprova.")

user_id, username = str(me["user_id"]), me.get("username", "?")
print(f"Token valido per @{username} (user_id {user_id}).")
if input("Salvo i secret su GitHub? [s/N] ").strip().lower() != "s":
    sys.exit("Annullato, niente salvato.")

for name, value in (("IG_ACCESS_TOKEN", token), ("IG_USER_ID", user_id)):
    subprocess.run(["gh", "secret", "set", name, "-R", REPO], input=value, text=True, check=True)
print("Fatto: IG_ACCESS_TOKEN e IG_USER_ID salvati nei secret del repo.")
