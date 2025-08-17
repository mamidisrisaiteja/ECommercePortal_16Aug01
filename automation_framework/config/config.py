import os
from pathlib import Path
from typing import Dict, Any
import yaml

class Config:
    """Configuration management for the test framework"""
    
    BASE_DIR = Path(__file__).parent.parent
    CONFIG_DIR = BASE_DIR / "config"
    REPORTS_DIR = BASE_DIR / "reports"
    
    # Default configuration
    DEFAULT_CONFIG = {
        "base_url": "https://www.saucedemo.com",
        "browser": {
            "name": "chromium",
            "headless": False,
            "timeout": 30000,
            "viewport": {"width": 1280, "height": 720}
        },
        "test_data": {
            "valid_username": "standard_user",
            "valid_password": "secret_sauce",
            "invalid_username": "standard_use",
            "invalid_password": "secret_sauce"
        },
        "timeouts": {
            "default": 30000,
            "short": 5000,
            "long": 60000
        },
        "screenshots": {
            "enabled": True,
            "on_failure": True,
            "path": "reports/screenshots"
        }
    }
    
    @classmethod
    def load_config(cls, env: str = "default") -> Dict[str, Any]:
        """Load configuration from file or return default"""
        config_file = cls.CONFIG_DIR / f"{env}.yaml"
        
        if config_file.exists():
            with open(config_file, 'r') as f:
                file_config = yaml.safe_load(f)
                # Merge with default config
                config = {**cls.DEFAULT_CONFIG, **file_config}
        else:
            config = cls.DEFAULT_CONFIG.copy()
            
        # Override with environment variables
        if os.getenv("BASE_URL"):
            config["base_url"] = os.getenv("BASE_URL")
            
        if os.getenv("BROWSER_NAME"):
            config["browser"]["name"] = os.getenv("BROWSER_NAME")
            
        headless_env = os.getenv("HEADLESS")
        if headless_env:
            config["browser"]["headless"] = headless_env.lower() == "true"
            
        return config
    
    @classmethod
    def get_base_url(cls) -> str:
        return cls.load_config().get("base_url", cls.DEFAULT_CONFIG["base_url"])
    
    @classmethod
    def get_browser_config(cls) -> Dict[str, Any]:
        return cls.load_config().get("browser", cls.DEFAULT_CONFIG["browser"])
    
    @classmethod
    def get_test_data(cls) -> Dict[str, Any]:
        return cls.load_config().get("test_data", cls.DEFAULT_CONFIG["test_data"])