# Guia para preparar e rodar o backend em Python

Primeiro certifique-se que possui Python3 instalado em sua máquina.

Após, prossiga com os passos abaixo.

# Execute na raíz do backend, respeitando a ordem:

py -3 -m venv .venv  

.venv\Scripts\activate

# Com o ambiente virtual ativado (confira a flag .venv no terminal) execute:

pip install -r requirements.txt

#  Pronto, o serviço já pode ser iniciado com o seguinte comando:

flask --app .\run.py --debug run

# Rodar Firestore Emulator localmente (dentro do .venv):

firebase emulators:start