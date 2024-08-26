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
2024-08-25 09:42:56.565 | INFO     | __main__:<module>:22 - {'event_date': '2024-08-25', 'name': 'Michael Brewer', 'email': 'johnsonpatricia@example.net', 'credentials': '123a@'}
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
NAME                                  DESCRIPTION                             STARS     OFFICIAL
mrroot501/streaming-k8s-job-example                                                 0         
'
```

- Deploy application on K8s:
```bash
# Validate syntax
$ kustomize buil k8s/overlays/dev
$ kubectl apply -k k8s/overlays/dev
: '
cronjob.batch/streaming-k8s-job-example created
'
$ kubectl get cronjob
: '
NAME                  SCHEDULE    TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
streaming-k8s-job-example   2 * * * *   <none>     False     0        16m             19m
'
```

- Remove deployment:
```bash
$ kubectl delete cronjob streaming-k8s-job-example
: '
cronjob.batch "streaming-k8s-job-example" deleted
'
```

