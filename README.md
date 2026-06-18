# Strumento di organizzazione file Py

🎯 FileOrganizer è un potente strumento da riga di comando scritto in Python che aiuta a gestire, ordinare, ripulire e analizzare le cartelle locali in modo automatizzato e sicuro.

🔍 Cosa fa

Questo script consente di:
* effettuare l'ordinamento intelligente dei file spostandoli in cartelle dedicate in base alla loro estensione (Documenti, Immagini, Video, Audio, Archivi, Applicazioni, Codice Sorgente, Modelli 3D).
* isolare automaticamente i file con estensioni sconosciute all'interno di una directory protetta chiamata `Altri_File`.
* scansionare e gestire esclusivamente le sottocartelle reali, ignorando i file sfusi presenti nella directory.
* archiviare in blocco tutte le sottocartelle trovate dentro una cartella centrale denominata `ARCHIVIO_CARTELLE`.
* raggruppare e spostare le sottocartelle all'interno di una nuova "Master Cartella" personalizzata dall'utente.
* eseguire una pulizia rapida e la formattazione sicura dell'intera directory di lavoro, rimuovendo file e cartelle in un solo click.
* analizzare nel dettaglio lo spazio totale occupato convertendo i dati in un formato leggibile (*Byte, KB, MB, GB*).
* creare istantaneamente copie di sicurezza (backup) speculari della cartella per non rischiare mai di perdere i propri dati importanti.

🚀 Come si usa

Apri il terminale nella cartella del progetto.
Esegui il file FileOrganizer.py con Python:

python FileOrganizer.py
All'avvio, inserisci il percorso preciso della cartella su cui desideri lavorare. Il sistema verificherà subito che la directory sia esistente e valida.

Nel menu principale puoi scegliere tra le opzioni disponibili:

oi: avvia l'ordinamento automatico e intelligente di tutti i file presenti nella cartella.

sc: accede al sottomenu dedicato alla gestione e archiviazione delle sole sottocartelle.

fc: permette di formattare velocemente la directory eliminando ogni file e sottocartella in essa contenuti.

ad: mostra un report analitico profondo con il conteggio di file, cartelle e lo spazio totale occupato sul disco.

cs: crea una copia di backup esatta della cartella di lavoro, posizionandola in sicurezza nella directory madre.

e: chiude in modo sicuro i processi ed esce dal programma.

🧠 Dettagli tecnici

Lo script utilizza esclusivamente moduli nativi della libreria standard di Python, garantendo la massima compatibilità senza richiedere installazioni di terze parti:

os: utilizzato per mappare i percorsi, verificare la validità delle cartelle, scansionare l'albero delle directory con os.walk e calcolare i pesi dei singoli file.

shutil: impiegato per le operazioni ad alto livello sui file, come il trasferimento sicuro (shutil.move), la clonazione di alberi di directory per il backup (shutil.copytree) e la rimozione forzata (shutil.rmtree).

sys: sfruttato per gestire la terminazione pulita dello script all'uscita dell'utente.

Il sistema include una robusta gestione delle eccezioni (PermissionError, FileNotFoundError, OSError), assicurando che il programma non crashi mai in caso di file di sistema protetti o bloccati, notificando l'utente e proseguendo il lavoro.

💡 Esempio d'uso

Avvia il programma e digita il percorso della tua cartella disordinata (es: C:\Utenti\Nome\Download).

Scegli l'opzione oi dal menu principale.

Il programma mostrerà a schermo l'elenco dei file rilevati con le relative estensioni e li sposterà in tempo reale.

Al termine del processo, all'interno della cartella troverai i tuoi file perfettamente suddivisi in cartelle ordinate come Documenti, Immagini, Codice_Sorgente o Altri_File.

🛠️ Possibili modifiche future

Questa versione è già estremamente stabile e performante, ma può essere espansa con nuove funzioni avanzate:

implementare un sistema di logging automatico su file .log per tenere traccia di ogni file spostato o eliminato.

aggiungere filtri temporali (es: ordina o elimina solo i file creati più di 30 giorni fa).

includere la gestione dei file duplicati, confrontandone le dimensioni o l'hash per eliminare i doppioni che sprecano spazio.

sviluppare un'interfaccia grafica moderna (GUI) in aggiunta alla modalità da riga di comando.

integrare un sistema di compressione automatico che converte in formato .zip o .rar le cartelle archiviate.

✅ Perché usare

è nativo, leggero e sicuro: non richiede pacchetti esterni o connessione internet.

previene le distrazioni dell'utente convertendo gli input e accettando percorsi puliti dalle virgolette.

gestisce gli imprevisti di sistema legati ai permessi di amministratore senza interrompere l'esecuzione.

la struttura visiva da terminale è chiara, geometrica e piacevole da leggere.

📌 Nota importante

Questo strumento opera modifiche dirette sui file presenti sul disco fisso (spostamenti ed eliminazioni). Si consiglia di utilizzare l'opzione cs (Copia di Sicurezza) prima di effettuare operazioni di pulizia radicale (fc).

✨ Suggerimenti per contributori GitHub

espandere i dizionari delle estensioni inserendo formati multimediali o professionali più rari.

perfezionare la formattazione dei messaggi di errore rendendoli ancora più descrittivi.

ottimizzare i processi di scansione per incrementare la velocità di analisi su directory con decine di migliaia di file.

Buon lavoro con FileOrganizer! 🖥️📂
