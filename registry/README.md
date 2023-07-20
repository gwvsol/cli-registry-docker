### CLI application for Registry       

[Distribution Registry](https://hub.docker.com/_/registry)      
[Docker Registry](https://docs.docker.com/registry/)      
[Configuring a registry](https://docs.docker.com/registry/configuration/)     
[Deploy a registry server](https://docs.docker.com/registry/deploying/)      
[Docker Registry HTTP API V2](https://docs.docker.com/registry/spec/api/)    
[Настройка локального хранилища Docker Registry](https://winitpro.ru/index.php/2021/03/03/nastrojka-lokalnogo-docker-registry/)     
[Настройка локального репозитория для образов Docker и работа с ним](https://www.dmosk.ru/miniinstruktions.php?mini=docker-local-repo)       
[How To Set Up a Private Docker Registry on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-18-04)     

---    
[Set up Docker Registry with an UI](https://medium.com/open-devops-academy/set-up-docker-registry-and-a-docker-regui-8340bb287276)     
[Docker Registry UI](https://hub.docker.com/r/joxit/docker-registry-ui)      
[Docker Registry UI](https://github.com/Joxit/docker-registry-ui)    
[Docker Registry UI](https://joxit.dev/docker-registry-ui/)    

---     

[Docker Registry V2 api](https://russianblogs.com/article/84741139528/) - Плохой перевод, но все же...    
[Docker Registry API – Listing Images and Tags](https://www.baeldung.com/ops/docker-registry-api-list-images-tags)      
[How can I use the Docker Registry API V2 to delete an image from a private registry?](https://stackoverflow.com/questions/37033055/how-can-i-use-the-docker-registry-api-v2-to-delete-an-image-from-a-private-regis)      
[How to Delete Images From a Private Docker Registry](https://azizunsal.github.io/blog/post/delete-images-from-private-docker-registry/)    
  

```shell
curl -s -I -H "Accept: application/vnd.docker.distribution.manifest.v2+json" http://localhost:5000/v2/geoservice/manifests/2022-10-05

# HTTP/1.1 200 OK
# Content-Length: 2002
# Content-Type: application/vnd.docker.distribution.manifest.v2+json
# Docker-Content-Digest: sha256:1afb1988694db2c535001e769991cfece0a6f73364ca59782f276bbd16252c2b
# Docker-Distribution-Api-Version: registry/2.0
# Etag: "sha256:1afb1988694db2c535001e769991cfece0a6f73364ca59782f276bbd16252c2b"
# X-Content-Type-Options: nosniff
# Date: Mon, 10 Oct 2022 07:07:54 GMT

curl -s -X "DELETE" http://localhost:5000/v2/robotisk/manifests/sha256:1afb1988694db2c535001e769991cfece0a6f73364ca59782f276bbd16252c2b

#curl -s -X "DELETE" "http://localhost:5000/v2/robotisk/manifests/$(curl -s -I -H "Accept: application/vnd.docker.distribution.manifest.v2+json" http://localhost:5000/v2/robotisk/manifests/latest | awk '$1 == "Docker-Content-Digest:" { print($2) }')"
```

Для того, чтобы docker pull твой_registry:твой_образ не требовал от твой_registry HTTPS, необходимо и достаточно вписать   

```json
{
  "insecure-registries": [
    "твой_registry:порт"
  ]
}
```    

в /etc/docker/daemon.json, после чего сказать ```systemctl reload-or-restart docker.service``` .     
