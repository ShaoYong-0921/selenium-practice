def send_email(from_email, password, to_email):

    import email.message
    import smtplib

    msg = email.message.EmailMessage()
    msg['From'] = from_email
    msg['To'] = to_email
    msg["Subject"] = "測試"
    msg.set_content('測試自動郵件，收到請幫忙回報<3')

    smtpssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtpssl.ehlo()
    smtpssl.login(from_email, password)
    smtpssl.send_message(msg)
    print("Send Email Complete!")

    return
