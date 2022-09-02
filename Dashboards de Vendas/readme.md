## Dashboard de Vendas de Imóveis de Nova Iorque

- Projeto tem como objetivo a criação de um dashboard que demonstra os preços de vendas de imóveis da cidade de Nova Iorque, e alguns controles interativos que possibilita uma análise sobre o dash, existe tres controles no dash, é possível filtrar por bairro(Bronx, Queens, etc), pela  metragem (100, 500 metros e etc) e por ultimo por total de unidades, preço, ano de construção.
 
### Projeto está dividido da seguinte maneira:

- Index 
- App
- Controllers
- Componentes (map, hist)

### Bibliotecas e suas versões

- dash==2.6.1
- dash-bootstrap-components==1.2.1
- dash-core-components==2.0.0
- ash-html-components==2.0.0
- gunicorn==20.1.0
- numpy==1.23.2
- pandas==1.4.3
- plotly==5.10.0


### Index
- Projeto está subdividido em duas partes com o app.py e o index.py por convenção.
- Código está elaborado da seguinte maneira, primeiro importando bibliotecas necessárias para execução do projeto.
- Logo após está a parte de ingestão e tratamento de dados.
- A parte de layout se baseia em pegar os elementos criados nos demais componentes como os controllers, map, hist.
- Posteriormente vem o callback que utiliza do método de decorators do python que possibilita pegar uma função e replica-la em outra função, esse conceito está de acordo com a documentação do dash. 
- Um elemento importante na aplicação do dash é essencial para o sucesso do projeto seria realizar o cadastro no site: https://account.mapbox.com/ e criar um token de acesso. Com esse token é possivel criar maps mais bonitos e dinamicos com o mapbox.

### App
- No app consiste em somente escolher o layout do dash, o tema escolhido para este projeto foi o "Slate".

### Controllers
- Estrutura para criar o layout dos controles

### Componentes
- Maps e Histograma

### Links da Documentações
- https://plotly.com/python/
- https://dash.plotly.com/introduction

#### 
Projeto
