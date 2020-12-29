#!/bin/bash 


echo "Instalando python3-venv"
sudo apt-get install python3-venv

echo "Criando venv"
python3 -m venv venv
echo "Ativando venv"
source "venv/bin/activate"

echo "Instalando requirements"
pip install -r requirements.txt

export PYTHONPATH=$PWD
source envs

echo "Inicializando Serviços"
#inicialização dos serviços
python producer/twitter_streaming_productor.py &
python consumer/twitter_streaming_consumer.py &
cd $PWD/fastApi &&
pwd &&
uvicorn api:app --host 0.0.0.0 --port 8000

