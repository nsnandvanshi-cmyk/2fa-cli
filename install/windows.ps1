Write-Host "[+] Checking Python..."

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python not found. Install from https://python.org"
    exit 1
}

Write-Host "[+] Upgrading pip tools..."
python -m pip install --upgrade pip setuptools wheel

Write-Host "[+] Installing Python dependencies..."
pip install `
  pyotp `
  cryptography `
  argon2-cffi `
  pyperclip

Write-Host "[+] Installing 2fa-cli..."
pip install .

Write-Host "[✓] Installation complete"
Write-Host "Run with: 2fa"
