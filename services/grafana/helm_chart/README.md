Grafana - Helm chart
===

## Pre-requisites
Check [here](../../../README.md#prerequisites)

## Developement guide
- Setup grafana helm repository
```bash
$ helm repo add grafana https://grafana.github.io/helm-charts
$ helm repo list
: '
NAME    URL                                  
grafana https://grafana.github.io/helm-charts
'
$ helm repo update
: '
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "grafana" chart repository
Update Complete. ⎈Happy Helming!⎈
'
```

- Deploy helm chart
```bash
# Install helm chart
$ helm install grafana grafana/grafana --namespace data-platform -f k8s/dev/values.yaml
# Verify
$ kubectl get pods
: '
NAME                                     READY   STATUS    RESTARTS   AGE
grafana-758fb6f47-gfkxt                  2/2     Running   0          4h26m
grafana-image-renderer-8dd6596f5-fx94p   1/1     Running   0          4h26m
'
# Expose pod to Internet
$ kubectl expose deployment grafana --namespace data-platform --port=3000 --target-port=3000 --name nginx-exposed-svc --type LoadBalancer
# Apply changes of values.yml file
$ helm upgrade grafana grafana/grafana --namespace data-platform -f k8s/dev/values.yaml
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
$ helm uninstall grafana
```

References:
- [Deploy Grafana using Helm Charts](https://grafana.com/docs/grafana/latest/setup-grafana/installation/helm/#enable-persistent-storage-recommended)
- [helm-charts/charts/grafana/values.yaml](https://github.com/grafana/helm-charts/blob/main/charts/grafana/values.yaml)
