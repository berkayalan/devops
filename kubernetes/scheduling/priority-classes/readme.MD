## PriorityClass

A PriorityClass is a non-namespaced object that defines a mapping from a priority class name to the integer value of the priority. The name is specified in the name field of the PriorityClass object's metadata. The value is specified in the required value field. The higher the value, the higher the priority. The name of a PriorityClass object must be a valid DNS subdomain name, and it cannot be prefixed with system-.

A PriorityClass object can have any 32-bit integer value smaller than or equal to 1 billion. This means that the range of values for a PriorityClass object is from -2147483648 to 1000000000 inclusive. Larger numbers are reserved for built-in PriorityClasses that represent critical system Pods. A cluster admin should create one PriorityClass object for each such mapping that they want.

> [!IMPORTANT]
> Kubernetes already ships with two PriorityClasses: system-cluster-critical and system-node-critical.

### Key Concepts

**Priority Value (value)**: A 32-bit integer up to 1,000,000,000 (1 billion). Higher numbers represent higher priority. Values greater than 1 billion are reserved for critical system components.

**Scheduling Queue Placement**: When multiple pods are waiting in the Pending state, the kube-scheduler orders the scheduling queue by priority. The pod with the highest priority value is evaluated for scheduling first.

**Preemption (preemptionPolicy)**: If a high-priority pod cannot find a node with sufficient resources (requests), the scheduler can evict (terminate) lower-priority pods from a node to free up compute space:

    - PreemptLowerPriority (Default): Allows evicting lower-priority pods to schedule the incoming pod.

    - Never: The pod jumps to the front of the scheduling queue, but it will not evict running workloads; it waits until capacity frees up naturally.
