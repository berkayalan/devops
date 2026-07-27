## Taints and Tolerations

Taints and Tolerations work together in Kubernetes to ensure pods are not scheduled on inappropriate nodes. Taints are applied to nodes (acting as a "lock") to repel pods, while tolerations are applied to pods (acting as a "key") to allow them to be scheduled on those tainted nodes.

### Taint Effects

**NoExecute**
    Pods that do not tolerate the taint are evicted immediately
    Pods that tolerate the taint without specifying tolerationSeconds in their toleration specification remain bound forever
    Pods that tolerate the taint with a specified tolerationSeconds remain bound for the specified amount of time. After that time elapses, the node lifecycle controller evicts the Pods from the node.

**NoSchedule**
    No new Pods will be scheduled on the tainted node unless they have a matching toleration. Pods currently running on the node are not evicted.

**PreferNoSchedule**
    PreferNoSchedule is a "preference" or "soft" version of NoSchedule. The control plane will try to avoid placing a Pod that does not tolerate the taint on the node, but it is not guaranteed.

You can put multiple taints on the same node and multiple tolerations on the same pod. The way Kubernetes processes multiple taints and tolerations is like a filter: start with all of a node's taints, then ignore the ones for which the pod has a matching toleration; the remaining un-ignored taints have the indicated effects on the pod. 

### Taint a Node

kubectl taint nodes node1 key1=value1:NoSchedule
kubectl taint nodes node01 maintainer=berkaytest:NoSchedule

### Untaint a Node

kubectl taint nodes node1 key1=value1:NoSchedule-
kubectl taint nodes node01 maintainer=berkaytest:NoSchedule-

### Add Toleration to a Pod

```apiVersion: v1
kind: Pod
metadata:
  name: berkay-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "maintainer"
    operator: "Equal"
    value: "berkaytest"
    effect: "NoSchedule"```
