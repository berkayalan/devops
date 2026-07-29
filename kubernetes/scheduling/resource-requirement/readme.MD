## Resource Requirement

When you specify a Pod, you can optionally specify how much of each resource a container needs. The most common resources to specify are CPU and memory (RAM).

When you specify the resource request for containers in a Pod, the kube-scheduler uses this information to decide which node to place the Pod on. When you specify a resource limit for a container, the kubelet enforces those limits so that the running container is not allowed to use more of that resource than the limit you set. The kubelet also reserves at least the request amount of that system resource specifically for that container to use.

### Requests and Limits

If the node where a Pod is running has enough of a resource available, it's possible (and allowed) for a container to use more resource than its request for that resource specifies.

For example, if you set a memory request of 256 MiB for a container, and that container is in a Pod scheduled to a Node with 8GiB of memory and no other Pods, then the container can try to use more RAM.

Limits are a different story. Both cpu and memory limits are applied by the kubelet (and container runtime), and are ultimately enforced by the kernel. On Linux nodes, the Linux kernel enforces limits with cgroups. The behavior of cpu and memory limit enforcement is slightly different.

cpu limits are enforced by CPU throttling. When a container approaches its cpu limit, the kernel will restrict access to the CPU corresponding to the container's limit. Thus, a cpu limit is a hard limit the kernel enforces. Containers may not use more CPU than is specified in their cpu limit.

memory limits are enforced by the kernel with out of memory (OOM) kills. When a container uses more than its memory limit, the kernel may terminate it. However, terminations only happen when the kernel detects memory pressure. Thus, a container that over allocates memory may not be immediately killed. This means memory limits are enforced reactively. A container may use more memory than its memory limit, but if it does, it may get killed.

**By default, k8s sets resource limits to 1 CPU and 512Mi of memory**

### CPU resource units

Limits and requests for CPU resources are measured in cpu units. In Kubernetes, 1 CPU unit is equivalent to 1 physical CPU core, or 1 virtual core, depending on whether the node is a physical host or a virtual machine running inside a physical machine.

Fractional requests are allowed. When you define a container with spec.containers[].resources.requests.cpu set to 0.5, you are requesting half as much CPU time compared to if you asked for 1.0 CPU. For CPU resource units, the quantity expression 0.1 is equivalent to the expression 100m, which can be read as "one hundred millicpu". Some people say "one hundred millicores", and this is understood to mean the same thing.

### Memory resource units

Limits and requests for memory are measured in bytes. You can express memory as a plain integer or as a fixed-point number using one of these quantity suffixes: E, P, T, G, M, k. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. The Kubernetes API also allows m as a suffix (for millibytes: 1/1000 of a byte), but this isn't useful to specify: you must always assign whole numbers of bytes, or sometimes larger chunks such as multiples of 1 gibibyte.

### Check Limit range of a namespace

kubectl describe limitrange berkay-namespaces

### Check Resource usage of a node

kubectl top nodes