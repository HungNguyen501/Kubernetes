Apache Airflow - Helm chart
===

## Prerequisites
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

## Development guide
- Install Airflow
```bash
$ helm repo add apache-airflow https://airflow.apache.org
: '
"apache-airflow" has been added to your repositories
'
$ helm repo update
: '
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "apache-airflow" chart repository
Update Complete. ⎈Happy Helming!⎈
'
# Create data-platform namespace
$ kubectl create namespace data-platform && kubectl config set-context --current --namespace=data-platform
# Install airflow
$ helm install airflow apache-airflow/airflow --namespace data-platform -f k8s/values.yaml
# Access airlfow UI
$ kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow
```

- Enable git-sync feature
```bash

```

Ref links:
- [Airflow Helm Chart](https://artifacthub.io/packages/helm/apache-airflow/airflow)
- https://hungngph.medium.com/airflow-on-kubernetes-with-helm-c795545325dc
- https://github.com/lyabomyr/k8s_local_airflow_deployment