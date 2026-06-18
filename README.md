# FileOrganizer

🎯 **FileOrganizer** è un piccolo strumento da riga di comando scritto in Python che aiuta a organizzare, gestire e analizzare i file e le cartelle in una directory.

## 🔍 Cosa fa

Questo script permette di:

- ordinare i file in cartelle per *categoria* in base alla loro *estensione*
- identificare automaticamente il *tipo di file* (Documenti, Immagini, Video, Audio, ecc.)
- gestire e *spostare le sottocartelle* in un'unica cartella di archiviazione
- *rinominare* le sottocartelle in modo personalizzato
- effettuare una *pulizia rapida* e *formattazione veloce* della directory
- analizzare lo *spazio totale occupato* da file e cartelle
- creare automaticamente *copie di sicurezza* (backup) della directory

## 🚀 Come si usa

1. Apri il terminale nella cartella del progetto.
2. Esegui il file `FileOrganizer.py` con Python:

```bash
python FileOrganizer.py
```

3. Il programma ti chiederà di inserire il percorso della directory da organizzare.
4. Nel menu principale puoi scegliere:

- `oi` : ordinamento file INTELLIGENTE per categoria e estensione
- `sc` : gestione SOLO cartelle (sposta o rinomina le sottocartelle)
- `fc` : pulizia rapida / formattazione veloce della directory
- `ad` : analisi dettagliata dello spazio occupato
- `cs` : copia di sicurezza (backup)
- `e` : esci dal programma

## 🧠 Dettagli tecnici

Lo script utilizza i moduli Python standard `os` e `shutil` per gestire file e cartelle in modo affidabile.

### Categorie supportate

- **Documenti**: `.txt`, `.pdf`, `.doc`, `.docx`, `.odt`, `.rtf`, `.xls`, `.xlsx`, `.ods`, `.csv`, `.ppt`, `.pptx`, `.odp`, `.epub`, `.mobi`, `.azw3`
- **Immagini**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`, `.svg`, `.ai`, `.eps`, `.psd`, `.xcf`, `.ico`
- **Video**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.mpeg`, `.3gp`, `.webm`
- **Audio**: `.mp3`, `.wav`, `.wma`, `.ogg`, `.flac`, `.m4a`, `.aac`, `.mid`
- **Archivi**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.iso`
- **Applicazioni e Installatori**: `.exe`, `.msi`, `.apk`, `.bat`, `.cmd`, `.sh`
- **Codice Sorgente**: `.py`, `.pyw`, `.html`, `.htm`, `.css`, `.js`, `.ts`, `.c`, `.cpp`, `.h`, `.hpp`, `.java`, `.cs`, `.json`, `.xml`, `.yaml`, `.yml`
- **Modelli 3D**: `.stl`, `.obj`, `.fbx`, `.3ds`
- **File sconosciuti**: vengono spostati automaticamente in una cartella `Altri_File`

### Funzioni principali

- **Ordinamento Intelligente (oi)**: scandisce la directory, identifica ogni file e lo sposta nella cartella appropriata
- **Gestione Cartelle (sc)**: consente di raggruppare le sottocartelle o rinominarle con un nome personalizzato
- **Pulizia Formattazione (fc)**: elimina tutto il contenuto della directory dopo conferma dell'utente
- **Analisi Dettagliata (ad)**: conta file e cartelle, calcola lo spazio totale in Byte, KB, MB o GB
- **Backup (cs)**: crea una copia completa della directory con suffisso `_BACKUP`

## 💡 Esempio d'uso

- Esegui il programma
- Inserisci il percorso: `C:\Users\TuoNome\Desktop\FilesDaOrganizzare`
- Scegli `oi` per ordinare i file
- Il programma creerà automaticamente le cartelle necessarie e sposterà i file

Il programma mostrerà:

- Elenco di tutti i file trovati
- Categoria e estensione di ciascun file
- Conferma dello spostamento con emoji 🚚
- Avvisi per file sconosciuti

## 🛠️ Possibili modifiche future

Questa versione è già utile, ma può essere migliorata per diventare uno strumento ancora più completo per gli utenti:

- aggiungere la ricerca **ricorsiva avanzata** con filtri per nome file e data di modifica
- includere il supporto per **regole personalizzate** salvabili in file di configurazione
- implementare la **rinomina in batch** di file con pattern specifici
- aggiungere un'interfaccia a menu più moderna con **colori ANSI** e output formattato
- salvare i report di analisi su file `.txt` o `.csv`
- supportare il caricamento di **profili di organizzazione** pre-configurati
- implementare un sistema di **log dettagliato** di tutte le operazioni effettuate
- aggiungere la possibilità di **annullare le operazioni** (undo)
- supportare la ricerca e l'eliminazione di **file duplicati**
- integrare il monitoraggio di **cartelle in tempo reale** con auto-organizzazione

## ✅ Perché usarlo

- è facile da usare anche per chi non è esperto
- fornisce risultati completi e leggibili con emoji e messaggi informativi
- è utile per chi vuole mantenere il PC ordinato e organizzato
- il menu è strutturato e guidato step-by-step
- supporta moltissime estensioni di file diverse
- è perfetto per pulire desktop e cartelle Download

## 📌 Nota importante

Questo strumento è pensato per gestire directory locali su Windows, macOS e Linux. Usalo con cautela quando esegui la pulizia (fc) in quanto l'operazione è irreversibile.

## ✨ Suggerimenti per contributori GitHub

- migliorare i messaggi di errore con più dettagli diagnostici
- aggiungere controlli più robusti per permessi e accessi negati
- introdurre funzionalità di **sincronizzazione** tra cartelle
- creare una versione con output in **HTML** formattato con tabelle e grafici
- aggiungere il supporto per **cloud storage** (Google Drive, OneDrive, ecc.)

Buon lavoro con `FileOrganizer`! 🖥️📁

