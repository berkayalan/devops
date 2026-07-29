## How to add a label to a node?

kubectl label nodes mynode size=Large

## How to add selector to a Pod?

```
apiVersion: v1
kind: Pod
metadata:
  name: berkay-pod
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    size: Large
```

## Node Affinity

Node affinity is conceptually similar to nodeSelector, allowing you to constrain which nodes your Pod can be scheduled on based on node labels. There are two types of node affinity:

 - requiredDuringSchedulingIgnoredDuringExecution: The scheduler can't schedule the Pod unless the rule is met. This functions like nodeSelector, but with a more expressive syntax.

 - preferredDuringSchedulingIgnoredDuringExecution: The scheduler tries to find a node that meets the rule. If a matching node is not available, the scheduler still schedules the Pod.

You can use the operator field to specify a logical operator for Kubernetes to use when interpreting the rules. You can use 'In', 'NotIn', 'Exists', 'DoesNotExist', 'Gt' and 'Lt'.

