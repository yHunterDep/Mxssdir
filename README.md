# Mxssdir
mxssdir é um script em python que verifica se um path existe

# Clonar Repositório
```sh
git clone https://github.com/yHunterDep/Mxssdir/
cd Mxssdir
```

# Baixar Requirementos
```sh
pip3 install -r requirements.txt
```
# Help
```sh
python3 mxssdir.py -h
```

# Verificar se um path existe
```sh
python3 mxssdir.py -u http://testphp.vulnweb.com/ -p admin
```

# Ver o status-code
```sh
python3 mxssdir.py -u http://testphp.vulnweb.com/ -p admin -sc
```

# Usando o User-Agent + status_code
```sh
python3 mxssdir.py -u http://testphp.vulnweb.com/ -p admin -ua "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
python3 mxssdir.py -u http://testphp.vulnweb.com/ -p admin -ua "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36" -sc
```
