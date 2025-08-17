#!/usr/bin/env python3
"""
Test Execution Script for E-commerce Test Automation Framework
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_command(command, description):
    """Run shell command and handle errors"""
    print(f"\n🔄 {description}")
    print(f"Running: {command}")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"❌ {description} failed")
        print(f"Error: {result.stderr}")
        return False
    return True

def install_dependencies():
    """Install Python dependencies"""
    return run_command("pip install -r requirements.txt", "Installing Python dependencies")

def install_playwright():
    """Install Playwright browsers"""
    return run_command("playwright install", "Installing Playwright browsers")

def run_tests(args):
    """Run tests based on provided arguments"""
    cmd_parts = ["pytest"]
    
    # Add markers/tags
    if args.tags:
        cmd_parts.append(f"-m {args.tags}")
    
    # Add browser
    if args.browser:
        cmd_parts.append(f"--browser={args.browser}")
    
    # Add headless mode
    if args.headless:
        cmd_parts.append("--headed=false")
    
    # Add parallel execution
    if args.parallel:
        cmd_parts.append(f"-n {args.parallel}")
    
    # Add specific test
    if args.test:
        cmd_parts.append(f"-k {args.test}")
    
    # Add reporting
    cmd_parts.append("--html=reports/report.html --self-contained-html")
    cmd_parts.append("--alluredir=reports/allure-results")
    
    # Add verbose output
    if args.verbose:
        cmd_parts.append("-v")
    
    command = " ".join(cmd_parts)
    return run_command(command, f"Running tests with command: {command}")

def generate_allure_report():
    """Generate and serve Allure report"""
    if not Path("reports/allure-results").exists():
        print("❌ No Allure results found. Run tests first.")
        return False
    
    return run_command("allure serve reports/allure-results", "Generating Allure report")

def clean_reports():
    """Clean previous test reports"""
    dirs_to_clean = ["reports/screenshots", "reports/videos", "reports/logs", "reports/allure-results"]
    
    for dir_path in dirs_to_clean:
        if Path(dir_path).exists():
            run_command(f"rm -rf {dir_path}/*", f"Cleaning {dir_path}")
    
    print("✅ Reports cleaned")

def main():
    parser = argparse.ArgumentParser(description="E-commerce Test Automation Framework")
    parser.add_argument("--setup", action="store_true", help="Setup dependencies")
    parser.add_argument("--clean", action="store_true", help="Clean previous reports")
    parser.add_argument("--tags", help="Test tags to run (auth, smoke, regression)")
    parser.add_argument("--browser", choices=["chromium", "firefox", "webkit"], default="chromium", help="Browser to use")
    parser.add_argument("--headless", action="store_true", help="Run in headless mode")
    parser.add_argument("--parallel", type=int, help="Number of parallel workers (e.g., 4 or 'auto')")
    parser.add_argument("--test", help="Specific test to run (e.g., TC_AUTH_01)")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--report", action="store_true", help="Generate Allure report")
    
    args = parser.parse_args()
    
    # Change to framework directory
    framework_dir = Path(__file__).parent
    os.chdir(framework_dir)
    
    print("🚀 E-commerce Test Automation Framework")
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Setup dependencies
    if args.setup:
        if not install_dependencies():
            sys.exit(1)
        if not install_playwright():
            sys.exit(1)
        print("✅ Setup completed successfully")
        return
    
    # Clean reports
    if args.clean:
        clean_reports()
        return
    
    # Generate Allure report
    if args.report:
        generate_allure_report()
        return
    
    # Run tests
    if not run_tests(args):
        sys.exit(1)
    
    print("\n🎉 Test execution completed!")
    print("📊 Check reports in the 'reports' folder")
    print("🌐 For Allure report, run: python run_tests.py --report")

if __name__ == "__main__":
    main()
