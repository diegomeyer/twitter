<h3 align="center">Twitter Hadoop</h3>


---

## 📝 Table of Contents

- [Sobre - Desafio](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
<!-- - [Usage](#usage) -->
<!-- - [Built Using](#built_using) -->
<!-- - [Contributing](../CONTRIBUTING.md) -->
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
Hadoop
Hive
Flume
xxx
xxx
```

### Instalação

Passo a passo para a instalação de todos os softwares necessarios.

Hadoop:

- http://www.ehadoopinfo.com/2017/07/installing-apache-hadoop-in-ubuntu.html


Hive:


- https://www.dezyre.com/hadoop-tutorial/install-hive


Flume:

- 

Foi encontrado um problema de desserialização dos arquivos gerados,  para contornar o problema foi usado:

 - TwitterAgent.sources.Twitter.type = com.cloudera.flume.source.TwitterSource

ao invés de:

 - TwitterAgent.sources.Twitter.type = org.apache.flume.source.twitter.TwitterSource

Foi feito o build seguindo:
 - https://github.com/cloudera/cdh-twitter-example

Os dois arquivo ja estão no na pasta "extras".

Crie as seguintes pastas:
```
mkdir -p /usr/lib/flume-ng/plugins.d/twitter-streaming/lib/

mkdir -p /var/lib/flume-ng/plugins.d/twitter-streaming/lib/
```
Copie os arquivos:

```
cp flume-sources-1.0-SNAPSHOT.jar /usr/lib/flume-ng/plugins.d/twitter-streaming/lib/

cp flume-sources-1.0-SNAPSHOT.jar /var/lib/flume-ng/plugins.d/twitter-streaming/lib/

cp hive-serdes-1.0-SNAPSHOT.jar $HIVE_HOME/lib
```

<!-- ## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment -->

## ✍️ Authors <a name = "authors"></a>

- [@diegomeyer](https://github.com/diegomeyer)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
