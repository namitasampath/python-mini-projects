from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials (from your Twilio Console)
account_sid = 'ACxxxxxxxxxxxxxxxxxxxx'
auth_token = 'your_auth_token'
verify_sid = 'VAxxxxxxxxxxxxxxxxxxxx'

client = Client(account_sid, auth_token)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-otp', methods=['POST'])
def send_otp():
    phone = request.form['phone']
    client.verify.v2.services(verify_sid).verifications.create(
        to=phone, channel='sms'
    )
    return render_template('verify.html', phone=phone)

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    phone = request.form['phone']
    otp = request.form['otp']
    result = client.verify.v2.services(verify_sid).verification_checks.create(
        to=phone, code=otp
    )
    if result.status == "approved":
        return "<h2>✅ Phone number verified successfully!</h2>"
    else:
        return "<h2>❌ Verification failed. Please try again.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
