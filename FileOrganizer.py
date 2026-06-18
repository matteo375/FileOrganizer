import os
import shutil
import sys

# 📄 Categoria Documenti
dizionario_documenti = {
    ".txt": "Documenti", ".pdf": "Documenti", ".doc": "Documenti", 
    ".docx": "Documenti", ".odt": "Documenti", ".rtf": "Documenti",
    ".xls": "Documenti", ".xlsx": "Documenti", ".ods": "Documenti", 
    ".csv": "Documenti", ".ppt": "Documenti", ".pptx": "Documenti", 
    ".odp": "Documenti", ".epub": "Documenti", ".mobi": "Documenti", 
    ".azw3": "Documenti"
}

# 🖼️ Categoria Immagini
dizionario_immagini = {
    ".jpg": "Immagini", ".jpeg": "Immagini", ".png": "Immagini", 
    ".gif": "Immagini", ".bmp": "Immagini", ".tiff": "Immagini", 
    ".webp": "Immagini", ".svg": "Immagini", ".ai": "Immagini", 
    ".eps": "Immagini", ".psd": "Immagini", ".xcf": "Immagini", 
    ".ico": "Immagini"
}

# 🎬 Categoria Video
dizionario_video = {
    ".mp4": "Video", ".mkv": "Video", ".avi": "Video", 
    ".mov": "Video", ".wmv": "Video", ".flv": "Video", 
    ".mpeg": "Video", ".3gp": "Video", ".webm": "Video"
}

# 🎵 Categoria Audio
dizionario_audio = {
    ".mp3": "Audio", ".wav": "Audio", ".wma": "Audio", 
    ".ogg": "Audio", ".flac": "Audio", ".m4a": "Audio", 
    ".aac": "Audio", ".mid": "Audio"
}

# 📦 Categoria Archivi
dizionario_archivi = {
    ".zip": "Archivi", ".rar": "Archivi", ".7z": "Archivi", 
    ".tar": "Archivi", ".gz": "Archivi", ".iso": "Archivi"
}

# ⚙️ Categoria Applicazioni e Installatori
dizionario_applicazioni = {
    ".exe": "Applicazioni_e_Installatori", ".msi": "Applicazioni_e_Installatori", 
    ".apk": "Applicazioni_e_Installatori", ".bat": "Applicazioni_e_Installatori", 
    ".cmd": "Applicazioni_e_Installatori", ".sh": "Applicazioni_e_Installatori"
}

# 💻 Categoria Codice Sorgente
dizionario_codice = {
    ".py": "Codice_Sorgente", ".pyw": "Codice_Sorgente", ".html": "Codice_Sorgente", 
    ".htm": "Codice_Sorgente", ".css": "Codice_Sorgente", ".js": "Codice_Sorgente", 
    ".ts": "Codice_Sorgente", ".c": "Codice_Sorgente", ".cpp": "Codice_Sorgente", 
    ".h": "Codice_Sorgente", ".hpp": "Codice_Sorgente", ".java": "Codice_Sorgente", 
    ".cs": "Codice_Sorgente", ".json": "Codice_Sorgente", ".xml": "Codice_Sorgente", 
    ".yaml": "Codice_Sorgente", ".yml": "Codice_Sorgente"
}

# 🌀 Categoria Modelli 3D
dizionario_modelli3d = {
    ".stl": "Modelli_3D", ".obj": "Modelli_3D", ".fbx": "Modelli_3D", 
    ".3ds": "Modelli_3D"
}

# Uniamo tutti i mini-dizionari in un'unica grande mappa globale delle regole
regoleSmistamento = {**dizionario_documenti, **dizionario_immagini, **dizionario_video, **dizionario_audio, **dizionario_archivi, **dizionario_applicazioni, **dizionario_codice, **dizionario_modelli3d}

print(r"""
███████╗██╗██╗     ███████╗ ██████╗ ██████╗  ██████╗  █████╗ ███╗   ██╗██╗███████╗███████╗██████╗ 
██╔════╝██║██║     ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔══██╗████╗  ██║██║╚══███╔╝██╔════╝██╔══██╗
█████╗  ██║██║     █████╗  ██║   ██║██████╔╝██║  ███╗███████║██╔██╗ ██║██║  ███╔╝ █████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══██║██║╚██╗██║██║ ███╔╝  ██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║ ╚████║██║███████╗███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
""")

print("\n---------- AVVIO TUTTI I SISTEMI E MOSTRO L'OBBIETTIVO DEL TOOL... ----------")
print(r"""ℹ️ INFO: Utente, benvenuto nel nostro programma! Qui potrai effettuare: 
    • l'ordinamento intelligente dei file per estensione, 
    • la gestione, rinomina e archiviazione delle sottocartelle, 
    • la pulizia rapida e la formattazione sicura della directory, 
    • l'analisi dettagliata dello spazio totale occupato,
    • la creazione automatica di copie di sicurezza (backup).
(sulla directory precisa che hai inserito inizialmente).""")
print("-----------------------------------------------------------------------------")

def copiaSicurezza(directoryDaCopiare):
    print("\n---------- AVVIO DEL SISTEMA ('cs') IN CORSO... ----------")
    print(f"ℹ️ INFO: Utente la directory da te inserita inizialmente ({directoryDaCopiare}) sarà quella che verrà salvata come BACKUP.")
    macroCartella = os.path.dirname(directoryDaCopiare) ## Per capire qual è la cartella che contiene tutto.
    nomeCartellaOriginale = os.path.basename(directoryDaCopiare)
    nomeBackup = "_BACKUP"
    nuovoNomeCartella = nomeCartellaOriginale + nomeBackup
    percorsoDestinazioneBackup = os.path.join(macroCartella, nuovoNomeCartella)

    try:
        shutil.copytree(directoryDaCopiare, percorsoDestinazioneBackup)
        print("✅ SUCCESS: Copia di sicurezza creata con successo ora tutti i tuoi FILE sono al sicuro.")
    except FileExistsError:
        print("⚠️ ATTENZIONE: Esiste già una cartella di backup in questo percorso, ci dispiace.")
    except OSError as e:
        print(f"❌ ERROR: Utente impossibile creare la copia di backup. Errore di sistema: {e}")

while True:
    sceltaPercorso = input("> Utente ti chiediamo di inserire la directory precisa dove lavorare: ").strip('"')
    if os.path.exists(sceltaPercorso) and os.path.isdir(sceltaPercorso):
        print("✅ SUCCESS: Directory validata e verificata con successo puoi procedere...")
        break
    else:
        if not os.path.exists(sceltaPercorso):
            print("❌ ERROR: Il percorso inserito non esiste. Controlla di non aver fatto errori di battitura.")
        else:
            print("❌ ERROR: Il percorso inserito punta a un file, ma il programma richiede una cartella.")
        continue

while True:
    print("\n---------- CARICAMENTO MENU PRINCIPALE... ----------")
    print(r"""1. oi  /  🧠 Ordinamento file INTELLIGENTE
2. sc  /  📁 Gestione SOLO cartelle
3. fc  /  ⚡ Pulizia rapida / Formattazzione veloce DELLA DIRECTORY
4. ad  /  📊 Analisi dettagliata
5. cs  /  🛡️ Copia di sicurezza
6. e  /  ❌ Esci dal programma""")
    print("----------------------------------------------------")

    sceltaMenu = input("> Perfetto utente ti chiediamo di digitare una selta tra quelle elencate nel menu (es. oi): ").lower()

    if sceltaMenu == "oi":
        print("\n---------- AVVIO DEL SISTEMA ('oi') IN CORSO... ----------")
        files = os.listdir(sceltaPercorso)

        if not files:
            print("⚠️ ATTENZIONE: Utente nella directory selezionata non è presente alcun dato.")
            continue

        presenzaDiFile = any(os.path.isfile(os.path.join(sceltaPercorso, f)) for f in files)

        if not presenzaDiFile:
            print("⚠️ ATTENZIONE: Utente nella directory selezionata sono presenti solo sottocartelle.")
            continue

        ## FLUSSO PRINCIPALE: Se superiamo i controlli sopra, qui ci sono sicuramente dei file da elaborare.
        print("\n---------- AVVIANDO SPOSTAMENTO FILE E CARICANDO IL SISTEMA... ----------")
        for indice, file in enumerate(files):
            if os.path.isfile(os.path.join(sceltaPercorso, file)):
                nomeFileNoEs = os.path.splitext(file)[0]
                estensione = os.path.splitext(file)[1].lower()
                print(f"{indice + 1}. Nome file: {nomeFileNoEs} | Estensione: {estensione}")
                percorsoPartenza = os.path.join(sceltaPercorso, file)
                if estensione in regoleSmistamento:
                    nomeCartellaEstensione = regoleSmistamento[estensione]
                    percorsoDestinazione = os.path.join(sceltaPercorso, nomeCartellaEstensione)

                    percorsoArrivo = os.path.join(percorsoDestinazione, file)
                    if not os.path.exists(percorsoDestinazione):
                        os.makedirs(percorsoDestinazione)
                
                    trasportoDati = shutil.move(percorsoPartenza, percorsoArrivo)
                    print(f"🚚 SPOSTATO: {file}  ➔  {nomeCartellaEstensione}")
                else:
                    destinazioneSconosciuta = "Altri_File"
                    percorsoDellaDestinazione = os.path.join(sceltaPercorso, destinazioneSconosciuta)
                    percorsoDiArrivo = os.path.join(percorsoDellaDestinazione, file)
                    print(f"⚠️ ATTENZIONE: Ehilà utente il tipo di file ({file}) risulta sconosciuto lo sposteremo in ({destinazioneSconosciuta}).")
                    if not os.path.exists(percorsoDellaDestinazione):
                        os.makedirs(percorsoDellaDestinazione)
                    trasportoDatiSconosciuti = shutil.move(percorsoPartenza, percorsoDiArrivo)
                    print(f"🚚 SPOSTATO: {file}  ➔  {destinazioneSconosciuta}")
        print("-----------------------------------------------------------------------------")
    elif sceltaMenu == "sc":
        print("\n---------- AVVIO DEL SISTEMA ('sc') IN CORSO... ----------")
        tuttiGliElementi = os.listdir(sceltaPercorso)

        cartelle = []
        for f in tuttiGliElementi:
            ilPercorsoCompleto = os.path.join(sceltaPercorso, f)
            if os.path.isdir(ilPercorsoCompleto):
                cartelle.append(f)

        if not cartelle:
            print("⚠️ ATTENZIONE: Utente nella directory selezionata sono presenti solo file (NON SOTTOCARTELLE).")
            continue

        for indice, cartella in enumerate(cartelle):
            print(f"{indice + 1}. Nome cartella trovata: {cartella}")
        
        print("---------- CARICAMENTO SOTTOMENU DI (sc)... ----------")
        print (r"""[1] 🔀 • Sposta tutte le cartelle trovate dentro una cartella chiamata ARCHIVIO_CARTELLE
[2] 🔀 • Rinomina aggiungendo un nome alla sottocartella (es: cartella_lavoro)
[3] ↩️ • Torna al menu precedente""")
        print("---------------------------------------------------------")
        while True:
            sceltaSc = input("> Utente ti chiediamo di digitare una scelta NUMERICA elencata quì sopra: ")

            if sceltaSc == "1":
                print("\n---------- CARICAMENTO SISTEMI PER L'OPZIONE (1)... ----------")
                destinazioneUno = "ARCHIVIO_CARTELLE"
                percorsoDiDestinazione = os.path.join(sceltaPercorso, destinazioneUno)
                if not os.path.exists(percorsoDiDestinazione):
                    os.makedirs(percorsoDiDestinazione)
                for cartella in cartelle:
                    percorsoCompleto = os.path.join(sceltaPercorso, cartella)

                    if os.path.isdir(percorsoCompleto) and cartella != destinazioneUno:
                        percorsoDiArrivo = os.path.join(percorsoDiDestinazione, cartella)
                        trasportoCartelle = shutil.move(percorsoCompleto, percorsoDiArrivo)
                        print(f"🚚 SPOSTATO: {cartella}  ➔  {destinazioneUno}")
                break
            elif sceltaSc == "2":
                print("\n---------- CARICAMENTO SISTEMI PER L'OPZIONE (2)... ----------")
                nomeCartella = input("> Ricevuto, utente inserisci il nome che vuoi dare alla tua MASTER CARTELLA: ")
                percorsoDiDestinazione = os.path.join(sceltaPercorso, nomeCartella)
                if not os.path.exists(percorsoDiDestinazione):
                    os.makedirs(percorsoDiDestinazione)
                for cartella in cartelle:
                    percorsoCompleto = os.path.join(sceltaPercorso, cartella)

                    if not os.path.exists(percorsoCompleto):
                        print(f"ℹ️ INFO: '{cartella}' non è più presente, salto.")
                        continue

                    if os.path.isdir(percorsoCompleto) and cartella != nomeCartella:
                        percorsoDiArrivo = os.path.join(percorsoDiDestinazione, cartella)
                        trasportoCartelle = shutil.move(percorsoCompleto, percorsoDiArrivo)
                        print(f"🚚 SPOSTATO: {cartella}  ➔  {nomeCartella}")
                break
            elif sceltaSc == "3":
                print(f"✅ SUCCESS: Utente ti stiamo riportando al MENU PRINCIPALE...")
                break
            else:
                print(f"❌ ERROR: Utente Il comando da te selezionato non ci risulta valido riprova...")
                continue
    elif sceltaMenu == "fc":
        while True:
            print("\n---------- AVVIO DEL SISTEMA ('fc') IN CORSO... ----------")
            verificaProcedimento = input(f"⚠️ ATTENZIONE: > Utente confermi di eliminare i contenuti dalla directory da te inserita ({sceltaPercorso}) s / n: ").lower()
            if verificaProcedimento == "s":
                print("\n---------- PROCEDIMENTO AUTORIZZATO CONTINUO CALCOLI... ----------")
                elencoContenuti = os.listdir(sceltaPercorso)
                for elemento in elencoContenuti:
                    percorsoCompleto = os.path.join(sceltaPercorso, elemento)
                    try:
                        if os.path.isfile(percorsoCompleto):
                            eliminaFile = os.remove(percorsoCompleto)
                            print(f"🗑️ ELIMINATO: Nome del file cancellato: {elemento}")
                        elif os.path.isdir(percorsoCompleto):
                            eliminaCartella = shutil.rmtree(percorsoCompleto)
                            print(f"🗑️ ELIMINATO: Nome della cartella cancellata: {elemento}")
                    except PermissionError:
                        print(f"❌ ERROR: Non ho il permesso di eliminare questo file ci dispiace: {elemento}")
                    except OSError as e:
                        print(f"❌ ERROR: Errore di sistema generico ci dispiace: {e}")
                    except Exception as e:
                        print(f"❌ ERROR: Errore imprevisto ci dispiace: {e}")
                break
            elif verificaProcedimento == "n":
                print("\n---------- STOP DEI PROCEDIMENTI DI FORMATTAZZIONE... ----------")
                print("ℹ️ INFO: Confermato, utente hai selezionato l'opzione (n) quindi non proseguiremo col processo.")
                break
            else:
                print(f"❌ ERROR: Mhmm... utente hai fatto un'inserimento invalido! (RICORDA scegli: s / n) riprova...")
                continue
    elif sceltaMenu == "ad":
        print("\n---------- AVVIO DEL SISTEMA ('ad') IN CORSO... ----------")
        conteggioFile = 0
        conteggioCartelle = 0
        pesoDelFile = 0
        fileNonAccessibili = 0
        for percorsoCorrente, listaCartelle, listaFile in os.walk(sceltaPercorso):
            conteggioFile += len(listaFile)
            conteggioCartelle += len(listaCartelle)
            for file in listaFile:
                try:
                    percorsoCompleto = os.path.join(percorsoCorrente, file)
                    pesoFile = os.path.getsize(percorsoCompleto)
                    pesoDelFile += pesoFile
                except PermissionError:
                    print(f"❌ ERROR: Accesso negato per il file: {file}")
                    fileNonAccessibili += 1
                except FileNotFoundError:
                    print(f"❌ ERROR: File non trovato (forse rimosso): {file}")
                    fileNonAccessibili += 1
                except OSError as e:
                    print(f"❌ ERROR: Errore di sistema con {file}: {e}")
                    fileNonAccessibili += 1
        
        if pesoDelFile < 1024:
            pesoFormattato = f"{pesoDelFile} Byte" ## f"" sarebbe l'equivalente di print(f"")
        elif pesoDelFile < 1024 ** 2:
            pesoFormattato = f"{pesoDelFile / 1024:.2f} KB"
        elif pesoDelFile < 1024 ** 3:
            pesoFormattato = f"{pesoDelFile / (1024 ** 2):.2f} MB"
        else:
            pesoFormattato = f"{pesoDelFile / (1024 ** 3):.2f} GB"
        
        print(f"\n📊 Report Analisi per: {sceltaPercorso}")
        print("--------------------------------------------------")
        print(f"📁 Numero di sottocartelle trovate: {conteggioCartelle}")
        print(f"📄 Numero di file totali trovati: {conteggioFile}")
        print(f"💾 Spazio totale occupato: {pesoFormattato}")
        if fileNonAccessibili > 0:
            print(f"⚠️ File protetti o non accessibili saltati: {fileNonAccessibili}")
        print("--------------------------------------------------")
    elif sceltaMenu == "cs":
        copiaSicurezza(sceltaPercorso)
    elif sceltaMenu == "e":
        print("\n---------- UTENTE STIAMO USCENDO DAL SISTEMA PER TE... ----------")
        print(f"⚙️ SISTEMA: Spegnimento in corso... Alla prossima.")
        sys.exit()
    else:
        print(f"❌ ERROR: Attento utente ! hai appena inserito un comando non valido. Riprova...")