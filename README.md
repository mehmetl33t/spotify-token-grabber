<div align="center">

# 🎵 Spotify Web Token Grabber

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-2EAD33.svg?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<p align="center">
  A lightweight, automated Python utility to extract Spotify Web API Bearer tokens directly from your active Google Chrome session using Playwright.
</p>

</div>

---

## ⚡ Features
- 🚀 **Zero Login Friction:** Uses your existing Chrome session / profile so you don't need to re-enter your credentials or deal with 2FA/Captchas.
- 🔍 **Automated Network Interception:** Listens to background Spotify web client network requests and captures valid Bearer authorization tokens on the fly.
- 💻 **Dynamic Path Resolution:** Automatically resolves your Windows user data directory.

## 📦 Installation

```bash
git clone https://github.com/mehmetl33t/spotify-token-grabber.git
cd spotify-token-grabber
pip install -r requirements.txt
playwright install chromium
```

## 🚀 Usage

Make sure you have logged into [Spotify Web](https://open.spotify.com) on Google Chrome at least once, then run:

```bash
python autoTokenGrabber.py
```

The script will launch Chrome, intercept the active authorization header, and print your token directly to the console.

## 🤝 Contributing
Pull requests are welcome! If this script helped you, please consider giving it a ⭐!
