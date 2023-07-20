## CLI application for Registry       

```shell

dnf install httpd-tools # для Fedora, CentOs
apt install apache2-utils # для Debian

# Создание файла .htpasswd для Registry
htpasswd -c /home/work/.htpasswd bob123

```

```shell

docker tag geoservice-db:latest localhost:5000/geoservice-db:2022-10-07-01

docker push localhost:5000/geoservice-db:2022-10-07-01

docker pull 192.168.62.148:5000/robotisk:2022-10-14-01

curl -s https://techvsolregistry.svc.1ckab.ru/v2/amiclient/tags/list | jq '.'

```    