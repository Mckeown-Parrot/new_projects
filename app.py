from flask import Flask
from dotenv import load_dotenv
import os
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER']=str(os.getenv('MAIL_SERVER'))
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
app.config['MAIL_USE_TLS'] = bool(os.getenv('MAIL_USE_TLS'))
app.config['MAIL_USE_SSL'] = bool(os.getenv('MAIL_USE_SSL'))

mail = Mail(app)
@app.route("/mail")
def send_mail():
    message = Message(subject='BUTTON EVENT', 
                      recipients=['jameskwaku2020@outlook.com'], 
                      body='Programming with  rasberrypi', 
                      sender='jamesmckeown847@gmail.com'
                      )
    message.body = "l pushed a button"

    try:
        mail.send(message)
        return "Successful"
    except:
        return "failed"

    return "mail"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4545)

