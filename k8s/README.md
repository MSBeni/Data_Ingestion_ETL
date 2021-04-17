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
microk8s kubectl logs deploy/my-dep
microk8s kubectl logs pod/pingpong
```
Or we can scale our application, We can create additional copies of our container (I mean, our pod) with kubectl scale:
```shell
microk8s kubectl scale deployment my-dep --replicas 3
```
To see the tail of the command and just printing one by one the results:
```shell
kubectl logs deploy/pingpong --tail 1 --follow
```

### Deleting the Pods:
You use delete, but you will see another one will run again:
```shell
microk8s kubectl delete pod/pingpong-8f6db4897-dd9d4
```

## Cronjobs
sample command:
```shell
microk8s kubectl create cronjob sleep-job --image=sleep --schedule="*/3 * * * *" --restart=OnFailure
microk8s kubectl get cronjobs
```

## Streaming logs of multiple pods
Can we stream the logs of all our pingpong pods.
Combine -l and -f flags:
```shell
microk8s kubectl logs -l run=pingpong --tail 1 -f
```
### Stern: Shortcomings of kubectl logs
Follow installation on https://github.com/wercker/stern.
or simply use:
```shell
brew install stern
```
Sample:
```shell
stern pingpong
stern --tail 1 --timestamps pingpong
```

## Service types:
There are different types of services:

```ClusterIP, NodePort, LoadBalancer, ExternalName```

- ClusterIP:
It's the default service type, A virtual IP address is allocated for the service 
  (in an internal, private range; e.g. 10.96.0.0/12), This IP address is reachable 
  only from within the cluster (nodes and pods), Our code can connect to the service 
  using the original port number, Perfect for internal communication, within the cluster
  
  
- NodePort
A port number is allocated for the service, (by default, in the 30000-32767 range)
That port is made available on all our nodes and anybody can connect to it
(we can connect to any node on that port to reach the service)
Our code needs to be changed to connect to that new port number, 
  Under the hood: kube-proxy sets up a bunch of iptables rules on our nodes
Sometimes, it's the only available option for external traffic (e.g. most clusters deployed with kubeadm or on-premises)
  

- LoadBalancer
An external load balancer is allocated for the service, 
(typically a cloud load balancer, e.g. ELB on AWS, GLB on GCE ...)
This is available only when the underlying infrastructure provides some kind of "load balancer as a service"
Each service of that type will typically cost a little bit of money
(e.g. a few cents per hour on AWS or GCE)
Ideally, traffic would flow directly from the load balancer to the pods
In practice, it will often flow through a NodePort first
  
- Creating a deployment for our HTTP server and then real time watching 
the generated pod ```microk8s kubectl get pods -w```

```shell
microk8s kubectl create deployment httpenv --image=msbeni/httpenv
microk8s kubectl get pods -w
```
You can scale them and see the results:
```shell
microk8s kubectl scale deployment httpenv --replicas 10
```

Now using the ```expose``` command we cann create the service for those
pods:
```shell
microk8s kubectl expose deployment httpenv --port 8893
```