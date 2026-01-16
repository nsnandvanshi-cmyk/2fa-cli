#!/usr/bin/env bash

set -e

echo "[+] Detecting package manager..."

if command -v apt >/dev/null; then
  sudo apt update
  sudo apt install -y python3 python3-pip python3-venv \
    build-essential libssl-dev libffi-dev rustc cargo
elif command -v pacman >/dev/null; then
  sudo pacman -Sy --noconfirm python python-pip rust
elif command -v dnf >/dev/null; then
  sudo dnf install -y python3 python3-pip openssl-devel libffi-devel rust cargo
else
  echo "Unsupported distro"
  exit 1
fi

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
