# Requirements to use this program
# The csv file with the contacts should be in the same folder as the main project
# Password for the mail server/mail id is required

import smtplib
import ssl
import csv

port = 465  # for ssl
password = input("Enter password here")

# creating secure ssl context
context = ssl.create_default_context()

with open("contacts_list.csv") as file:
    reader = csv.reader(file)
    # defining our values

    sender = "lavish.dudeja@nic.in"
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase

    next(reader)  # skip header row
    for name, email in reader: # this reads the name and email in the csv file and loops until all of them are read
        print(f"Sending email to: {name}") # fstring to auto-substitute name according to csv file
        with smtplib.SMTP_SSL("smtp.mail.gov.in", port, context=context) as server: # log-in for the email
            server.login("lavish.dudeja@nic.in", password)

            # This section is to edit the header information
            msg = MIMEMultipart() # breaks message into component parts of header and the body
            msg['From'] = 'lavish.dudeja@nic.in'
            msg['To'] = email
            msg['Subject'] = 'Image Test'

# now we use a html syntax to format the file as we require and make changes as we need
            html1=""" 
            <html>	
	<head>
	<style>
button {
 background-color:#bc451b; 
 width:18%;
 height:80px;
 position:absolute;
 left:70%;
 top:70%;
 font-size:22px;
 border-radius:8px;
 border:2px solid #ccffff;
 transition-duration: 0.4s;
} 	
button:hover {
 background-color: #cc9900;
 color: white;
 border: 2px solid #000099; 
}
</style>
	</head>
	<body>
<p>दिनांक 16 मार्च 2021 को शिक्षा मंत्रालय की अनुदान माँगों पर लोक सभा में अपना वक्तव्य रखा । सभी माननीय सदस्यों का आभारी हूँ जिन्होंने शिक्षा के विषय पर पूर्ण सक्रियता एवं मनोयोग के साथ सहभागिता करते हुए अनुदान मांगो को पारित करवाने में सहयोग प्रदान किया |</p>
        </body>
</html>
            """
            part1= (MIMEText(html1, 'html')) # in a variable part1, stores the contents of var html1 in html format

            msg.attach(part1) # attaches the contents of part1/html1 to our message

            text = msg.as_string() # converts msg to a string format
            server.sendmail(sender, email, text) # sends email

#server.quit()
