import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

class TestDataHelper:
    """Helper class for test data management"""
    
    @staticmethod
    def load_test_data(file_name: str) -> Dict[str, Any]:
        """Load test data from JSON file"""
        data_dir = Path("tests/test_data")
        file_path = data_dir / file_name
        
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}
    
    @staticmethod
    def save_test_results(test_name: str, results: Dict[str, Any]) -> None:
        """Save test results to JSON file"""
        results_dir = Path("reports/test_results")
        results_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = results_dir / f"{test_name}_{timestamp}.json"
        
        with open(file_path, 'w') as f:
            json.dump(results, f, indent=2)

class ScreenshotHelper:
    """Helper class for screenshot management"""
    
    @staticmethod
    def create_screenshot_dir() -> Path:
        """Create screenshot directory"""
        screenshot_dir = Path("reports/screenshots")
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        return screenshot_dir
    
    @staticmethod
    def generate_screenshot_name(test_name: str, step: str = "") -> str:
        """Generate screenshot filename"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
        if step:
            return f"{test_name}_{step}_{timestamp}.png"
        return f"{test_name}_{timestamp}.png"

class FileHelper:
    """Helper class for file operations"""
    
    @staticmethod
    def ensure_directory_exists(directory_path: str) -> None:
        """Ensure directory exists, create if not"""
        Path(directory_path).mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def clean_directory(directory_path: str, keep_files: int = 10) -> None:
        """Clean directory keeping only the latest files"""
        directory = Path(directory_path)
        if not directory.exists():
            return
        
        files = sorted(directory.glob("*"), key=lambda x: x.stat().st_mtime, reverse=True)
        for file in files[keep_files:]:
            if file.is_file():
                file.unlink()

class EnvironmentHelper:
    """Helper class for environment management"""
    
    @staticmethod
    def get_env_var(var_name: str, default_value: str = "") -> str:
        """Get environment variable with default"""
        return os.getenv(var_name, default_value)
    
    @staticmethod
    def is_debug_mode() -> bool:
        """Check if running in debug mode"""
        return os.getenv("DEBUG", "false").lower() == "true"
    
    @staticmethod
    def get_test_environment() -> str:
        """Get test environment (dev, staging, prod)"""
        return os.getenv("TEST_ENV", "default")