Avvertenze prima dell'utilizzo: contesto e del progetto è licenza
------------------------------------------------------------
Il presente file README si propone come guida da seguire per la corretta esecuzione e visualizzazione del sito web, che funge da progetto d'esame per il corso di "Tecnologie Web" dell'Università degli Studi di Napoli "Parthenope" per l'anno accademico 2024/2025. Prima di descrivere i passi da eseguire, avvisiamo che questo progetto è distribuito sotto la licenza Apache 2.0 (vedi il file `LICENSE` per ulteriori dettagli).

Avvertenze prima dell'utilizzo: dichiarazione di Copyright
----------------------------------------------------------
Il presente progetto è protetto sotto la seguente sigla di Copyright:

Copyright 2025 RottaNautica

Avvertenze prima dell'utilizzo: termini di Utilizzo
----------------------------------------------------
L'uso, la riproduzione e la distribuzione di questo progetto sono consentiti solo in conformità con i termini della licenza Apache 2.0. Non è permesso utilizzare o distribuire questo progetto come proprio senza l'adeguata attribuzione e il rispetto dei termini della licenza.

Per ulteriori informazioni, consulta il file `LICENSE` incluso in questa repository.

Avvertenze prima dell'utilizzo: ulteriori informazioni
-----------------------------------------------------
Dato per assodato tutto ciò che è scritto nelle righe precedenti, se si accettano i termini di Utilizzo e si agisce in conformità al Copyright che protegge il presente progetto, per la corretta esecuzione e visualizzazione, continuare a leggere questo file e assicurarsi di eseguire in ordine e alla lettera i passi descritti in basso. 

Nome del progetto: RottaNautica

Descrizione del progetto
------------------------
Il progetto si propone di offrire una piattaforma completa per la vendita online di prodotti nautici, inclusa la gestione del catalogo e la gestione degli utenti. L'obiettivo di “RottaNautica”, questo il nome del sito, è quello di creare un'esperienza di shopping online intuitiva e sicura per gli appassionati di attività nautiche.

Installazione ed esecuzione
---------------------------
Di seguito, la descrizione dettagliata dei programmi da scaricare e dei passi da seguire per poter eseguire correttamente il sito web.

PASSO 1 (obbligatorio)
-------
Installazione dei programmi necessari per l'esecuzione
------------------------------------------------------
Per poter eseguire correttamente il progetto è necessario installare i seguenti programmi:

Obbligatori
-----------

- Python (dal sito Python.org);

P.S. Assicurarsi di flaggare l'opzione "Add Python to PATH", questa opzione aggiunge Python al PATH di sistema, il che significa che sarà possibile eseguire comandi Python da qualsiasi directory nel terminale o prompt dei comandi senza dover specificare il percorso completo dell'eseguibile Python.

- SQL Lite (dal sito https://sqlitebrowser.org/dl/);

P.S. Per la realizzazione del progetto è stata utilizzata la versione DB Browser for SQLite - Standard installer for 64-bit Windows.

- Visual Studio Code (dal sito https://code.visualstudio.com/ oppure dal Microsoft Store).

Facoltativi
-----------

- DIA (dal sito http://dia-installer.de/)


PASSO 2 (obbligatorio)
-------
Scaricamento dei file necessari
--------------------------------
Scaricare TUTTI i file presenti nella repository, assicurandosi di NON dimenticarne nessuno e di NON sposare file all'interno o all'esterno delle cartelle di appartenenza. Inoltre, è assolutamente necessario NON rinominare le cartelle e/o i file con altri nomi, in quanto i percorsi sono già stati definiti con gli attuali nomi.

Teconologie utilizzate: si fa presente che le tencologie utilizzate per la realizzazione del presente progetto sono HTML5, CSS3, Python, Flask, SQL Alchemy ed SQL Lite.


PASSO 3 (facoltativo)
-------
Visualizzazione dell'architettura del database
----------------------------------------------
N.B. Questo passo è facoltativo, in quanto NON NECESSARIO per la corretta esecuzione del sito web. Se si decide di eseguirlo, informiamo che è necessario aver installato "DIA" al passo 1. In caso contrario, non sarà possibile visualizzare il file. 

E' possibile visualizzare l'architettura del database che gestisce il sito web. L'architettura del database è mostrata dal file RottaNautica_database (che ha estensione .dia).


PASSO 4 (obbligatorio)
-------
Esecuzione del sito web
-----------------------
Per la corretta esecuzione e visualizzazione del sito web, seguire in ordine i seguenti passi:

1) Avviare "Visual Studio Code";

2) Cliccare sulla sezione delle estensioni ("Extensions") a sinistra (icona del quadrato, terza icona dal basso), cercare e installare l'estensione "Python" di "Microsoft";

3) Scaricare dal terminale "SQLAlchemy" e "Flask", eseguendo separatamente i seguenti comandi:

pip install sqlalchemy

pip install flask

Per farlo, è necessario aprire il terminale del sistema operativo che si sta utilizzando e selezionare la cartella in cui sono ubicati tutti i file scaricati. Ad esempio, per Windows, sarà una cosa del genere:

C:\Users\Nome_utente\OneDrive\Desktop\Risorse del Computer\Personale\Università\TERZO_ANNO\Tecnologie_web\RottaNautica>

Dopo aver scritto ciò, eseguire separatamente e in ordine i comandi sopra indicati;

4) Tornare su "Visual Studio Code" e cliccare sulla sezione "File" in alto a sinistra, selezionare l'opzione "Open Folder" e scegliere la cartella in cui sono stati ubicati i file "database.py" e "app.py";

5) Una volta selezionata la cartella, eseguire in ordine prima il file "database.py" e poi il file "app.py";

6) Una volta eseguito il file "app.py" verrà restituito in output un link che porta al sito web;

7) Cliccare sul link e testare il progetto, ad esempio, creando un account e provando ad accedervi.

TEST CON SQL LITE
-----------------
Per verificare la corretta funzionalità del database, è possibile aprire contemporaneamente sia il sito web sia la finestra di SQL Lite e provare ad eserguire la registrazione di un account utente. Eseguire in ordine i seguenti passi:

1) Eseguire il setup di SQL Lite e installare il programma;

2) Avviare il programma e cliccare sull'opzione "Apri Database" e selezionare dalla cartella contenente i file installati dalla repository il file denominato "database", che ha estensione .db;

3) Una volta aperto il database, cliccare sulla sezione "Visualizza Dati", cliccare sulla freccia verso il basso che apre il menù a tendina di fianco alla scritta "Tabella:" e selezionare la tabella denominata "Users".

