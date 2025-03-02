import os
import argparse
import subprocess
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from rich.console import Console
from rich.table import Table

console = Console()

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

def subdomain_enumeration(target):
    console.print(f"[bold cyan]Enumerating subdomains for {target}...[/bold cyan]")
    command = f"python3 Sublist3r/sublist3r.py -d {target} -o {target}_subdomains.txt"
    return run_command(command)

def directory_bruteforce(target):
    console.print(f"[bold cyan]Brute-forcing directories for {target}...[/bold cyan]")
    command = f"python3 dirsearch/dirsearch.py -u {target} -e php,html,js -w wordlists.txt"
    return run_command(command)

def vulnerability_scan(target):
    console.print(f"[bold cyan]Scanning vulnerabilities on {target}...[/bold cyan]")
    command = f"nuclei -u {target} -o {target}_vulns.txt"
    return run_command(command)

def port_scan(target):
    console.print(f"[bold cyan]Scanning open ports for {target}...[/bold cyan]")
    command = f"nmap -sV {target}"
    return run_command(command)

def capture_screenshot(target):
    console.print(f"[bold cyan]Capturing screenshot of {target}...[/bold cyan]")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(target)
    driver.save_screenshot(f"{target}_screenshot.png")
    driver.quit()
    return f"Screenshot saved: {target}_screenshot.png"

def generate_report(target, data):
    console.print(f"[bold cyan]Generating report for {target}...[/bold cyan]")
    with open(f"{target}_report.json", "w") as f:
        json.dump(data, f, indent=4)
    return f"Report saved: {target}_report.json"

def main():
    parser = argparse.ArgumentParser(description="WhyCheck - Automated Bug Bounty Scanner")
    parser.add_argument("--target", required=True, help="Target website to scan")
    args = parser.parse_args()
    target = args.target

    results = {
        "subdomains": subdomain_enumeration(target),
        "directories": directory_bruteforce(target),
        "vulnerabilities": vulnerability_scan(target),
        "ports": port_scan(target),
        "screenshot": capture_screenshot(target),
    }

    console.print("\n[bold green]Scan Completed![/bold green]")
    generate_report(target, results)

if __name__ == "__main__":
    main()
