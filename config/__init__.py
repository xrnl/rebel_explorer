import os

def load_config():
    """configuration loading"""
    mode = os.environ.get("MODE")
    try:
        if mode == 'TESTING':
            from .testing import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .default import Config
        return Config