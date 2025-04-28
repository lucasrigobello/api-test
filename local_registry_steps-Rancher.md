# A seguir segue passo a passo, para criar um local registry, bem como a criação de um container Rancher
editar
# com finalidade de validar o funcinamento do deployment em kubernetes

# criar container de local registry
docker run -d -p 5000:5000 --name dockerregistry registry

# verificar images no local registry
http://localhost:5000/v2/_catalog

# criando a imagem
docker build -t localhost:5000/api-test .

# push da imagem para local registry
docker push localhost:5000/api-test 

# se ocorre falha, precisa editar o arquivo /.docker/daemon.json, para incluir insecure-registries:
{
  "insecure-registries": [
    "localhost:5000"
  ],
  "experimental": true
}


"insecure-registries": ["192.168.1.3:5000"],

# criar container Rancher
docker run -d --restart=unless-stopped -p 81:81 -p 80:80 -p 443:443 --privileged rancher/rancher:latest
docker run -d --restart=unless-stopped -p 81:81 -p 80:80 -p 443:443 --privileged rancher/rancher:stable

# Acesso ao Rancher
https://localhost/

# Recuperar senha de primeiro Acesso do Rancher. Primeiro encontre o container-id. Em sequência cadastre sua senha:
docker ps
docker logs container-id 2>&1 | findstr "Bootstrap Password:"
Ldsr010!123456789

# Criando deployment em Kubernetes no Rancher, pela imagem do Local Resgistry:
- Local -> Workloads -> Create -> Deployment

# Preencher com um nome para o Deployment, e em seguinda o endereço da imagem:
- Image: localhost:5000/api-test

# kubernetes, criando a imagem
nerdctl -n k8s.io build -t api-test .

# aplicando Serviço LoadBalance
kubectl apply -f ./helm-charts/templates/service.yaml

# aplicando o Deploy em Kubernetes
kubectl apply -f ./helm-charts/templates/deployent.yaml
