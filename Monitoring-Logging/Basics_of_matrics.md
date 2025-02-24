
https://docs.google.com/spreadsheets/d/1P64yLVrXvCfpCx-0KFwcCcbQU2aD-6df/edit?gid=2073752426#gid=2073752426


**Performance Metrics for Monitoring Web Applications**
- Monitoring the performance and health of a web application involves understanding key metrics collected from servers, 
    - networks, 
    - databases, and 
    - other infrastructure components. 
    
- Below is a detailed breakdown of essential metrics and their meanings across different layers of an application stack:
 
 `1.`**General Application Performance Metrics**
- Response Time (Latency):
    - Time taken by the server to process a request and send a response.
    - Measured in milliseconds (ms) or seconds (s).
- Throughput:
    - The number of requests processed by the server per second.
    - Measured in requests per second (RPS).
- Error Rate:
    - Percentage of requests that result in an error (e.g., 4xx or 5xx HTTP codes).
    - Formula: (Total errors / Total requests) * 100.
- Saturation:
    - Degree to which system resources (CPU, memory, etc.) are utilized.
- Capacity Unit:
    - A combined measure of `CPU utilization`, `concurrent connections`, and `network throughput`. 
    - `Example`: 1 Capacity Unit = 1 CPU core OR 2.5K concurrent connections OR 2.25 Mbps throughput.

 

`2.` **Server Metrics**
- CPU Utilization:
    - Percentage of CPU resources currently in use.
    - Key threshold: Should ideally stay below 85%.
- Memory Usage:
    - Amount of RAM in use by applications or processes.
    - Threshold: Leave enough buffer to avoid memory swaps.
- Disk I/O:
    - The rate of reading/writing operations to the disk.
    - Measured in Input/Output Operations Per Second (IOPS).
- Disk Space Utilization:
    - Percentage of disk storage used.
    - Threshold: Ensure at least 15-20% free space.
- Network Bandwidth:
    - Amount of data transmitted/received over the network.
    - Measured in Mbps or Gbps.
- Network Latency:
    - Time taken for data packets to travel from source to destination.
    - Measured in ms.
- Connection Count:
    - Number of active connections to the server.
 
`3.` **Kubernetes Metrics**
- Pod Resource Usage:
    - CPU and Memory usage of individual pods.
- Replica Health:
    - Number of replicas available vs. desired replicas.
- Pod Restarts:
    - Frequency of pod restarts (may indicate issues with container stability).
- Node Utilization:
    - CPU, memory, and disk usage at the node level.
- Control Plane Latency:
    - Latency in Kubernetes API calls.
- Container Disk I/O:
    - Read/write operations performed by containers.
 
`4.` **Database Metrics**
- Query Latency:
    - Time taken to execute a database query.
- Connections:
    - Number of active connections to the database.
- Cache Hit Ratio:
    - Percentage of queries served from the cache vs. total queries.
    - Ideal ratio: >95%.
- Locks/Deadlocks:
    - Number of queries waiting for locks or encountering deadlocks.
- Replication Lag:
    - Time delay between the primary and replica databases.
 
`5.` **Firewall/Gateway Metrics**
- Active Sessions:
    - Number of concurrent sessions handled by the firewall.
- Traffic Throughput:
    - Volume of traffic passing through the firewall.
    - Measured in Mbps or Gbps.
- Blocked Requests:
    - Number of requests blocked due to security rules.
- Packet Drops:
    - Percentage of packets dropped by the firewall.
 
`6.` **Cloud-Specific Metrics**
***AWS CloudWatch:***
- CPU Credit Balance (Burstable Instances):
    - Indicates if burstable EC2 instances can sustain high CPU usage.
- Request Count (ELB):
    - Number of requests processed by a load balancer.
- 4xx/5xx Errors:
    - Count of client/server errors at the load balancer.
- Read/Write Latency (RDS):
    - Latency of database read/write operations.
***Azure Monitor:***
- DTU Utilization (SQL Database):
    - Database Transaction Units used vs. provisioned.
- Throttled Requests (Storage):
    - Number of requests throttled due to resource limits.
 
`7.` **Monitoring Tools and Dashboards**
- Prometheus/Grafana:
    - Ideal for custom metrics and visualizations for both Kubernetes and bare-metal servers.
- Datadog/New Relic:
    - Comprehensive application performance monitoring (APM) tools.
- Cloud-Native Services:
    - AWS CloudWatch, Azure Monitor, Google Cloud Operations.
 
**Best Practices for Monitoring**
1.	Set Alerts: Define thresholds for critical metrics to trigger notifications.
2.	Use Dashboards: Aggregate key metrics into intuitive dashboards for easy monitoring.
3.	Automate Scaling: Use metrics to trigger auto-scaling actions.
4.	Enable Logging: Correlate logs with metrics for deeper insights.
5.	Analyze Trends: Regularly review trends to predict and prevent potential issues.
