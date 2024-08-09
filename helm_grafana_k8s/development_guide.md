Development Guide
===

```bash
# Get the Grafana admin password
$ kubectl get secret --namespace data-platform my-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
# Install Grafana
$ helm install my-grafana grafana/grafana --namespace data-platform -f values.yaml
# Update Grafana configs
$ helm upgrade my-grafana grafana/grafana --namespace data-platform -f values.yaml
# Uninstall Grafana
helm uninstall my-grafana --namespace data-platform
```

References:
- [Deploy Grafana using Helm Charts](https://grafana.com/docs/grafana/latest/setup-grafana/installation/helm/#enable-persistent-storage-recommended)
- [helm-charts/charts/grafana/values.yaml](https://github.com/grafana/helm-charts/blob/main/charts/grafana/values.yaml)
