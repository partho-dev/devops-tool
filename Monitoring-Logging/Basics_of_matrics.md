
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
o	Percentage of CPU resources currently in use.
o	Key threshold: Should ideally stay below 85%.
- Memory Usage:
o	Amount of RAM in use by applications or processes.
o	Threshold: Leave enough buffer to avoid memory swaps.
- Disk I/O:
o	The rate of reading/writing operations to the disk.
o	Measured in Input/Output Operations Per Second (IOPS).
- Disk Space Utilization:
o	Percentage of disk storage used.
o	Threshold: Ensure at least 15-20% free space.
- Network Bandwidth:
o	Amount of data transmitted/received over the network.
o	Measured in Mbps or Gbps.
- Network Latency:
o	Time taken for data packets to travel from source to destination.
o	Measured in ms.
- Connection Count:
o	Number of active connections to the server.
 
`3.` **Kubernetes Metrics**
- Pod Resource Usage:
o	CPU and Memory usage of individual pods.
- Replica Health:
o	Number of replicas available vs. desired replicas.
- Pod Restarts:
o	Frequency of pod restarts (may indicate issues with container stability).
- Node Utilization:
o	CPU, memory, and disk usage at the node level.
- Control Plane Latency:
o	Latency in Kubernetes API calls.
- Container Disk I/O:
o	Read/write operations performed by containers.
 
`4.` **Database Metrics**
- Query Latency:
o	Time taken to execute a database query.
- Connections:
o	Number of active connections to the database.
- Cache Hit Ratio:
o	Percentage of queries served from the cache vs. total queries.
o	Ideal ratio: >95%.
- Locks/Deadlocks:
o	Number of queries waiting for locks or encountering deadlocks.
- Replication Lag:
o	Time delay between the primary and replica databases.
 
`5.` **Firewall/Gateway Metrics**
- Active Sessions:
o	Number of concurrent sessions handled by the firewall.
- Traffic Throughput:
o	Volume of traffic passing through the firewall.
o	Measured in Mbps or Gbps.
- Blocked Requests:
o	Number of requests blocked due to security rules.
- Packet Drops:
o	Percentage of packets dropped by the firewall.
 
`6.` **Cloud-Specific Metrics**
***AWS CloudWatch:***
- CPU Credit Balance (Burstable Instances):
o	Indicates if burstable EC2 instances can sustain high CPU usage.
- Request Count (ELB):
o	Number of requests processed by a load balancer.
- 4xx/5xx Errors:
o	Count of client/server errors at the load balancer.
- Read/Write Latency (RDS):
o	Latency of database read/write operations.
***Azure Monitor:***
- DTU Utilization (SQL Database):
o	Database Transaction Units used vs. provisioned.
- Throttled Requests (Storage):
o	Number of requests throttled due to resource limits.
 
`7.` **Monitoring Tools and Dashboards**
- Prometheus/Grafana:
o	Ideal for custom metrics and visualizations for both Kubernetes and bare-metal servers.
- Datadog/New Relic:
o	Comprehensive application performance monitoring (APM) tools.
- Cloud-Native Services:
o	AWS CloudWatch, Azure Monitor, Google Cloud Operations.
 
**Best Practices for Monitoring**
1.	Set Alerts: Define thresholds for critical metrics to trigger notifications.
2.	Use Dashboards: Aggregate key metrics into intuitive dashboards for easy monitoring.
3.	Automate Scaling: Use metrics to trigger auto-scaling actions.
4.	Enable Logging: Correlate logs with metrics for deeper insights.
5.	Analyze Trends: Regularly review trends to predict and prevent potential issues.
 
This comprehensive set of metrics ensures you can effectively monitor and troubleshoot web application performance. Tailor your dashboards and alerts based on these categories to maintain a healthy and performant system.

