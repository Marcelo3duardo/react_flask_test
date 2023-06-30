###nesse diretório, crie o ambiente virtual
```cmd
py -3 -m venv .venv
```

###ative o ambiente virtual
```cmd
.venv/Scripts/Activate
```

###instale as dependências(flask,flask-cors)
```cmd
pip install -r requirements.txt
```

###exporte a variável de ambiente
```cmd
export FLASK_APP=api/__init__.py
```
###execute a aplicação
```cmd
flask run
```

