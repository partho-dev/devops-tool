- Jenkins is configured as a deployment on EKS
- To run the pipeline on this Jenkins, we can use kubernetes as pod for running jobs as an agent

> # How to setup the kubernetes as a pod for Jenkins

- Login to Jenkins (Linked with k8s ingress)
- install `Kubernetes` plugins
- Disabled the `default - build executor`


- Need these to setup the kubentets cloud on Jenkins
1. Create ns - kubectl create ns jenkins
2. create sa - kubectl create serviceaccount jenkins-sa --namespace=jenkins
3. Create token on the SA - jenkins-token.yaml 
```
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: jenkins-token
  annotations:
    kubernetes.io/service-account.name: jenkins
```
4. kubectl -n jenkins create -f jenkins-token.yaml 

5. Find the token of the user - `kubectl describe secret $(kubectl describe serviceaccount jenkins-sa --namespace=jenkins | grep Token | awk '{print $2}') -n jenkins`

- Alternatively for K8s version 1.24 and above, the creation of token for servce account became easier 
  - `kubectl create token jenkins --namespace jenkins`
- This one command can eliminate the step `3` `4` & `5`
- This one command handles the `creation` of the token, its `association` secret in one step.

5. Find the ssl of the kubernetes - `kubectl get configmap -n kube-public kube-root-ca.crt -o jsonpath='{.data.ca\.crt}'`

6. give the permission to the user by binding its role to kubernetes admin role binding - `kubectl create rolebinding jenkins-admin-binding --clusterrole=admin --serviceaccount=jenkins_ns:jenkins_sa --namespace=jenkins_ns`
7. To know about the cluster address - `kubectl cluster-info`