##### Minikube 

*  Deps

    virtualbox
    kubectl.

After successfull installation of virtualbox,

```
minikube start
kubectl cluster-info
minikube dashboard
```

###### deploy image
`kubectl run hello-go --image=shapeshed/hello-go --port=8080`
###### Expose deployment    
`kubectl expose deployment hello-go --type=NodePort`
###### Get Pod
`kubectl get pod`
###### Discover url
`minikube service hello-go --url`
