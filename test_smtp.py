import smtplib
import os
from email.message import EmailMessage

def test_smtp():
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "aigrievancecitizensystem@gmail.com"
    smtp_pass = "ilfanwjadkffmpak"
    smtp_from = "aigrievancecitizensystem@gmail.com"
    
    print(f"Connecting to {smtp_host}:{smtp_port}...")
    try:
        server = smtplib.SMTP(smtp_host, smtp_port, timeout=15)
        server.set_debuglevel(1)
        print("EHLO 1...")
        server.ehlo()
        print("STARTTLS...")
        server.starttls()
        print("EHLO 2...")
        server.ehlo()
        print("Login...")
        server.login(smtp_user, smtp_pass)
        print("Login successful!")
        
        msg = EmailMessage()
        msg["Subject"] = "SMTP Test"
        msg["From"] = smtp_from
        msg["To"] = smtp_user  # Send to self
        msg.set_content("Connection test successful.")
        
        server.send_message(msg)
        print("Message sent successfully!")
        server.quit()
        return True
    except Exception as e:
        print(f"FAILED: {e}")
        return False

if __name__ == "__main__":
    test_smtp()
