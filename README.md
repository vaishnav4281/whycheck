# WhyCheck - Advanced Bug Bounty Scanner

WhyCheck is a powerful, automated bug bounty tool designed to assist security researchers in identifying vulnerabilities efficiently. It combines multiple scanning techniques into a single script to help streamline reconnaissance and security analysis.

## Features
✅ **Subdomain Enumeration** (Uses Sublist3r)  
✅ **Directory Brute-Forcing** (Uses dirsearch)  
✅ **Vulnerability Scanning** (Uses Nuclei)  
✅ **Port Scanning** (Uses Nmap)  
✅ **Website Screenshot Capture** (Uses Selenium)  
✅ **Detailed JSON Report Generation**  
✅ **Customizable and Extensible for Advanced Scanning**  

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Git
- Chrome & Chromedriver (for Selenium screenshots)

### Clone the Repository
```sh
git clone https://github.com/vaishnav4281/whycheck.git
cd whycheck
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage

### Basic Scan
```sh
python3 whycheck.py --target https://example.com
```

### Advanced Usage
```sh
python3 whycheck.py --target https://example.com --full-scan --screenshot
```

### Available Options
| Option            | Description                                      |
|------------------|------------------------------------------------|
| `--target`       | Specify the target domain                       |
| `--subdomains`   | Perform subdomain enumeration                   |
| `--directories`  | Brute-force hidden directories                  |
| `--vulnerabilities` | Scan for known vulnerabilities (Nuclei)        |
| `--ports`        | Perform port scanning (Nmap)                    |
| `--screenshot`   | Capture a screenshot of the target website      |
| `--full-scan`    | Perform all available scans                     |
| `--output`       | Save results in a JSON report                   |

## Example Output
```
[+] Scanning Target: https://example.com
[*] Enumerating subdomains...
[*] Running directory brute-force...
[*] Scanning for vulnerabilities...
[*] Capturing website screenshot...
[✔] Scan completed successfully! Report saved: reports/example.com_report.json
```

## Contributing
Feel free to fork and improve **WhyCheck**. Contributions are welcome!

## License
This project is licensed under the MIT License.

---
**Happy Bug Hunting! 🕵️‍♂️🚀**

