<h3 align="center">Twitter Hadoop</h3>


---

## 📝 Table of Contents

- [Sobre - Desafio](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
<!-- - [Usage](#usage) -->
<!-- - [Built Using](#built_using) -->

- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 Desafio <a name = "about"></a>

Objetivo: Criar Data Lake on premise.

Regras:

- Explorar os cenários de implementação abaixo

- Utilizar tecnologias de sua preferência;

- Montar um protótipo funcional;

- Entregar scripts de automação das tecnologias (script shell simples ou framework de automação) e todos os códigos fontes desenvolvidos; (pode compartilhar via git)

- Criar desenho da solução;

- Relatório funcional com a solução,definições dos conceitos, tecnologias utilizadas e referência com os scripts desenvolvidos. (pdf, ppt,txt).



Cenários de implementação:

- Ingestão de dados do Twiter com hashtag especificas.

- Integração de um banco de dados Nosql com o data lake.

- Demonstre as opções para melhorar a performance de consumo de dados do data lake via SQL.

- Demonstre consumo de dados do datalake por uma aplicação web


## 🏁 Getting Started <a name = "getting_started"></a>

### Pré-requisitos

Softwares necessarios para a execução

```
Python
Kafka
Cassandra DB
FastAPI
```

### Instalação

Passo a passo para a instalação de todos os softwares necessarios.

Kafka:

- https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-18-04-pt


Cassandra:


- https://phoenixnap.com/kb/install-cassandra-on-ubuntu


FastAPI:

- https://fastapi.tiangolo.com/#installation

## 🎈 Usage <a name="usage"></a>
Criar a tabela tweet no Cassandra utilizando o script "table.
Para iniciar a captura dos tweets utilize o comando:

```
./start.sh
```

Com isso criamos a tabela tweets no Cassandra e inicializamos producer, consumer e fastAPI.


<!-- ## 🚀 Deployment <a name = "deployment"></a>



## ⛏️ Built Using <a name = "built_using"></a>



## ✍️ Authors <a name = "authors"></a>

- [@diegomeyer](https://github.com/diegomeyer)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
