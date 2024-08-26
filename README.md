K8s Handbook
===

## Prerequisites
<details>
<summary>Kubectl</summary>

```bash
$ kubectl version --client
Client Version: v1.30.3
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```
</details>

<details>
<summary>Helm</summary>

```bash
$ helm version
version.BuildInfo Version:"v3.15.3", GitCommit:"3bb50bbbdd9c946ba9989fbe4fb4104766302a64", GitTreeState:"clean", GoVersion:"go1.22.5"
```
</details>

<details>
<summary>Ready to connect an AWS EKS cluster</summary>

```bash
$ export AWS_PROFILE=hungnguyendinh
$ aws eks update-kubeconfig --region ap-southeast-2 --name dev-hungnguyendinh --kubeconfig ~/.kube/dev-hungnguyendinh-config
: '
Added new context arn:aws:eks:ap-southeast-2:025066273328:cluster/dev-hungnguyendinh to /home/mrroot501/.kube/dev-hungnguyendinh-config
'
$ export KUBECONFIG=~/.kube/dev-hungnguyendinh-config
# Create data-platform namespace
$ kubectl create namespace data-platform
# Set namespace context
$ kubectl config set-context --current --namespace=data-platform
```
</details>

<details>
<summary>Configure Amazon EBS CSI driver for working PersistentVolumes in EKS</summary>

```bash
# Install eksctl
$ curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
$ sudo mv /tmp/eksctl /usr/local/bin
# Enable IAM OIDC provider
$ eksctl utils associate-iam-oidc-provider --region=ap-southeast-2 --cluster=dev-hungnguyendinh --approve
: '
2024-08-22 21:34:33 [ℹ]  will create IAM Open ID Connect provider for cluster "dev-hungnguyendinh" in "ap-southeast-2"
2024-08-22 21:34:35 [✔]  created IAM Open ID Connect provider for cluster "dev-hungnguyendinh" in "ap-southeast-2"
'
# Create Amazon EBS CSI driver IAM role
$ eksctl create iamserviceaccount \
  --region ap-southeast-2 \
  --name ebs-csi-controller-sa \
  --namespace kube-system \
  --cluster dev-hungnguyendinh \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve \
  --role-only \
  --role-name AmazonEKS_EBS_CSI_DriverRole
: '
2024-08-22 21:37:18 [ℹ]  1 iamserviceaccount (kube-system/ebs-csi-controller-sa) was included (based on the include/exclude rules)
2024-08-22 21:37:18 [!]  serviceaccounts in Kubernetes will not be created or modified, since the option --role-only is used
2024-08-22 21:37:18 [ℹ]  1 task: create IAM role for serviceaccount "kube-system/ebs-csi-controller-sa"
2024-08-22 21:37:18 [ℹ]  building iamserviceaccount stack "eksctl-dev-hungnguyendinh-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
2024-08-22 21:37:19 [ℹ]  deploying stack "eksctl-dev-hungnguyendinh-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
2024-08-22 21:37:19 [ℹ]  waiting for CloudFormation stack "eksctl-dev-hungnguyendinh-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
2024-08-22 21:37:51 [ℹ]  waiting for CloudFormation stack "eksctl-dev-hungnguyendinh-addon-iamserviceaccount-kube-system-ebs-csi-controller-sa"
'
# Add the Amazon EBS CSI add-on
$ eksctl create addon --name aws-ebs-csi-driver --region ap-southeast-2 --cluster dev-hungnguyendinh \
  --service-account-role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/AmazonEKS_EBS_CSI_DriverRole --force
: '
024-08-22 21:40:32 [ℹ]  Kubernetes version "1.30" in use by cluster "dev-hungnguyendinh"
2024-08-22 21:40:34 [ℹ]  IRSA is set for "aws-ebs-csi-driver" addon; will use this to configure IAM permissions
2024-08-22 21:40:34 [!]  IRSA has been deprecated; the recommended way to provide IAM permissions for "aws-ebs-csi-driver" addon is via pod identity associations; after addon creation is completed, run `eksctl utils migrate-to-pod-identity`
2024-08-22 21:40:34 [ℹ]  using provided ServiceAccountRoleARN "arn:aws:iam::025066273328:role/AmazonEKS_EBS_CSI_DriverRole"
2024-08-22 21:40:34 [ℹ]  creating addon
'
```
</details>

## Handbooks

- [airflow-helm_chart](./services/airflow/helm_chart/README.md)
- [grafana-terraform](./services/grafana/terraform/README.md)
- [grafana-helm_chart](./services/grafana/helm_chart/README.md)
- [streaming_k8s_job_example](./services/streaming_k8s_job_example/README.md)
- [python_app_example](./services/python_app_example/README.md)
- [etl_k8s_job_example](./services/etl_k8s_job_example/README.md)
