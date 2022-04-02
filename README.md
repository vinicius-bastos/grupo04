# Grupo 04 - 3CCO
> Repositório para o projeto de Pesquisa e Inovação do GRUPO 04 do 3CCO da São Paulo Tech School

## Arquitetura V1 que para seguir

![Captura de tela 2022-03-11 230040](https://user-images.githubusercontent.com/61800458/157999481-e6841513-bd70-4471-aae6-39cefe634c5f.png)

## Criando images Docker

Para nos facilitar na criação da imagem e container Docker (MySQL), foi disponibilizado um arquivo Dockerfile com o seguinte conteudo:

```dockerfile
FROM mysql:5.7
COPY ./db/ /docker-entrypoint-initdb.d/
```

Após configurado o arquivo navegamos até o caminho que ele está e rodamos o seguinte comando:

```bash
sudo docker build -t <name-image> .
```

Verifique se a imagem foi criada:

```bash
sudo docker images
```

Se a imagem estiver criada, vamos criar o container para acessarmos o banco MySql:

```bash
sudo docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=urubu100 -e MYSQL_DATABASE=algas -e MYSQL_USER=grupo04 -e MYSQL_PASSWORD=urubu100 <name-image>
```

Visualize se o container foi criado e obtenha o id do container:

```bash
sudo docker ps
```

Se o container estiver em running:

```bash
sudo docker exec -it <container_id> bash
```

```bash
mysql -uroot -p
```

### Extra

Se quiser utilizar apenas o comando docker, sem precisar do sudo, navegue até o usuario root de sua Ec2 e digite o comando:

```bash
usermod -a -G docker urubu100
```
