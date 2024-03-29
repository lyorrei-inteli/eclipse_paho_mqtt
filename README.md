# Integração simulador com HiveMQ

Este repositório contém um simulador de dispositivos IoT para sensor de radiação solar e um conjunto de testes automatizados para validar o simulador. O simulador publica dados simulados de um sensor de radiação solar no HiveMQ. O assinante escuta as mensagens publicadas no tópico MQTT e imprime as mensagens recebidas.

## Como instalar

Após clonar o repositório, navegue até a pasta do projeto e instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Como rodar o sistema

Crie um arquivo `.env` na root do projeto e preencha as váriaveis de ambiente no arquivo com as informações do seu broker MQTT. O arquivo `.env` deve conter as seguintes variáveis:

```bash
BROKER_ADDR=...
HIVE_USER=...
HIVE_PSWD=...
```

Para iniciar o simulador, execute o seguinte comando:

```bash
python3 publisher.py
```

Para iniciar o subscriber que irá ouvir as mensagens publicadas pelo simulador, abra um novo terminal e execute:

```bash
python3 subscriber.py
```

## Executar os Testes

Para executar os testes automatizados, use o seguinte comando:

```bash
pytest tests/
```

## Demonstração do Sistema

Demonstração dos Publishers e Subscribers: [Link do vídeo](https://youtu.be/mvigfNvgJ_4) <br/>
Demonstração dos testes: [Link do vídeo](https://youtu.be/P0oVfgMh7zs) <br/>
Demonstração do HiveMQ: [Link do vídeo](https://youtu.be/9e3lP3gzc_A)

## Estrutura do Projeto

- `publisher.py`: Contém o código do publicador que envia dados simulados de um sensor de radiação solar para um broker MQTT.
- `subscriber.py`: Contém o código do assinante que escuta e imprime as mensagens do tópico MQTT.
- `sensor_simulator.py`: Define a classe `SolarRadiationSensorSimulator` que simula dados de radiação solar.
- `tests/`: Pasta contendo os testes automatizados para o simulador.
  - `test_sensor_simulator.py`: Testes automatizados para validar as funcionalidades do simulador.
