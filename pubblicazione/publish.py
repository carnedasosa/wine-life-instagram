#!/usr/bin/env python3
"""Pubblica i post di Wine Life su Instagram leggendo calendario.json.

Usa la Instagram API con login Instagram (graph.instagram.com): serve un account
Professional (Creator o Business), niente Pagina Facebook.

Variabili d'ambiente:
  IG_USER_ID       id dell'account Instagram (dal token, vedi README)
  IG_ACCESS_TOKEN  token di lunga durata con permesso instagram_business_content_publish
  IMAGE_BASE_URL   URL pubblico della cartella jpg/, es. https://raw.githubusercontent.com/<utente>/<repo>/main/jpg

Esempi:
  python3 publish.py --dry-run --due     # mostra cosa uscirebbe adesso, senza toccare Instagram
  python3 publish.py --due               # pubblica i post arrivati alla loro ora e non ancora usciti
  python3 publish.py --post 01-certe-bottiglie   # pubblica subito un post preciso
  python3 publish.py --check --post 23-mercoledi # prepara il post su Instagram ma NON lo pubblica
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

API = "https://graph.instagram.com/v23.0"
HERE = Path(__file__).resolve().parent
CALENDARIO = HERE / "calendario.json"
STATO = HERE / "pubblicati.json"


def call(method, path, **params):
    params["access_token"] = os.environ["IG_ACCESS_TOKEN"]
    data = urllib.parse.urlencode(params).encode()
    url = f"{API}/{path}"
    if method == "GET":
        req = urllib.request.Request(f"{url}?{data.decode()}")
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Errore API {e.code} su {path}: {e.read().decode()}")


def wait_ready(container_id):
    # Instagram scarica e valida l'immagine in modo asincrono.
    for _ in range(30):
        status = call("GET", container_id, fields="status_code")["status_code"]
        if status == "FINISHED":
            return
        if status in ("ERROR", "EXPIRED"):
            sys.exit(f"Container {container_id} in stato {status}")
        time.sleep(5)
    sys.exit(f"Container {container_id} non pronto dopo 150 secondi")


def publish(post, dry_run, check=False):
    user = os.environ.get("IG_USER_ID", "<IG_USER_ID>")
    base = os.environ.get("IMAGE_BASE_URL", "<IMAGE_BASE_URL>").rstrip("/")
    urls = [f"{base}/{name}" for name in post["immagini"]]
    kind = "carosello" if len(urls) > 1 else "singolo"
    print(f"→ {post['id']} ({kind}, {len(urls)} immagini)")
    if dry_run:
        for u in urls:
            print(f"   {u}")
        print("   caption: " + post["caption"].splitlines()[0])
        return None

    if len(urls) == 1:
        container = call("POST", f"{user}/media", image_url=urls[0], caption=post["caption"])["id"]
    else:
        children = []
        for u in urls:
            child = call("POST", f"{user}/media", image_url=u, is_carousel_item="true")["id"]
            wait_ready(child)
            children.append(child)
        container = call("POST", f"{user}/media", media_type="CAROUSEL",
                         children=",".join(children), caption=post["caption"])["id"]
    wait_ready(container)
    if check:
        # Instagram ha scaricato e accettato le immagini: senza media_publish il container scade da solo.
        print(f"   verifica ok: container {container} pronto, NON pubblicato")
        return None
    media_id = call("POST", f"{user}/media_publish", creation_id=container)["id"]
    print(f"   pubblicato, media id {media_id}")
    return media_id


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--due", action="store_true", help="pubblica i post la cui ora è passata")
    p.add_argument("--post", help="pubblica subito il post con questo id")
    p.add_argument("--dry-run", action="store_true", help="non chiama Instagram")
    p.add_argument("--check", action="store_true", help="con --post: prepara il post su Instagram senza pubblicarlo")
    args = p.parse_args()
    if not (args.due or args.post):
        p.error("serve --due oppure --post ID")
    if args.check and not args.post:
        p.error("--check va usato con --post ID")

    cal = json.loads(CALENDARIO.read_text(encoding="utf-8"))
    tz = ZoneInfo(cal["fuso_orario"])
    done = json.loads(STATO.read_text(encoding="utf-8")) if STATO.exists() else {}
    now = datetime.now(tz)

    if args.post:
        todo = [x for x in cal["post"] if x["id"] == args.post]
        if not todo:
            sys.exit(f"Nessun post con id {args.post}")
        if args.post in done:
            sys.exit(f"{args.post} è già stato pubblicato il {done[args.post]['pubblicato']}")
    else:
        todo = [x for x in cal["post"]
                if x["id"] not in done
                and datetime.fromisoformat(x["quando"]).replace(tzinfo=tz) <= now]
        # Uno per giro: se il cron è rimasto fermo, i post arretrati escono distanziati.
        todo = todo[:1]
    if not todo:
        print("Niente da pubblicare adesso.")
        return
    if not args.dry_run:
        for var in ("IG_USER_ID", "IG_ACCESS_TOKEN", "IMAGE_BASE_URL"):
            if not os.environ.get(var):
                sys.exit(f"Manca la variabile {var}")

    for post in todo:
        if post["id"] in done and not args.post:
            continue
        media_id = publish(post, args.dry_run, args.check)
        if media_id:
            done[post["id"]] = {"media_id": media_id, "pubblicato": datetime.now(tz).isoformat(timespec="minutes")}
            STATO.write_text(json.dumps(done, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
