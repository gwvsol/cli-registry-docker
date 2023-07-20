## Distribution Registry    
---    

```shell

docker tag geoservice-db:latest localhost:5000/geoservice-db:2022-10-07-01

docker push localhost:5000/geoservice-db:2022-10-07-01

docker pull 192.168.62.148:5000/robotisk:2022-10-14-01

curl -s https://techvsolregistry.svc.1ckab.ru/v2/amiclient/tags/list | jq '.'

```    

```shell
curl http://192.168.62.148:5000/v2/_catalog | jq '.'     

{
  "repositories": [
    "audiosocket",
    "geoservice",
    "geoservice-db",
    "rabbitmq-db",
    "robotisk"
  ]
}

curl http://192.168.62.148:5000/v2/geoservice/tags/list | jq '.'

{
  "name": "geoservice",
  "tags": [
    "2022-10-05-01",
    "2022-10-06-01",
    "2022-10-07-01"
  ]
}
