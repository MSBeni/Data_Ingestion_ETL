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
microk8s kubectl get services      # or svc # A service is a stable endpoint to connect to "something"
microk8s kubectl get namespaces
microk8s kubectl get pods --all-namespaces
microk8s kubectl -n kube-public get configmaps
microk8s kubectl -n kube-public get configmap your_namespaces -o yaml
```
If you do not have the ```jq``` you can simply install it ```sudo snap install jq```.

### Pods:
Pods are a new abstraction!

- A pod can have multiple containers working together
- (But you usually only have on container per pod)
- Pod is our smallest deployable unit; Kubernetes can't mange containers directly
- IP addresses are associated with pods, not with individual containers
- Containers in a pod share localhost, and can share volumes
- Multiple containers in a pod are deployed together
- In reality, Docker doesn't know a pod, only containers/namespaces/volumes

## Running Container on Kubernetes:
You cannot create containers directly. At the lowest level we can just create a pod. In most of the cases
we are not even creating a pod, we are creating something higher than that in the abstraction layers. let's
just start with a simple command:
```shell
microk8s kubectl create deployment my-dep --image=busybox
microk8s kubectl run pingpong --image alpine ping 1.1.1.1
```
other example:
```shell
microk8s kubectl create deployment nginx --image nginx
microk8s kubectl run nginx --image nginx
```
You will receive this message: ```pod/pingpong created```
Running the command below, you should see the new pod:
```shell
microk8s kubectl get all   # all the resources in the cluster
```
This can be a sample result:
```shell
NAME           READY   STATUS    RESTARTS   AGE
pod/pingpong   1/1     Running   0          85s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.00.100.00   <none>        443/TCP   20h

```
Actually by running this command we create a ReplicaSet and then this resource finally create the pod.
All deployment layer, ReplicaSet and Pod are called abstractions. Finally that pod will create the 
Container which is a real object running on Docker and inside the container we are running the specific command 
which is the ```ping``` command in the above case.

- A ```deployment``` is a high-level construct, allows scaling, rolling updates, rollbacks, 
  multiple deployments can be used together to implement a canary deployment,delegates 
  pods management to replica sets

- A ```replica set``` is a low-level construct, makes sure that a given number of identical pods are running, 
  allows scaling, rarely used directly

    - Note: A replication controller is the deprecated predecessor of a replica set

### view logs command:
Exploiting ```Kubectl logs ```command, you can pass either a pod name, or a type/name to see the result of the service.
View the result of our ping command:
```shell
microk8s kubectl logs deploy/pingpong
microk8s kubectl logs pod/pingpong
```
