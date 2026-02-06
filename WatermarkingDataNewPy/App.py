from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import mysql.connector
from ecies.utils import generate_key
from ecies import encrypt, decrypt
import base64, os, sys

app = Flask(__name__)
app.secret_key = 'a'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ServerLogin')
def ServerLogin():
    return render_template('ServerLogin.html')


@app.route('/OwnerLogin')
def OwnerLogin():
    return render_template('OwnerLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route('/NewOwner')
def NewOwner():
    return render_template('NewOwner.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route('/PKGLogin')
def PKGLogin():
    return render_template('PKGLogin.html')


@app.route("/serverlogin", methods=['GET', 'POST'])
def serverlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'server' and request.form['password'] == 'server':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where status='waiting'")
            data = cur.fetchall()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where status='Active'")
            data1 = cur.fetchall()
            return render_template('ServerHome.html', data=data, data1=data1)

        else:
            flash('Username or Password is wrong')
            return render_template('ServerLogin.html')


@app.route("/ServerHome")
def ServerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='Active'")
    data1 = cur.fetchall()
    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/SUserInfo")
def SUserInfo():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()

    return render_template('SUserInfo.html', data=data,data1=data1)


@app.route("/Approved11")
def Approved11():
    id = request.args.get('lid')
    email = request.args.get('email')
    import random
    loginkey = random.randint(1111, 9999)
    message = "User Login Key :" + str(loginkey)

    sendmail(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("Update regtb set Status='Active',LoginKey='" + str(loginkey) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()

    return render_template('SUserInfo.html', data=data, data1=data1)


@app.route("/Reject11")
def Reject11():
    id = request.args.get('lid')
    email = request.args.get('email')

    message = "Your Request  Rejected"

    sendmail(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("Update regtb set Status='reject' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status !='waiting'")
    data1 = cur.fetchall()

    return render_template('SUserInfo.html', data=data, data1=data1)




@app.route('/SFileInfo')
def SFileInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb ")
    data1 = cur.fetchall()
    return render_template('SFileInfo.html', data=data1)


@app.route('/SRequestInfo')
def SRequestInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb ")
    data1 = cur.fetchall()
    return render_template('SRequestInfo.html', data=data1)



@app.route("/Approved")
def Approved():
    id = request.args.get('lid')
    email = request.args.get('email')
    import random
    loginkey = random.randint(1111, 9999)
    message = "Owner Login Key :" + str(loginkey)

    sendmail(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("Update ownertb set Status='Active',LoginKey='" + str(loginkey) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='Active'")
    data1 = cur.fetchall()

    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/Reject")
def Reject():
    id = request.args.get('lid')
    email = request.args.get('email')

    message = "Your Request  Rejected"

    sendmail(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("Update ownertb set Status='reject' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status !='waiting'")
    data1 = cur.fetchall()

    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/newowner", methods=['GET', 'POST'])
def newowner():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO ownertb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','waiting','')")
            conn.commit()
            conn.close()

            flash('Record Saved!')
            return render_template('NewOwner.html')
        else:
            flash('Already Register This  UserName!')
            return render_template('NewOwner.html')


@app.route("/ownerlogin", methods=['GET', 'POST'])
def ownerlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        loginkey = request.form['loginkey']
        session['oname'] = request.form['uname']
        session['lk'] = loginkey

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('OwnerLogin.html')

        else:

            Status = data[7]
            lkey = data[8]
            print(lkey)

            if Status == "waiting":

                flash('Waiting For Server Approved!')
                return render_template('OwnerLogin.html')

            else:

                if lkey == loginkey:

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1watermarkdata')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM ownertb where username='" + session['oname'] + "'")
                    data1 = cur.fetchall()
                    return render_template('OwnerHome.html', data=data1)
                else:
                    flash('Login Key Incorrect')
                    return render_template('OwnerLogin.html')


@app.route('/OwnerHome')
def OwnerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where username='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('OwnerHome.html', data=data1)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "'  ")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" +
                username + "','" + password + "','waiting','')")
            conn.commit()
            conn.close()


            flash('Record Saved!')
            return render_template('NewUser.html')
        else:
            flash('Already Register This  UserName!')
            return render_template('NewUser.html')


@app.route('/OwnerFileUpload')
def OwnerFileUpload():
    return render_template('OwnerFileUpload.html', oname=session['oname'])


import hmac
import hashlib
import binascii


def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()


@app.route("/owfileupload", methods=['GET', 'POST'])
def owfileupload():
    if request.method == 'POST':
        oname = session['oname']
        info = request.form['info']
        file = request.files['file']
        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename

        file.save("static/upload/" + savename)

        secp_k = generate_key()
        privhex = secp_k.to_hex()
        pubhex = secp_k.public_key.format(True).hex()

        filepath = "./static/upload/" + savename
        head, tail = os.path.split(filepath)

        newfilepath1 = './static/Encrypt/' + str(tail)
        newfilepath2 = './static/Decrypt/' + str(tail)

        data = 0
        with open(filepath, "rb") as File:
            data = base64.b64encode(File.read())  # convert binary to string data to read file

        print("Private_key:", privhex, "\nPublic_key:", pubhex, "Type: ", type(privhex))

        if privhex == 'null':
            flash('Please Choose Another File,file corrupted!')
            return render_template('OwnerFileUpload.html')

        else:
            print("Binary of the file:", data)
            encrypted_secp = encrypt(pubhex, data)
            print("Encrypted binary:", encrypted_secp)

            with open(newfilepath1, "wb") as EFile:
                EFile.write(base64.b64encode(encrypted_secp))

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM filetb ")
            data2 = cursor.fetchone()

            if data2:

                conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
                cursor1 = conn1.cursor()
                cursor1.execute("select max(id) from filetb")
                da = cursor1.fetchone()
                if da:
                    d = da[0]
                    print(d)

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
                cursor = conn.cursor()
                cursor.execute("SELECT  *  FROM filetb where  id ='" + str(d) + "'   ")
                data1 = cursor.fetchone()
                if data1:
                    hash1 = data1[7]
                    num1 = random.randrange(1111, 9999)
                    hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1watermarkdata')
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO filetb VALUES ('','" + oname + "','" + info + "','" + savename + "','" + pubhex + "','" + privhex + "','" +
                        hash1 + "','" + hash2 + "')")
                    conn.commit()
                    conn.close()
                    flash('File Upload And Encrypt Successfully ')
                    return render_template('OwnerFileUpload.html', pkey=privhex, oname=oname)

            else:

                hash1 = '0'
                num1 = random.randrange(1111, 9999)
                hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO filetb VALUES ('','" + oname + "','" + info + "','" + savename + "','" + pubhex + "','" + privhex + "','" + hash1 + "','" + hash2 + "')")
                conn.commit()
                conn.close()
                flash('File Upload And Encrypt Successfully ')
                return render_template('OwnerFileUpload.html', pkey=privhex, oname=oname)


@app.route("/owfileupload1", methods=['GET', 'POST'])
def owfileupload1():
    if request.method == 'POST':
        info = request.form['info']
        file = request.files['file']
        print(file)

        if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            print('pass')

            return render_template('OwnerFileUpload.html')
        else:

            return "Invalid file type. Only images are allowed.", 400






@app.route('/OwnerFileInfo')
def OwnerFileInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where OwnerName='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('OwnerFileInfo.html', data=data1)


@app.route("/ODownload")
def ODownload():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:
        prkey = data[5]
        fname = data[3]

    else:
        return 'Incorrect username / password !'

    privhex = prkey

    filepath = "./static/Encrypt/" + fname
    head, tail = os.path.split(filepath)

    newfilepath1 = './static/Encrypt/' + str(tail)
    newfilepath2 = './static/Decrypt/' + str(tail)

    data = 0
    with open(newfilepath1, "rb") as File:
        data = base64.b64decode(File.read())

    print(data)
    decrypted_secp = decrypt(privhex, data)
    print("\nDecrypted:", decrypted_secp)
    with open(newfilepath2, "wb") as DFile:
        DFile.write(base64.b64decode(decrypted_secp))

    return send_file(newfilepath2, as_attachment=True)


@app.route("/OwnerFileApproved")
def OwnerFileApproved():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and OwnerName='" + session['oname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and OwnerName='" + session['oname'] + "' ")
    data1 = cur.fetchall()
    return render_template('OwnerFileApproved.html', data=data, data1=data1)


@app.route("/OApproved")
def OApproved():
    rid = request.args.get('rid')
    fid = request.args.get('fid')

    session["fid"] = fid
    session["rid"] = rid

    return render_template('Hide.html')


@app.route("/hide", methods=['GET', 'POST'])
def hide():
    if request.method == 'POST':
        from cryptography.fernet import Fernet
        import random
        from stegano import lsb

        Unhidekey = request.form['hkey']

        file = request.files['file']
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  userfiletb where  id='" + session["rid"] + "'")
        data = cursor.fetchone()
        if data:
            prkey = data[4]
            UserName = data[5]
        else:
            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  regtb where  UserName='" + UserName + "'")
        data1 = cursor.fetchone()
        if data1:
            session["email"] = data1[3]
            llkey = data1[8]
        else:
            return 'Incorrect username / password !'

        # key encrypt
        message = llkey + ',' + prkey

        key = Fernet.generate_key()

        Decryptkey = key.decode()

        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode())

        print("original string: ", message)
        print("encrypted string: ", encMessage)

        secret = lsb.hide("./static/upload/" + savename, encMessage.decode())

        pathname, extension = os.path.splitext("./static/upload/" + savename)
        filename = pathname.split('/')

        imageName = filename[-1] + ".png"

        secret.save("./static/Encode/" + imageName)

        secp_k = generate_key()
        privhex = secp_k.to_hex()
        pubhex = secp_k.public_key.format(True).hex()

        # Read the file path of the selected file

        filepath = "./static/Encode/" + imageName
        head, tail = os.path.split(filepath)

        newfilepath1 = './static/Encrypt/' + str(tail)
        # newfilepath2 = './static/Decrypt/' + str(tail)

        data = 0
        with open(filepath, "rb") as File:
            data = base64.b64encode(File.read())  # convert binary to string data to read file

        print("Private_key:", privhex, "\nPublic_key:", pubhex, "Type: ", type(privhex))
        # print("Binary of the file:", data)
        encrypted_secp = encrypt(pubhex, data)
        # print("Encrypted binary:", encrypted_secp)

        with open(newfilepath1, "wb") as EFile:
            EFile.write(base64.b64encode(encrypted_secp))

        imagedkey = privhex

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("update userfiletb set Status='Approved' ,ImageName='" + imageName + "',Imagedkey='" + str(
            imagedkey) + "',Unhidekey='" + str(Unhidekey) + "', Decryptkey='" + str(Decryptkey) + "' where id='" +
                       session["rid"] + "'")
        conn.commit()
        conn.close()

        mailmsg = "Request Id" + session[
            "rid"] + "\nimage decrypt key:" + imagedkey + "\nUnhidekey:" + Unhidekey + "\nDecryptkey: " + Decryptkey

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        fromaddr = "projectmailm@gmail.com"
        toaddr = session["email"]

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Cloud Security"

        # string to store the body of the mail
        body = mailmsg

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = imageName
        attachment = open("./static/Encrypt/" + imageName, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, "qmgn xecl bkqv musr")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()

        flash('key Hide and encrypt to Send to User')
        return OwnerFileApproved()


@app.route("/UDownload")
def UDownload():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and Username='" + session['uname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and Username='" + session['uname'] + "' ")
    data1 = cur.fetchall()
    return render_template('UDownload.html', data=data, data1=data1)


@app.route("/userdownload")
def userdownload():
    ufid = request.args.get('ufid')

    session["ufid"] = ufid

    return render_template('UnHide.html')


@app.route("/unhide", methods=['GET', 'POST'])
def unhide():
    if request.method == 'POST':
        from cryptography.fernet import Fernet
        import random
        from stegano import lsb

        idk = request.form['idk']
        uhk = request.form['uhk']
        dfk = request.form['dfk']

        file = request.files['file']

        file.save("static/Uupload/" + file.filename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "' and  Imagedkey='" + idk + "'")
        data = cursor.fetchone()
        if data:

            privhex = idk

            filepath = "./static/Uupload/" + file.filename
            head, tail = os.path.split(filepath)

            newfilepath1 = './static/Uupload/' + str(tail)
            newfilepath2 = './static/Decode/' + str(tail)

            data = 0
            with open(newfilepath1, "rb") as File:
                data = base64.b64decode(File.read())

            print(data)
            decrypted_secp = decrypt(privhex, data)
            print("\nDecrypted:", decrypted_secp)
            with open(newfilepath2, "wb") as DFile:
                DFile.write(base64.b64decode(decrypted_secp))

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
            cursor = conn.cursor()
            cursor.execute(
                "SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "' and  Unhidekey='" + uhk + "'")
            data = cursor.fetchone()
            if data:

                clear_message = lsb.reveal(newfilepath2)
                print(clear_message)

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "' and  Decryptkey='" + dfk + "'")
                data = cursor.fetchone()
                if data:
                    fname = data[3]

                    key = dfk.encode()
                    print(key)
                    fernet = Fernet(key)

                    encMessage = clear_message.encode()
                    decMessage = fernet.decrypt(encMessage).decode()
                    print("decrypted string: ", decMessage)

                    splitted_string = decMessage.split(',')

                    # Iterate through each substring
                    print(splitted_string[0])
                    print(splitted_string[1])

                    if splitted_string[0] == session['lkey']:
                        privhex = splitted_string[1]

                        filepath = "./static/Encrypt/" + fname
                        head, tail = os.path.split(filepath)

                        newfilepath1 = './static/Encrypt/' + str(tail)
                        newfilepath2 = './static/Decrypt/' + str(tail)

                        data = 0
                        with open(newfilepath1, "rb") as File:
                            data = base64.b64decode(File.read())

                        print(data)
                        decrypted_secp = decrypt(privhex, data)
                        print("\nDecrypted:", decrypted_secp)
                        with open(newfilepath2, "wb") as DFile:
                            DFile.write(base64.b64decode(decrypted_secp))

                        return send_file(newfilepath2, as_attachment=True)
                    else:
                        alert = 'User  key Incorrect!'
                        return render_template('goback.html', data=alert)


                else:
                    alert = 'Decrypt file key Incorrect!'
                    return render_template('goback.html', data=alert)

            else:
                alert = 'Image unhide key Incorrect!'
                return render_template('goback.html', data=alert)


        else:
            alert = 'Image decrypt key Incorrect!'
            return render_template('goback.html', data=alert)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        loginkey = request.form['loginkey']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')

        else:

            Status = data[7]
            lkey = data[8]
            session['lkey'] = data[8]

            if Status == "waiting":

                flash('Waiting For Server Approved!')
                return render_template('UserLogin.html')

            else:

                if lkey == loginkey:
                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1watermarkdata')

                    cur = conn.cursor()
                    cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
                    data1 = cur.fetchall()
                    flash('Login Successfully')
                    return render_template('UserHome.html', data=data1)


                else:
                    flash('Login Key Incorrect')
                    return render_template('UserLogin.html')


def loginvales1():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM regtb where username='" + uname + "'")
    data = cursor.fetchone()

    if data:
        Email = data[3]
        Phone = data[2]


    else:
        return 'Incorrect username / password !'

    return uname, Email, Phone


@app.route("/facelogin")
def facelogin():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("SELECT * from temptb where username='" + uname + "' ")
    data = cursor.fetchone()
    if data is None:

        alert = 'Face  is wrong'
        return render_template('goback.html', data=alert)


    else:

        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='1watermarkdata')
        cur = conn.cursor()
        cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
        data1 = cur.fetchall()
        flash('Login Successfully')
        return render_template('UserHome.html', data=data1)


@app.route('/UserHome')
def UserHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserHome where OwnerName='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('UserHome.html', data=data1)


@app.route('/USearch')
def USearch():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb ")
    data1 = cur.fetchall()
    return render_template('USearch.html', data=data1)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        sear = request.form['sear']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM filetb where ownername like'%" + sear + "%' or FileInfo like'%" + sear + "%' or FileName like '%" + sear + "%' ")
        data1 = cur.fetchall()
        return render_template('USearch.html', data=data1)


@app.route("/SendKeyRequest")
def SendKeyRequest():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        oname = data[1]
        fname = data[3]
        prkey = data[5]

    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO userfiletb VALUES ('','" + fid + "','" + oname + "','" + fname + "','" + prkey + "','" + session[
            'uname'] + "','waiting','','','','')")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and username='" + session['uname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1watermarkdata')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and username='" + session['uname'] + "' ")
    data1 = cur.fetchall()
    return render_template('UDownload.html', data=data, data1=data1)


def sendmail(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qmgn xecl bkqv musr")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True, port=5000)
    app.run(debug=True, use_reloader=True)
