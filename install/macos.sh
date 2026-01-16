#!/usr/bin/env bash

set -e

echo "[+] Checking Homebrew..."
if ! command -v brew >/dev/null; then
  echo "Homebrew not found. Install it from https://brew.sh"
  exit 1
fi

echo "[+] Installing system dependencies..."
brew install python rust openssl libffi

echo "[+] Upgrading pip tools..."
pip3 install --upgrade pip setuptools wheel

echo "[+] Installing Python dependencies..."
pip3 install \
  pyotp \
  cryptography \
  argon2-cffi \
  pyperclip

echo "[+] Installing 2fa-cli..."
pip3 install .

echo "[✓] Installation complete"
echo "Run with: 2fa"
