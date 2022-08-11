# Installation and launching

### Launch in Docker compose mode

Modify the below variables in Docker compose files

* POSTGRES_USER
* POSTGRES_PASSWORD
* POSTGRES_DB
* MIGRATE


```
docker-compose build
docker-compose up -d
```

### Launch in Docker compose mode

Modify the below variables in helm yaml value files

* pguser
* pgpass
* secretName
* migrate


### Launch in K8S mode

```
cd postgresql
helm install postgres ./ 

cd titanicapi
helm install titanicapi ./ 
```

### Step to perform to install EKS

