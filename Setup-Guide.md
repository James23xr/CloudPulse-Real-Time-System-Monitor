# Setup Guide

This guide will walk you through the process of setting up CloudPulse on your local machine for development purposes.

## Prerequisites

- Python 3.9+
- Docker
- Git

## Installation Steps

1. Clone the repository:
`git clone https://github.com/yourusername/cloudpulse.git`
2. Navigate to the project directory:
`cd cloudpulse`

3. Create a virtual environment:
`python -m venv venv`

4. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On macOS and Linux: `source venv/bin/activate`

5. Install the required packages:
`pip install -r requirements.txt`

6. Run the application:
`python app.py`

7. Access the application at `http://localhost:5000`

For Docker setup, refer to the [Deployment Guide](https://github.com/yourusername/cloudpulse/blob/main/docs/deployment-guide.md).
