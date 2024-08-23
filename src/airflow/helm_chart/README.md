Apache Airflow - Helm chart
===

## Prerequisites
- Enviroments: [here](../../../README.md#prerequisites)
- Create `airflow-ssh-secret` for gitSync:
```bash
# Make sure you already to add your private key to GitHub
$ kubectl create secret generic airflow-ssh-secret --from-file=gitSshKey=/home/mrroot501/.ssh/id_rsa
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
# Create PersistanceVoumeClaim for Airflow
$ kubectl apply -f k8s/pv_claim.yaml
: '
persistentvolumeclaim/data-airflow-postgresql-0 created
persistentvolumeclaim/redis-db-airflow-redis-0 created
persistentvolumeclaim/logs-airflow-triggerer-0 created
persistentvolumeclaim/logs-airflow-worker-0 created
'
# Install airflow
$ helm install airflow apache-airflow/airflow --namespace data-platform -f k8s/values.yaml --debug
# Access airlfow UI
$ kubectl port-forward svc/airflow-webserver 8080:8080
# Apply changes in values.yaml
$ helm upgrade airflow apache-airflow/airflow --namespace data-platform -f k8s/values.yaml --debug
```

- Uninstall Airflow
```bash
$ helm delete airflow -n data-platform
$ kubectl delete pvc --all
$ kubectl delete pv --all
```

Ref links:
- [Airflow Helm Chart](https://artifacthub.io/packages/helm/apache-airflow/airflow)
- [Airflow Production Guide](https://airflow.apache.org/docs/helm-chart/stable/production-guide.html#values-file)
- [Airflow on Kubernetes with Helm](https://hungngph.medium.com/airflow-on-kubernetes-with-helm-c795545325dc)
