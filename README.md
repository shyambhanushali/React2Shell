# React2Shell



     /$$$$$$$                                  /$$      /$$$$$$   /$$$$$$  /$$                 /$$ /$$
    | $$__  $$                                | $$     /$$__  $$ /$$__  $$| $$                | $$| $$
    | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$  |__/  \ $$| $$  \__/| $$$$$$$   /$$$$$$ | $$| $$
    | $$$$$$$/ /$$__  $$ |____  $$ /$$_____/|_  $$_/    /$$$$$$/|  $$$$$$ | $$__  $$ /$$__  $$| $$| $$
    | $$__  $$| $$$$$$$$  /$$$$$$$| $$        | $$     /$$____/  \____  $$| $$  \ $$| $$$$$$$$| $$| $$
    | $$  \ $$| $$_____/ /$$__  $$| $$        | $$ /$$| $$       /$$  \ $$| $$  | $$| $$_____/| $$| $$
    | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/| $$$$$$$$|  $$$$$$/| $$  | $$|  $$$$$$$| $$| $$
    |__/  |__/ \_______/ \_______/ \_______/   \___/  |________/ \______/ |__/  |__/ \_______/|__/|__/
                                                                                                      
                                                                                                      
               @shyambhanushali @nickvourd                                                                                       


## Overview

React2Shell is a Python-based proof-of-concept tool designed to exploit CVE-2025-55182 and CVE-2025-66478, both impacting Next.js applications using React Server Components (RSC).
The tool enables remote JavaScript execution (RCE) by generating and delivering malicious payload that abuses RSC deserialization behavior.
It is intended for security researchers, penetration testers, and red-team operators performing authorized assessments.

## Disclaimer

This tool is provided strictly for educational and security research purposes.
The authors assume no liability for misuse.
You are solely responsible for ensuring legal and authorized usage.

## Version & Credits

React2Shell v1.0 – Python-based RCE PoC for CVE-2025-55182 / CVE-2025-66478
Written with ❤️ by @shyambhanushali & @nickvourd
Licensed under MIT

Repository: https://github.com/shyambhanushali/React2Shell---CVE-2025-55182-CVE-2025-66478


## USAGE 

react2shell.py [-h] -t TARGET -c COMMAND


options:

  -h, --help            show this help message and exit
  
  -t, --target TARGET   Target URL (e.g. http://localhost:3000)
  
  -c, --command COMMAND Command to Execute on the Target
