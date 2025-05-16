📱 Anonymous-SMS
A lightweight Python tool to send anonymous SMS messages using the Textbelt API.

⚠️ For educational and ethical use only.

✨ Features
Send SMS messages anonymously.

Clean text-based interface.

Works on Windows, macOS, and Linux.

Fully standalone — no extra dependencies except requests.

🛠 Requirements
Python 3.7+

requests library (install with pip install requests)

Internet connection

🚀 Getting Started
1. Clone or download the script
bash
Copier
Modifier
git clone https://github.com/yourusername/Anonymous-SMS.git
cd Anonymous-SMS
Or just download Anon-sms.py and run it.

2. Install dependencies
bash
Copier
Modifier
pip install requests
3. Run the script
bash
Copier
Modifier
python Anon-sms.py
On first run, you’ll see:

csharp
Copier
Modifier
[1] Send SMS
[2] Exit
Choose option 1, and enter:

The recipient's phone number (with country prefix, e.g., +1234567890)

Your message

The script will send the message via the free Textbelt endpoint.

🌐 Textbelt API Notes
This script uses the free Textbelt endpoint (https://textbelt.com/text) with a default key.

The free key is limited to 1 message per day per IP address.

For unlimited use, get a paid key from Textbelt.

To use a custom API key, modify this line in the script:

python
Copier
Modifier
'key': 'textbelt'
Change 'textbelt' to your paid key.

⚠️ Disclaimer
This tool is provided for educational and ethical testing purposes only.
Do not use for harassment, spam, or illegal activities. Misuse may violate laws in your country.

📄 License
This project is licensed under the MIT License.

