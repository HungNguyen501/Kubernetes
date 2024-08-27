Python Streaming Job Example
===

## Prerequisites
Check [here](../../README.md#prerequisites)

## Development guide
- Build docker image:
```bash
$ docker build -t streaming-k8s-job-example:v2024.08.25 .
# Verify
$ docker image ls
: '
REPOSITORY                     TAG           IMAGE ID       CREATED         SIZE
streaming-k8s-job-example            v2024.08.25   f073f5fb8b4e   6 hours ago     408MB
'
# Test docker run
$ docker run -e CREDENTIALS=123a@ \
    streaming-k8s-job-example:v2024.08.25 \
    /usr/bin/env python3 /app/main.py
: '
2024-08-27 00:53:06.197 | INFO     | __main__:<module>:24 - {'event_time': '2024-08-27 00:53:06', 'name': 'Katherine Mccoy', 'email': 'autumnnelson@example.com', 'credentials': '123a@'}
2024-08-27 00:54:06.201 | INFO     | __main__:<module>:24 - {'event_time': '2024-08-27 00:54:06', 'name': 'Benjamin Yu', 'email': 'bishopjonathon@example.net', 'credentials': '123a@'}
'
```

- Push docker image to docker hub:
```bash
$ docker login
Login Succeeded
$ docker tag streaming-k8s-job-example:v2024.08.25 mrroot501/streaming-k8s-job-example:v2024.08.25
$ docker push mrroot501/streaming-k8s-job-example:v2024.08.25
# Verify
$  docker search mrroot501/streaming-k8s-job-example
: '
NAME                                      DESCRIPTION                             STARS     OFFICIAL
mrroot501/streaming-k8s-job-example                                               0         
'
```

- Deploy application on K8s:
```bash
# Validate syntax
$ kustomize build k8s/overlays/dev
$ kubectl apply -k k8s/overlays/dev
: '
cronjob.batch/streaming-k8s-job-example created
'
$ kubectl get deployments
: '
NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
streaming-k8s-job-example   3/3     3            3           4m46s
'
```

- Remove deployment:
```bash
$ $ kubectl delete deployment streaming-k8s-job-example
: '
deployment.apps "streaming-k8s-job-example" deleted
'
```

