Python Application Example
===

## Prerequisites
Check [here](../../README.md#prerequisites)

## Development guide
- Build docker image:
```bash
$ docker build -t python-app-example:latest .
# Verify
$ docker image ls
: '
REPOSITORY                     TAG           IMAGE ID       CREATED          SIZE
python-app-example             latest        5c19c8d5f3c8   10 minutes ago   445MB
'
# Test docker run
$ docker run python-app-example:latest
: '
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8123 (Press CTRL+C to quit)
'
```

- Push docker image to docker hub:
```bash
$ docker login
Login Succeeded
$ docker tag python-app-example:latest mrroot501/python-app-example:latest
$ docker push mrroot501/python-app-example:latest
# Verify
$  docker search mrroot501/python-app-example
NAME                                             DESCRIPTION                                     STARS     OFFICIAL
mrroot501/python-app-example                                                                     0         
```

- Deploy application on K8s:
```bash
# Switch to data-platform namespace
$ kubectl config set-context --current --namespace=data-platform
$ kubectl apply -f k8s/python_api.yaml
deployment.apps/python-api created
$ kubectl get deployment
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-api   3/3     3            3           72s
$ kubectl get pods
: '
NAME                          READY   STATUS    RESTARTS   AGE
python-api-7d7b764c66-brfb4   1/1     Running   0          5m9s
python-api-7d7b764c66-nd85b   1/1     Running   0          5m9s
python-api-7d7b764c66-rjgm9   1/1     Running   0          5m9s
'
```

- Expose pods to external:
```bash
$ kubectl get svc python-api
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP                                                                   PORT(S)        AGE
python-api   LoadBalancer   10.100.207.244   aa96d9a54375c45ebae77185a918646b-866320457.ap-southeast-2.elb.amazonaws.com   80:30725/TCP   16m
# Test api
$ curl aa96d9a54375c45ebae77185a918646b-866320457.ap-southeast-2.elb.amazonaws.com:80/health
{"status":"200 OK"}
```

- Remove deployment:
```bash
$ kubectl get deployment
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-api   3/3     3            3           24m
$ kubectl delete deployment python-api
deployment.apps "python-api" deleted
```

## References:
- [Deploying a Python Application with Kubernetes](https://komodor.com/blog/deploying-a-python-application-with-kubernetes/)
