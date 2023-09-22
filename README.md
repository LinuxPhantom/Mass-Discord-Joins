# Mass Discord Joins 🔄

![MDJ](Main.gif)

A utility built for educational purposes, the Discord Account Switcher allows automated switching and logging into multiple Discord accounts to join servers via invite links.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation & Usage](#installation--usage)
- [Issues & Contributions](#issues--contributions)
- [License](#license)
- [Support the Project](#support-the-project)

## About
This Python script leverages the power of `tkinter` for its GUI and `selenium` for web automation to switch between multiple Discord accounts and join servers.

**Note**: This tool is purely for educational purposes. Ensure you have the right to access any information or automate any processes before proceeding.

## Features
- Store multiple Discord account credentials.
- Easy GUI for adding/removing accounts.
- Automated browser control to log into accounts and join servers.
- All credentials are stored locally.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed.
- Google Chrome browser installed.
- ChromeDriver compatible with your Chrome version (needed for Selenium).

## Installation & Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YourGitHubUsername/DiscordAccountSwitcher.git
    cd DiscordAccountSwitcher
    ```

2. **Set up a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the script**:
    ```bash
    python main.py
    ```

5. **Usage**:
    - Enter your Discord account's email and password, then click "Add Account" to store the account.
    - Enter a Discord invite link and click "Submit" to join the server with all stored accounts.

## Issues & Contributions
- If you encounter any issues or want to suggest improvements, please [open an issue](https://github.com/LinuxPhantom/Mass-Discord-Joins/issues).
- Feel free to fork this repository and contribute. Pull requests are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support the Project
If you find this project helpful or learned something from the source code orrrr want updates, please consider giving it a 🌟 on GitHub!

