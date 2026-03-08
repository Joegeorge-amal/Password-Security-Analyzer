# Password Security Analyzer

A simple Python tool that analyzes password strength.  
It checks password length, character types, entropy, and whether the password appears in known data breaches.

## How to run

Install dependencies:

pip install requests zxcvbn

Run the program:

python main.py

## What it does

- Checks password length and character types
- Calculates password entropy
- Estimates strength using zxcvbn
- Checks if the password appears in known breaches
