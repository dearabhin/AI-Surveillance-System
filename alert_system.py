import smtplib

def send_alert():
    sender_email = "your_email@example.com"
    receiver_email = "receiver@example.com"
    password = "your_password"

    message = """\
    Subject: Beach Alert

    A person has crossed the danger zone on the beach."""

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Alert email sent!")
    except Exception as e:
        print(f"Error sending alert: {e}")
