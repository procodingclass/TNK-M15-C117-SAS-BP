import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSenderApp():
    def __init__(self):
        super().__init__()

    def send_single_email(self):
        sender_email = input("Enter Sender Email\n")
        sender_password = input("Enter Sender Password\n")
        # Accept comma seprated values as recipient email and remove the white spaces
        # Change variable name to recipients_email
        recipient_email = input("Enter Recipient Email\n")
        subject = input("Enter Email Subject\n")
        message_body = input("Enter Message\n")
        # Split the recipient email values by comma



        # Write for loop to send email to multiple recipients


       
    
        try:
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(message_body, "plain"))

            smtp_server.sendmail(sender_email, recipient_email, message.as_string())
            smtp_server.quit()
            print("Email Sent", "Email sent successfully!")

        except Exception as e:
            print("Error", f"An error occurred: {str(e)}")


def main():
    app = EmailSenderApp()
    app.send_single_email()

if __name__ == "__main__":
    main()
