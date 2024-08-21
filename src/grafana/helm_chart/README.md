Grafana - Helm chart
===

## Pre-requisites
- Kubectl
```bash
$ kubectl version --client
Client Version: v1.30.3
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```
- Helm chart
```bash
$ helm version
version.BuildInfo{Version:"v3.15.3", GitCommit:"3bb50bbbdd9c946ba9989fbe4fb4104766302a64", GitTreeState:"clean", GoVersion:"go1.22.5"}
```

- Connects to a K8s cluster already:
```bash
$ kubectl cluster-info                                                          
Kubernetes control plane is running at https://3A49C05A87E05C7B0EA5F113109C3466.gr7.ap-southeast-2.eks.amazonaws.com
CoreDNS is running at https://3A49C05A87E05C7B0EA5F113109C3466.gr7.ap-southeast-2.eks.amazonaws.com/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'. 
```

## Developement guide
- Setup grafana helm repository
```bash
$ helm repo add grafana https://grafana.github.io/helm-charts
$ helm repo list
NAME    URL                                  
grafana https://grafana.github.io/helm-charts
$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "grafana" chart repository
Update Complete. ⎈Happy Helming!⎈
```

- Deploy helm chart
```bash
# Create new namespace
$ kubectl create namespace data-platform
namespace/data-platform created
# Navigate to grafana/helm_chart
$ cd ./grafana/helm_chart
# Install helm chart
$ helm install grafana grafana/grafana --namespace data-platform -f values.yaml
# Verify
$ kubectl --namespace data-platform get pods
NAME                                     READY   STATUS    RESTARTS   AGE
grafana-758fb6f47-gfkxt                  2/2     Running   0          4h26m
grafana-image-renderer-8dd6596f5-fx94p   1/1     Running   0          4h26m
# Expose pod to Internet
$ kubectl expose deployment grafana --namespace data-platform --port=3000 --target-port=3000 --name nginx-exposed-svc --type LoadBalancer
# Apply changes of values.yml file
$ helm upgrade grafana grafana/grafana --namespace data-platform -f values.yaml
```

- Access to Grafana
```bash
# Get password for admin user
$ kubectl get secret --namespace data-platform grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
SKWqlns4vQGu38KdYwVm5ILQMSezsiEHbkglNv7S
# Get adderss
$ kubectl --namespace data-platform get svc
: '
NAME                     TYPE           CLUSTER-IP       EXTERNAL-IP                                                                   PORT(S)          AGE
grafana                  ClusterIP      10.100.124.76    <none>                                                                        80/TCP           4h53m
grafana-image-renderer   ClusterIP      10.100.21.196    <none>                                                                        8081/TCP         4h53m
nginx-exposed-svc        LoadBalancer   10.100.226.220   ac5a8d13d6cb04534b081c03c55d6b5f-827035668.ap-southeast-2.elb.amazonaws.com   3000:30133/TCP   24m
'
```
Go to http://ac5a8d13d6cb04534b081c03c55d6b5f-827035668.ap-southeast-2.elb.amazonaws.com:3000 and do log in

- Uninstall Grafana
```bash
# Uninstall Grafana
$ helm uninstall grafana --namespace data-platform
# Delete k8s namespace
$ kubectl delete namespace data-platform
```

References:
- [Deploy Grafana using Helm Charts](https://grafana.com/docs/grafana/latest/setup-grafana/installation/helm/#enable-persistent-storage-recommended)
- [helm-charts/charts/grafana/values.yaml](https://github.com/grafana/helm-charts/blob/main/charts/grafana/values.yaml)
