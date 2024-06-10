### Incident Postmortem: Load Balancer Installation and Nginx Server Issues

### Issue Summary
	* Duration of Outage: Friday, June 7th, 2024 from 10:30 AM GMT  to 12:45 PM GMT (2 hours and 15 minutes)
	* Impact: It was inaccessible to users for approximately two hours. The server received a "404" error message. And the server was inaccessible.
	* Root Cause: A combination of misconfiguration during load balancer installation and oversight in the Nginx server configuration led to the application outage.

### Timeline
	* 10:30 AM GMT: I began installing a new load balancer to distribute traffic across two Nginx servers.
	* 10:45 AM GMT: The initial configuration of the load balancer appeared successful. However, upon attempting to route traffic through the load balancer, the application became unavailable.
	* 11:00 AM GMT: I investigated the issue and discovered the load balancer health checks were not configured correctly. The health checks were configured to ping a specific port on the Nginx servers that was not being used by the application.
	* 11:15 AM GMT: The load balancer health checks were corrected to ping the appropriate port used by the application. However, the application remained unavailable.
	* 11:30 AM GMT: Further investigation revealed an error in the Nginx server configuration. The Nginx servers were not configured to listen on the port being used by the load balancer for health checks.
	* 11:45 AM GMT: The Nginx server configuration was corrected to list on the appropriate port.
	* Noon GMT: The load balancer and Nginx servers were verified as functional, and traffic was successfully routed through the load balancer.
	* 12:45 PM GMT: The incident was declared resolved.

### Root Cause and Resolution

The root cause of the incident was twofold. First, the initial configuration of the load balancer health checks was incorrect. The health checks were pinging the wrong port on the Nginx servers, causing the load balancer to mark the servers as unhealthy and not route traffic to them. Second, the Nginx server configuration was missing a crucial step. The servers were not configured to listen on the port the load balancer was using for health checks, preventing the load balancer from establishing a healthy connection.
The resolution involved correcting both configuration errors. The load balancer health checks were updated to ping the correct port used by the application. The Nginx server configuration was also modified to list the designated port for health checks.

### Corrective and Preventative Measures
Implement a mandatory code review process for all load balancer configuration changes.
Update the load balancer installation documentation to detail the health check configuration explicitly.
Include a verification step in the deployment process to confirm communication between the load balancer and Nginx servers.
Enhance the Nginx server configuration documentation to clearly outline the required settings for integration with a load balancer.
Lessons Learned
This incident highlights the importance of thorough testing and configuration review during deployments.
Improved Communication: I will improve communication during deployments. This will involve including the operations team throughout the process to ensure a smooth transition when routing traffic through the new load balancer.
Testing Procedures: I will develop more comprehensive testing procedures to validate the integration between the load balancer and Nginx servers before deploying to production. This will include testing load balancer health checks and ensuring proper communication between all components.

