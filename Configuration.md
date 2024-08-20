# Configuration

CloudPulse can be configured using environment variables or a configuration file.

## Environment Variables

- `FLASK_ENV`: Set to `development` for debug mode, `production` for production mode.
- `PORT`: The port on which the Flask app will run (default: 5000).
- `LOG_LEVEL`: Logging level (default: INFO).

## Configuration File

Create a `config.py` file in the root directory with the following structure:

```python
class Config:
    DEBUG = False
    TESTING = False
    LOG_LEVEL = 'INFO'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True
