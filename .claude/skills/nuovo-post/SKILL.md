---
name: nuovo-post
description: Crea un nuovo post o carosello Wine Life completo (grafica dai template, PNG, JPEG, caption e voce di calendario). Usalo quando Alessio chiede un post, un carosello, "i post della settimana" o un'idea da trasformare in contenuto.
---

# Nuovo post Wine Life

Segui questi passi in ordine. Le regole di brand sono in `CLAUDE.md` e `brand-kit/brand-kit.md`: rileggile se non le hai in mente.

## 1. Scegli rubrica e slot
- Guarda `pubblicazione/calendario.json`: trova il prossimo martedì, giovedì o sabato libero e il numero progressivo (`NN`) dopo l'ultimo.
- Scegli la rubrica in modo da avvicinarti al mix 40/25/20/15 (Pensieri / Lo sapevi? / Vino in 30 secondi / Consiglia) e da **non mettere due fondi uguali uno dopo l'altro** rispetto al post precedente nel calendario.
- Se Alessio non ha dato un tema, proponi 2–3 idee in una riga ciascuna e fai scegliere.

## 2. Scrivi i testi
- Hook: max 10 parole, un'idea forte, niente punto esclamativo. Una sola parola in corsivo (`<em>`).
- Testo per slide: max 25 parole. Zero emoji nelle grafiche.
- Fatti (temperature, denominazioni, vitigni, numeri): devono essere corretti. Se non sei sicuro, verificali prima di scriverli.

## 3. Crea la grafica
- Copia la cartella del template da `templates/` a `post/NN-nome-breve/`:
  - Pensieri: `pensieri-post` (fondo Vino) o `pensieri-foto` (su foto)
  - Lo sapevi?: `losapevi-post` o `losapevi-carosello`
  - Vino in 30 secondi: `30secondi-carosello`
  - Consiglia: `consiglia-post` o `consiglia-carosello`
- Negli HTML cambia il percorso del CSS in `../../templates/wl.css` e il `<title>`.
- Cambia solo i testi. Caroselli: contatore `N/5` e N segmenti `class="on"` nella barra.
- Foto: metti il file in `post/foto/` e usa `<img src="../foto/nome.jpg" alt="">` dentro `<div class="photo">`. Se manca una foto, scrivi ad Alessio il prompt da usare (vedi CLAUDE.md, sezione Foto).

## 4. Esporta e controlla
```
bash templates/export.sh post/NN-nome-breve
python pubblicazione/png2jpg.py post/png/NN-nome-breve-*.png
```
Apri **ogni** PNG generata e controlla: testo dentro i margini, font giusti (Bricolage per i titoli, non un font di sistema), una sola parola in corsivo, contrasti permessi. Se qualcosa non va, correggi l'HTML e riesporta.

## 5. Caption e calendario
- Caption: prima riga = hook; 1–3 frasi; una sola richiesta finale (salva / manda a qualcuno / commenta); 5 hashtag, sempre `#winelife`. Al massimo una emoji.
- Aggiungi la voce in `pubblicazione/calendario.json` (`id` = nome cartella, `quando` = `AAAA-MM-GGTHH:MM` ora italiana, `rubrica`, `immagini` = i JPEG in ordine, `caption`).
- Aggiungi la stessa caption e la riga di tabella in `pubblicazione/caption.md`.
- Verifica: `python pubblicazione/publish.py --dry-run --post NN-nome-breve`.

## 6. Consegna
Mostra ad Alessio le PNG e la caption, e ricorda data e ora di uscita. Se il repo è su GitHub, fai commit e push solo dopo il suo ok: dal push in poi il post uscirà da solo all'ora indicata.
