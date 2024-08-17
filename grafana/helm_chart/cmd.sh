curl -silent a32ae939d481d4e75a9d2ed04931b528-1737447523.ap-southeast-2.elb.amazonaws.com:80 | grep title
curl -silent a13c54e87bef149b29bacf6f679f7990-96034643.ap-southeast-2.elb.amazonaws.com:80 | grep title

kubectl expose deployment my-grafana --namespace data-platform --type=ClusterIP  --name=nginx-service-cluster-ip

kubectl expose deployment my-grafana --namespace data-platform  --type=LoadBalancer  --name=nginx-service-loadbalancer-data-platform


# kubectl expose deployment my-grafana --namespace data-platform --port=80 --target-port=3000 --name nginx-exposed-svc --type LoadBalancer
kubectl expose deployment my-grafana --namespace data-platform --port=3000 --target-port=3000 --name nginx-exposed-svc --type LoadBalancer


