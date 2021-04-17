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
microk8s kubectl attach --namespace=shpod -ti shpod
```

Now you can simply check the k8s internal:
```shell
microk8s kubectl get nodes   # or node or no
microk8s kubectl get nodes -o wide
microk8s kubectl get nodes -o json | jq ".items[] | {name:.metadata.name} + .status.capacity"
microk8s kubectl describe node/pop-os    # describing the active node 
microk8s kubectl api-resources
microk8s kubectl get pods
microk8s kubectl explain pods
microk8s kubectl explain pods.metadata
microk8s kubectl explain pods.metadata.uid
microk8s kubectl get services      # or svc
microk8s kubectl get namespaces
microk8s kubectl get pods --all-namespaces
```
If you do not have the ```jq``` you can simply install it ```sudo snap install jq```.