import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def send_email(self, to_email, subject, message):
        from_email = "your_email@example.com"
        password = "your_email_password"
        
        try:
            server = smtplib.SMTP("smtp.example.com", 587)
            server.starttls()
            server.login(from_email, password)
            
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))
            
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            
            return "Email sent successfully."
        except Exception as e:
            return "An error occurred while sending the email."

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "set a reminder" in user_input:
            # Implement reminder setting logic here
            reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
            print(f"Kiwi: Reminder set for {reminder_time}.")
        elif "make an appointment" in user_input:
            # Implement appointment scheduling logic here
            print("Kiwi: Appointment scheduled.")
        elif "send an email" in user_input:
            to_email = input("Enter recipient's email address: ")
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")
            email_response = kiwi.send_email(to_email, subject, message)
            print(f"Kiwi: {email_response}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
