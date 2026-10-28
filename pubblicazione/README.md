# Wine Life · Pubblicazione automatica

Cosa c'è qui:

- `jpg/`: le 26 slide in JPEG 1080×1350 (l'API di Instagram accetta solo JPEG, non PNG).
- `calendario.json`: data, ora, immagini e caption di ogni post. È l'unico file da toccare per aggiungere post.
- `caption.md`: le stesse caption e il calendario in forma leggibile, da copiare a mano se serve.
- `publish.py`: pubblica i post via API (solo libreria standard di Python, niente da installare).
- `../.github/workflows/pubblica.yml` (alla radice del repo): fa girare `publish.py --due` ogni 30 minuti su GitHub Actions.
- `pubblicati.json`: lo crea lo script, tiene traccia di cosa è già uscito, così niente esce due volte.

## Strada A, automatica: API + GitHub Actions

Una volta configurata, basta aggiungere immagini in `jpg/` e una voce in `calendario.json`: i post escono da soli all'ora scritta.

### 1. Account Instagram professionale
App Instagram → Impostazioni → Tipo di account e strumenti → Passa a un account professionale → Creator (o Business). Gratis, nessuna Pagina Facebook necessaria.

### 2. App Meta e token
1. Su developers.facebook.com crea un'app di tipo **Business** e aggiungi il prodotto **Instagram** → "API setup with Instagram login".
2. In "Generate access tokens" aggiungi il tuo account Instagram (devi accettare l'invito da Instagram → Impostazioni → App e siti web → Inviti tester).
3. Genera il token: è già di lunga durata (60 giorni). Permessi necessari: `instagram_business_basic` e `instagram_business_content_publish`.
4. Recupera il tuo id: apri `https://graph.instagram.com/v23.0/me?fields=user_id,username&access_token=IL_TUO_TOKEN` e copia `user_id`.

Finché pubblichi solo sul tuo account, l'app può restare in modalità sviluppo: non serve la revisione di Meta.

### 3. Repository GitHub
1. Crea un repository **pubblico** (serve perché Instagram scarica le immagini da un URL pubblico) e carica tutta la cartella `wine-life/`, compresa `.github/` alla radice.
2. Settings → Secrets and variables → Actions → aggiungi `IG_USER_ID` e `IG_ACCESS_TOKEN`.
3. Actions → "Pubblica su Instagram" → Run workflow per una prova: con nessun post scaduto stampa "Niente da pubblicare adesso".

Le immagini restano visibili nel repo prima dell'uscita: per una pagina di contenuti va bene, ma tienilo presente.

### Rinnovo del token
Il token scade dopo 60 giorni. Si rinnova (se ha almeno 24 ore) aprendo
`https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=IL_TUO_TOKEN`
e sostituendo il secret. Mettiti un promemoria ogni 50 giorni.

### Prova in locale
```
python3 publish.py --dry-run --due          # cosa uscirebbe adesso
python3 publish.py --dry-run --post 04-nebbiolo
```
Con le tre variabili d'ambiente impostate e senza `--dry-run`, `--post ID` pubblica subito quel post.

## Strada B, senza configurazione: programmazione dall'app

Se non vuoi fare la parte tecnica: l'app Instagram (prima di condividere: Impostazioni avanzate → Programma questo post) o Meta Business Suite, se colleghi l'account a Facebook, permettono di programmare post singoli e caroselli fino a 75 giorni prima. Carichi le immagini di `jpg/` nell'ordine, incolli la caption da `caption.md`, scegli data e ora. Per 10 post sono circa 15 minuti, una volta per ciclo. Richiede comunque l'account professionale (punto 1).
