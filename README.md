# xss-sarp-tester

Piccolo (e basilare) programma in python che verifica la vulnerabilità di un url ad un attacco XSS

## Versione 2.0
Il programma dispone di un array payload_default  in cui è possibile specificare una serie di payload da testare.

## Versione 3.0
* L'array payload_default è stato sostitutito con un nuovoargomento (--payload-file-url) che ti permette di caricare una lista di payload da un file di testo  (Esmpio: https://raw.githubusercontent.com/Emanuele-Furina/xss-SARP-tester/main/attacchi-xss.txt)

* È stato aggiunto un argomento che permette di specificare un cookie da tilizzare durante i test (--cookie)

