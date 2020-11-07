def sendWarning(content):
    import smtplib
    from email.mime.text import MIMEText
    msg_from=''
    passwd=''                                   
    msg_to=''                                  

    with open("./email_msg.conf") as f:
        msg_from = f.readline();
        passwd = f.readline();
        msg_to = f.readline();
    msg_from = msg_from.strip()
    passwd = passwd.strip()
    msg_to = msg_to.strip()
                                
    subject="自动打卡失败提醒"                                          
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except Exception as e:
        print(str(e))
    finally:
        s.quit()
