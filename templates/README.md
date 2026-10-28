# Wine Life · Template Instagram (brand kit v3)

Tutti i template sono 1080×1350 (4:5), margini 80 px, fondi e font del brand kit v3 (`../brand-kit/tokens.json`).
I testi nei template sono esempi di impaginazione: i contenuti veri li scriviamo nei prossimi passi (primi 10 post).

## Cosa c'è

| Rubrica | Cartella | Formato | Fondo |
|---|---|---|---|
| Un calice di pensieri | `pensieri-post/` | singolo | Vino |
| Un calice di pensieri | `pensieri-foto/` | singolo su foto (per spezzare il feed) | Foto |
| Lo sapevi? | `losapevi-post/` | singolo, numero gigante + sticker | Rosé |
| Lo sapevi? | `losapevi-carosello/` | 5 slide: hook Rosé → 3 Latte → chiusura Vino | Rosé/Latte/Vino |
| Vino in 30 secondi | `30secondi-carosello/` | 5 slide: nome enorme → scheda 4 riquadri → 2 Latte → chiusura | Latte/Vino |
| Wine Life consiglia | `consiglia-post/` | singolo su foto con chip | Foto |
| Wine Life consiglia | `consiglia-carosello/` | 5 slide: hook su foto → 3 alternative → chiusura | Foto/Latte/Vino |

Le PNG pronte sono in `png/`. Lo stile comune è in `wl.css`: non serve toccarlo.

## Regole da rispettare quando cambi i testi

- Hook max 10 parole, testo max 25 parole per slide.
- Una sola parola per titolo in corsivo: mettila dentro `<em>…</em>`. Il colore lo decide il fondo.
- Evidenziatore rosé su una parola: `<span class="mark">…</span>` (solo su Latte).
- Uno sticker al massimo per post.
- Nei caroselli aggiorna il contatore (`2/5`) e la barra: in `<div class="bars">` la slide N ha N segmenti `class="on"`.

## Come si usano (HTML)

1. Apri lo `slide-N.html` o `post.html` con un editor di testo e cambia solo le parole.
2. Per la foto: dentro `<div class="photo">` sostituisci `<div class="ph">…</div>` con `<img src="tua-foto.jpg" alt="">` (foto 1080×1350 o più grande, flash diretto, niente volti).
3. Esporta dalla radice di `wine-life/`: `bash templates/export.sh` rigenera tutte le PNG dei template, `bash templates/export.sh templates/consiglia-post` solo una cartella, `bash templates/export.sh post/04-nebbiolo` un post (le PNG finiscono in `post/png/`). Serve Chrome (o Edge su Windows) e la connessione (i font arrivano da Google Fonts).

## Se lavori su Canva

Crea un design personalizzato 1080×1350 e ricostruisci ogni template una volta sola, poi duplicalo.

- **Colori** (Brand Kit di Canva): Vino `#5B0E22`, Rosé `#F7B9C4`, Latte `#F5EEE6`, Inchiostro `#150A0D`, Fumo `#A18E92`.
- **Font**: Bricolage Grotesque, Instrument Serif (corsivo), Geist, Geist Mono sono gratuiti su Google Fonts. Se Canva non li ha nel menu, caricali dal Brand Kit (serve Canva Pro). Ripiego senza Pro: un grotesk compatto tipo "Inter Tight" o "Archivo" per i titoli e un serif corsivo tipo "DM Serif Display" per la parola accento.
- **Misure** (in px sul canvas): titolo/hook 110–120, titolo slide 86, numero gigante 440, testo 42, pill 30, dati 25. Interlinea titoli 0.95, spaziatura lettere −40 (Canva usa millesimi).
- **Margini**: guide a 80 px da ogni lato. Pill in alto a sinistra, @handle in basso a sinistra, freccia tonda (diametro 104) in basso a destra.
- **Pill**: rettangolo con angoli 100%, bordo 2 px, testo Geist 30.
- **Sticker**: cerchio 236 px ruotato −10°, testo Instrument Serif corsivo 52.
- **Barra caroselli**: 5 rettangoli alti 6 px a 40 px dal bordo alto, pieni fino alla slide corrente, gli altri al 22% di opacità.
- **Grana**: sopra a tutto un'immagine di rumore (cerca "grain texture" negli elementi) in modalità Sovrapponi al 20%.
- Il modo più rapido: carica le PNG di `png/` come riferimento sotto il tuo design e ricalca.
