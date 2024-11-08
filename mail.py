
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'kksupekar371121@kkwagh.edu.in'  
SMTP_PASSWORD = 'Ksupekar@2003'  
EMAIL_FROM = 'vsdhage371121@kkwagh.edu.in'  
EMAIL_TO = 'pdeep665511@gmail.com'  
EMAIL_SUBJECT = 'Object Detected!'


IR_SENSOR_PIN = 7
LED_PIN = 11


GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def send_email():
    try:
        # Create a secure SSL context
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Email content
        message = MIMEMultipart()
        message['From'] = EMAIL_FROM
        message['To'] = EMAIL_TO
        message['Subject'] = EMAIL_SUBJECT
        body = "An object has been detected by the IR sensor."
        message.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())

        # Clean up
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:
            print("Object detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            send_email()  # Send email notification
            time.sleep(1)  # Delay to avoid multiple emails in quick succession
        else:
            print("No object detected.")
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
       
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()
