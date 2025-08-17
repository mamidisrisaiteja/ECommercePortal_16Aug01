import pytest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import all fixtures
from fixtures.browser_fixtures import *

def pytest_configure(config):
    """Configure pytest"""
    # Create reports directory
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    (reports_dir / "screenshots").mkdir(exist_ok=True)
    (reports_dir / "videos").mkdir(exist_ok=True)
    (reports_dir / "logs").mkdir(exist_ok=True)
    (reports_dir / "allure-results").mkdir(exist_ok=True)

def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names"""
    for item in items:
        # Add markers based on test case IDs in test names - Only Authentication Module
        if "TC_AUTH_" in item.name:
            item.add_marker(pytest.mark.auth)
        
        # Add TC-specific markers
        if "TC_AUTH_01" in item.name:
            item.add_marker(pytest.mark.smoke)
        elif "TC_AUTH_02" in item.name:
            item.add_marker(pytest.mark.regression)