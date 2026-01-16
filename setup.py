from setuptools import setup, find_packages

setup(
    name="2fa-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyotp",
        "cryptography",
    ],
    entry_points={
        "console_scripts": [
            "2fa=two_fa_cli.cli:main",
        ],
    },
    description="Secure offline 2FA CLI tool",
    author="N.S.Nandvanshi",
    license="MIT",
    python_requires=">=3.8",
)
