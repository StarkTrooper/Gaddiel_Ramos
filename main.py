from flask import Flask, render_template, request, send_from_directory
import smtplib

app = Flask(__name__)
OWN_EMAIL = "yoyuyu16@gmail.com"
OWN_PASSWORD = "poiuy09876"


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message \n\nName: {name}\nEmail: {email}\n Phone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route('/download')
def download():
    return send_from_directory(directory="static/files", path="Resume_Gaddiel_Ramos.pdf", as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
