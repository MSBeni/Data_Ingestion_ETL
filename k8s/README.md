# k8s installation and commands

## Installation guide:
Please follow the below steps:
```shell
sudo snap install microk8s --classic
microk8s.kubectl
sudo usermod -a -G microk8s msbeni
echo "alias kubectl='microk8s.kubectl'" >> ~/.bashrc
```
Now Please log out and log in again:
```shell
sudo microk8s.enable dns
microk8s.status
```

Now you can activate the shpod:
```shell
microk8s kubectl apply -f https://k8smastery.com/shpod.yaml
```