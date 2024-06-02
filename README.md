# Atlantis-Launcher-Decompiled

This repository contains the decompiled code for Atlantis Launcher, a tool designed to bypass application block walls by routing traffic through a local proxy server using the Proxifier app and Xray binary. Additionally, it functions as a launcher for a FiveM game server, allowing users to connect to the server after bypassing restrictions. This tool can also help resolve Discord connection block issues. The original tool can be found at [https://www.atlantisrp.ir/](https://www.atlantisrp.ir/).

## Disclaimer

I want to make it clear that I am not the creator of this tool. I decompiled and shared it out of curiosity and for educational purposes. I do not intend to fight against the original creators or misuse their work. This repository is simply for fun and exploration. Additionally, I take no responsibility for its security, functionality, or any potential misuse.

## Purpose of this Repository

The primary reason for creating this repository is to understand and analyze the logic behind the original tool. While the tool works effectively, there are some concerns and potential improvements:

1. **Use of Python**: The tool is written in Python, which is easy to use but not the most optimized choice for creating such applications. The tool was packaged using PyInstaller, which can lead to performance issues. Consider using a more efficient language or optimizing the current implementation.

2. **Port Usage**: The tool uses port 1080, a commonly used port. It's advisable to implement a mechanism to find an open port dynamically to avoid conflicts.

3. **Proxifier Configuration**: Configuring Proxifier to use dynamic configurations and enabling remote loading of the configuration can enhance flexibility and reduce issues related to static configurations.

4. **Process Management**: Instead of terminating processes by name, store and kill process IDs (PIDs) to manage processes more securely and efficiently. This approach avoids unintended consequences and enhances security.

5. **VPN Configuration**: The VPN server configuration lacks restrictions, which could be exploited if someone gains access. It's important to implement robust security measures to prevent unauthorized use.

6. **Logging and Security**: The tool does not log user data, which is good for privacy. However, it's essential to ensure that no sensitive information is exposed or logged inadvertently. Using secure methods to manage and monitor applications is crucial to avoid vulnerabilities like XSS and privilege escalation.

7. **Fail-safes and Error Handling**: Implement fail-safes for downloading information from URLs and consider directly invoking necessary commands rather than using workarounds.

## Data and Configuration

I have censored the app's sensitive data, configuration, and remote configuration load URL to prevent abuse. However, I acknowledge that those with sufficient knowledge can still potentially uncover this information.

## Entry Point

The entry point for the code is `launcher.py`.

Feel free to explore the source code and understand how the Python packages work. I only decompiled the launcher as it's the main component. You can decompile other parts yourself if needed. This repository is here for you to learn from and enjoy.