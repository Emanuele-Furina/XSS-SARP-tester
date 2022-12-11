## Requisiti
* Python 3.6 o versioni successive
* Pacchetti Python requests e beautifulsoup4
* Pacchetto Python colorama (opzionale, ma consigliato per un output colorato)

## Installazione
Per installare i pacchetti Python richiesti, puoi usare pip:

```pip install requests beautifulsoup4 colorama```


## Uso
Per eseguire XSS Tester, puoi usare il seguente comando:

```python xss_tester.py <url> [options]```

Dove **url** è l'URL della pagina da testare per le vulnerabilità XSS e **[options]** sono gli argomenti opzionali.


## Argomenti del comando
**-p**, **--payload**: specifica il payload da utilizzare.

**-f**, **--payload-file-url**: specifica l'URL di un file contenente i payload da testare **(un payload per riga)**, Se non specificato, non verrà utilizzata alcuna lista.

**-o**, **--output-file**: specifica il percorso di un file in cui scrivere i payload funzionanti. Se non specificato, i payload funzionanti non verranno salvati.

**-c**, **--cookie**: specifica il valore dell'intestazione Cookie da impostare per le richieste. Se non specificato, l'intestazione Cookie non verrà impostata.

## Esempi
Ecco alcuni esempi di come usare XSS Tester:

Testare l'URL **http://example.com** per le vulnerabilità usando il payload ```<script>alert('XSS')</script>```:

```python xss_tester.py http://example.com -p "<script>alert('XSS')</script>"```

Testa l'URL **http://example.com** usando i payload nel file all'indirizzo **http://example.com/payloads.txt**:

```python xss_tester.py http://example.com -f http://example.com/payloads.txt```

Testa l'URL http://example.com usando i payload nel file all'indirizzo **http://example.com/payloads.txt** e scrivi i payload che hanno funzionato nel file **successful_payloads.txt**:

```python xss_tester.py http://example.com -f http://example.com/payloads.txt -o successful_payloads.txt```
