import requests
import argparse

vermelho = "\033[31m"
verde = "\033[32m"
azul = "\033[34m"
laranja = "\033[33m"
reset = "\033[0;0m"

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", required=True, help="coloque a url, exemplo: http://vulnweb.com/")
parser.add_argument("-p", "--path", required=True, help="coloque o diretório/path que deseja verificar, exemplo: admin")
parser.add_argument("-sc", "--status_code", action="store_true",help="verificar o status-code")
parser.add_argument("-ua", "--user_agent", help="coloque o user-agent, Default: Mxssdir/1.0")

args = parser.parse_args()

url = args.url
path = args.path
sc = args.status_code
agent = args.user_agent

if not agent:
	headers = {"User-Agent": "Mxssdir/1.0"}
else:
	headers = {"User-Agent": agent}

try:
	url_completa = url+"/"+path
	r = requests.get(url_completa, headers=headers, timeout=5)
	status = r.status_code
	if sc:
		if status in range(100, 200):
                        sc = azul+str(status)+reset
		if status in range(200, 300):
			sc = verde+str(status)+reset
		if status in range(300, 400):
                        sc = laranja+str(status)+reset
		if status in range(400, 500):
			sc = vermelho+str(status)+reset
		if status in range(500, 600):
                        sc = azul+str(status)+reset
	else:
		sc = ""
except Exception:
	quit()

if not status == 404:
	print(url_completa, sc)
