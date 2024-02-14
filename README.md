# Mxssdir
mxssdir é um script em python que verifica se um path existe

# Clonar Repositório
git clone https://github.com/yHunterDep/Mxssdir/
cd Mxssdir

# Baixar Requirementos
pip3 install -r requirements.txt

# Help
python3 mxssdir.py -h

# Verificar se um path existe
python3 mxssdir.py -u http://testphp.vulnweb.com/ -p admin

# Ver o status-code
python3 mxssdir.py -u http://testphp.vulnweb.com/ -p admin -sc

# Usando o User-Agent
python3 mxssdir.py -u http://testphp.vulnweb.com/ -p admin -ua "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
