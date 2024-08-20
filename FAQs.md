# Frequently Asked Questions (FAQs)

## General Questions

Q: What is CloudPulse?
A: CloudPulse is a real-time system monitoring tool designed for cloud environments, providing instant insights into CPU and memory utilization.

Q: Is CloudPulse free to use?
A: Yes, CloudPulse is open-source and free to use under the MIT License.

## Technical Questions

Q: What technologies does CloudPulse use?
A: CloudPulse is built with Python, Flask, Docker, and Kubernetes. It uses Plotly.js for data visualization.

Q: Can CloudPulse monitor remote servers?
A: The current version of CloudPulse monitors the system it's running on. Monitoring remote servers is a planned feature for future releases.

Q: How often does CloudPulse update its metrics?
A: By default, CloudPulse updates metrics every 5 seconds. This interval can be configured in the application settings.

## Deployment Questions

Q: Can I deploy CloudPulse on non-AWS cloud providers?
A: While our deployment guide focuses on AWS, CloudPulse can be deployed on any cloud provider that supports Docker and Kubernetes.

Q: How do I scale CloudPulse?
A: CloudPulse can be scaled horizontally by adjusting the number of replicas in your Kubernetes deployment.

For more detailed information, please refer to the specific sections of the [Deployment Guide](https://github.com/James23xr/cloudpulse/blob/main/docs/deployment-guide.md).
