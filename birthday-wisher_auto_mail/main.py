import pandas
import smtplib
import datetime as dt

my_email = "anuragkanukuntla443@gmail.com"
password = "bfpq nmeb bbmy mbcv"

data = pandas.read_csv("birthdays.csv")
data = {(row["month"], row["day"]) : row.to_dict() for _, row in data.iterrows()}

now = dt.datetime.now()
if (now.month, now.day) in data:
    with open("./letter_templates/letter_1.txt", "r") as file:
        lines = file.read()
        lines = lines.replace("[NAME]", data[(now.month, now.day)]["name"])
    
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shiva128143@gmail.com",
            msg=f"Subject:Birthday wishes\n\n{lines}"
        )   
    


