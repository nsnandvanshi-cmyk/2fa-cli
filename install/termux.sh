#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "[+] Updating Termux..."
pkg update -y && pkg upgrade -y

echo "[+] Installing system dependencies..."
pkg install -y python rust clang libffi openssl

echo "[+] Upgrading pip tools..."
pip install --upgrade pip setuptools wheel

echo "[+] Installing Python dependencies..."
pip install \
  pyotp \
  cryptography \
  argon2-cffi \
  pyperclip

echo "[+] Installing 2fa-cli..."
pip install .

echo "[✓] Installation complete"
echo "Run with: 2fa"
