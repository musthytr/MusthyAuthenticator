# MusthyAuthenticator

A modern PC version of Google Authenticator built with Python and CustomTkinter.

## Features

- Generate TOTP codes for your accounts
- Add and remove accounts manually
- Modern dark UI with CustomTkinter
- Real-time code updates with countdown
- Secure storage of accounts in JSON

## Installation

1. Install Python 3.7+
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python MusthyAuthenticator.py
   ```

## Creating Executable

To create a standalone executable (no Python required):
```
pip install pyinstaller
pyinstaller --onefile --windowed MusthyAuthenticator.py
```
The executable will be in the `dist/` folder as `MusthyAuthenticator.exe`

## Usage

- Click "Add Account" to add a new account with name and secret key
- Codes update automatically every second
- Red color indicates code is about to expire (<5 seconds)
- Click the "Sil" button next to each account to delete it
- Alternatively, use "Remove Account" button and enter the index (0-based)

## Security Note

Store your accounts.json file securely. It contains sensitive information.