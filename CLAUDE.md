# Wine Life · istruzioni per Claude Code

Pagina Instagram **faceless** "Wine Life" (handle `@winee.life`). Il proprietario è Alessio: scrivigli sempre in italiano, in modo semplice e diretto. Tutto il materiale (brand kit, template, primi 10 post, sistema di pubblicazione) è in questa cartella.

Prima di creare o modificare contenuti leggi `brand-kit/brand-kit.md` (regole) e `brand-kit/tokens.json` (valori esatti). Se una richiesta va contro il brand kit, fallo notare prima di procedere.

## Il brief

Wine Life racconta il vino come stile di vita: emozione, cultura, curiosità, momenti da vivere con un calice in mano.
- Non è una pagina tecnica da sommelier, non è una pagina meme, non mostra mai volti.
- Deve essere elegante, semplice, condivisibile e utile.
- **Target:** 25–55 anni, amano il vino ma non sono esperti. Vogliono capire cosa bere, scegliere, regalare, e vivere il vino in modo più consapevole.
- **Tono:** raffinato, caldo, semplice, evocativo. Elegante ma non snob, poetico ma non finto, educativo ma accessibile. In pratica: "l'amico che ne sa e ti dice cosa ordinare, portare, regalare, in due frasi". Si ferma lo scroll con un'idea forte, mai con un urlo.
- **Vietato:** gergo da sommelier, meme, emoji a pioggia (nelle grafiche zero, in caption al massimo una), oro/damaschi/calici disegnati, foto stock luminose.

## Pilastri e rubriche

| Pilastro | Quota | Rubrica | Obiettivo | Fondo |
|---|---|---|---|---|
| Wine Thoughts | 40% | Un calice di pensieri | condivisioni | Vino (o foto) |
| Wine Facts | 25% | Lo sapevi? | salvataggi | Rosé, numero gigante + sticker "salva per dopo" |
| Wine Focus | 20% | Vino in 30 secondi | autorevolezza | Latte, nome enorme + 4 riquadri (Dove, Sa di, Servilo, Con) |
| Wine Moments | 15% | Wine Life consiglia | salvataggi e identificazione | Foto col flash, titolo in alto, chip in basso |

Formato: post verticali **1080×1350**, singoli o caroselli da **5 slide** (hook → 3 slide Latte → chiusura Vino "salva + segui").

## Brand kit v3 (quello valido)

Storia: la v1 (scura, oro, Bodoni) è stata scartata perché "troppo AI slop"; la v2 piaceva ma aveva troppi serif. **La v3 è quella definitiva**, non tornare indietro.

- **Palette, solo questi 5:** Vino `#5B0E22` · Rosé `#F7B9C4` · Latte `#F5EEE6` · Inchiostro `#150A0D` · Fumo `#A18E92`. Mai testo rosé su latte, mai vino su inchiostro.
- **Font:** Bricolage Grotesque 600–700 per i titoli (tracking −4%, interlinea ~0.95). Instrument Serif Italic **solo per una parola per titolo** (in HTML `<em>…</em>`) e per gli sticker. Geist per testo, pill, chip. Geist Mono per i dati.
- **Scala su 1080:** numero 380–440 px · hook 100–120 · titolo slide 76–90 · testo 40–44 · pill 28–32 · dati 24–26.
- **Logo:** "wine life" tutto minuscolo, "wine" Bricolage 700 + "life" Instrument Serif Italic. Foto profilo: "wl" corsivo vino su cerchio rosé.
- **Layout:** margini 80 px, allineato a sinistra, una cosa enorme per post. Hook max 10 parole, testo max 25 parole per slide. Pill rubrica in alto a sinistra, @handle in basso a sinistra, freccia o contatore in basso a destra. Uno sticker al massimo per post.
- **Foto:** flash diretto, ombre nette, rossi saturi, grana media. Mani sì, volti mai. Prompt AI di base: `direct flash photography, wine glass, deep red, high contrast, film grain, editorial still life, no faces, 4:5`.
- **Feed:** mai due fondi uguali adiacenti, una foto ogni due grafiche, hook leggibile anche in miniatura.

Versione visiva del brand kit: `brand-kit/brand-kit.html` (aprila nel browser).

## Struttura della cartella

```
wine-life/
├── CLAUDE.md                 questo file
├── .claude/skills/nuovo-post/ procedura completa per creare un post (comando /nuovo-post)
├── .github/workflows/        pubblicazione automatica su GitHub Actions
├── brand-kit/                brand-kit.md (regole), tokens.json (valori), brand-kit.html (visivo)
├── templates/                un template HTML per ogni rubrica + wl.css (stile comune) + export.sh
│   └── png/                  anteprime dei template
├── post/                     i primi 10 post: NN-nome/ con gli HTML sorgente
│   ├── foto/                 foto col flash usate nei post
│   ├── png/                  PNG 1080×1350 pronte
│   └── pdf/                  versione PDF (senza foto)
└── pubblicazione/            calendario.json, caption.md, publish.py, png2jpg.py, jpg/
```

Gli HTML dei post usano `../../templates/wl.css`: non toccare `wl.css` se non per cambiare il brand.

## Come si lavora

**Nuovo post:** copia la cartella del template giusto da `templates/` in `post/NN-nome/` (NN = numero progressivo), cambia solo i testi, poi esporta. Nei caroselli aggiorna il contatore (`2/5`) e la barra (`<div class="bars">`: la slide N ha N segmenti `class="on"`). Evidenziatore rosé: `<span class="mark">…</span>`, solo su fondo Latte. Foto: dentro `<div class="photo">` sostituisci il segnaposto con `<img src="../foto/nome.jpg" alt="">`. La procedura passo passo è nello skill `nuovo-post`.

**Esportare in PNG** (dalla radice di `wine-life/`, serve Chrome o Edge e la connessione per i font):
```
bash templates/export.sh post/11-nome      un post  → post/png/
bash templates/export.sh post/*/           tutti i post
bash templates/export.sh                   tutti i template → templates/png/
```
Su Windows lo script trova da solo Chrome o Edge; altrimenti `CHROME="/percorso/chrome.exe" bash templates/export.sh ...`. Dopo l'esportazione **guarda sempre le PNG** prima di dire che sono pronte (testo che esce dai margini, font non caricati).

**Convertire in JPEG** per Instagram (l'API non accetta PNG): `python pubblicazione/png2jpg.py post/png/11-*.png` (serve `pip install pillow`).

**Aggiungere al calendario:** una voce in `pubblicazione/calendario.json` (`id`, `quando` in ora italiana `AAAA-MM-GGTHH:MM`, `rubrica`, `immagini` in ordine, `caption`) e la stessa caption in `pubblicazione/caption.md`. Ritmo: 3 post a settimana, martedì, giovedì e sabato. Rispetta il mix 40/25/20/15 e la regola dei fondi alternati.

**Caption:** prima riga = l'hook (deve reggere prima del "… altro"), poi 1–3 frasi utili o evocative, una sola richiesta finale (salva, manda a qualcuno, commenta), 5 hashtag in fondo con sempre `#winelife`. Esempi in `pubblicazione/caption.md`.

## Calendario dei primi 10 post

| # | Quando | Rubrica | Slide |
|---|---|---|---|
| 01 certe-bottiglie | sab 31/10/2026 21:00 | Un calice di pensieri | 1 |
| 02 temperatura | mar 03/11 18:00 | Lo sapevi? | 5 |
| 03 oltre-il-prosecco | gio 05/11 18:30 | Wine Life consiglia | 5 |
| 04 nebbiolo | sab 07/11 18:30 | Vino in 30 secondi | 5 |
| 05 con-chi-resta | mar 10/11 21:00 | Un calice di pensieri | 1 |
| 06 600-acini | gio 12/11 13:00 | Lo sapevi? | 1 |
| 07 un-viaggio | sab 14/11 21:00 | Un calice di pensieri | 1 |
| 08 cena-a-due | mar 17/11 19:00 | Wine Life consiglia | 1 |
| 09 vermentino | gio 19/11 18:30 | Vino in 30 secondi | 5 |
| 10 il-momento-giusto | sab 21/11 21:00 | Un calice di pensieri | 1 |

Dal 22/11 in poi il calendario è vuoto: i prossimi post sono da creare.

## Pubblicazione automatica: stato al 28/10/2026

**Niente è ancora stato pubblicato.** Il sistema è pronto ma non configurato.

Come funziona: GitHub Actions (`.github/workflows/pubblica.yml`) ogni 30 minuti lancia `pubblicazione/publish.py --due`, che pubblica con la Instagram API (login Instagram, `graph.instagram.com` v23.0) i post arrivati alla loro ora. Le immagini vengono prese da `raw.githubusercontent.com/<utente>/<repo>/<branch>/pubblicazione/jpg/`, per questo **il repository deve essere pubblico**. Lo script scrive `pubblicazione/pubblicati.json` e lo committa, così nessun post esce due volte. Esce al massimo un post per giro.

Cosa manca, in ordine (lo fa Alessio, tu lo guidi):
1. ✅ **Account Instagram professionale:** fatto, è `@winee.life` (Creator).
2. **Token Meta:** su developers.facebook.com crea un'app Business → prodotto Instagram → "API setup with Instagram login" → aggiungi l'account → "Genera token" (permessi `instagram_business_basic` e `instagram_business_content_publish`). `IG_USER_ID` si legge da `https://graph.instagram.com/v23.0/me?fields=user_id,username&access_token=TOKEN`.
3. ✅ **Repository GitHub pubblico:** fatto, è `carnedasosa/wine-life-instagram` (branch `main`), con il workflow attivo. I commit usano l'email noreply di GitHub, non la Gmail.
4. **Secret del repo:** Settings → Secrets and variables → Actions → `IG_ACCESS_TOKEN` e `IG_USER_ID`.
5. **Prova:** Actions → "Pubblica su Instagram" → Run workflow con `post` = `01-certe-bottiglie`, oppure lasciare che esca da solo sabato 31/10 alle 21:00.

Il token dura 60 giorni: si rinnova con `https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=TOKEN` e si aggiorna il secret (promemoria ogni 50 giorni).

Alternativa senza configurazione: programmare i post dall'app Instagram (Impostazioni avanzate → Programma) usando `pubblicazione/jpg/` e `caption.md`.

Prova in locale senza toccare Instagram: `python pubblicazione/publish.py --dry-run --due` oppure `--dry-run --post 04-nebbiolo`.

## Regole di sicurezza

- **Mai** chiedere, stampare o scrivere il token in chat, nei file del repo o nei commit. In locale va in un file `.env` (già in `.gitignore`), su GitHub solo nei Secrets.
- **Non pubblicare nulla su Instagram** senza un via libera esplicito di Alessio per quel post.
- Prima di cambiare l'ora di un post già in calendario o di cancellare un post, chiedi.
