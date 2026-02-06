import sqlite3

# Database file path
DB_PATH = 'watermarkdata.db'

def insert_data():
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        # Insert data into filetb
        cur.execute('''
            INSERT INTO filetb (id, OwnerName, FileInfo, FileName, pubkey, privkey, hash1, hash2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            1,
            'san',
            'my image',
            '65576.jpg',
            '03c92a8fe803acc2447c4782066231b4113fb856125c03398bb451ef0d2e36d758',
            '9aa81e5ffec3630caa94d190076705d9ae43d40f24b1671b24364c6fe58ed7a8',
            '0',
            '5C317E9BABDAE103B8718A301C28D1371358235A8F32B926E00888AE7666834B'
        ))

        # Insert data into ownertb
        cur.execute('''
            INSERT INTO ownertb (id, uname, mobile, email, address, username, password, status, LoginKey)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            1,
            'sangeeth Kumar',
            '9486365535',
            'sangeeth5535@gmail.com',
            'No 16, Samnath Plaza, Madurai Main Road, Melapudhur',
            'san',
            'san',
            'Active',
            '5922'
        ))

        # Insert data into regtb
        cur.execute('''
            INSERT INTO regtb (id, uname, mobile, email, address, username, password, status, LoginKey)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            1,
            'sangeeth Kumar',
            '9486365535',
            'sangeeth5535@gmail.com',
            'No 16, Samnath Plaza, Madurai Main Road, Melapudhur',
            'san',
            'san',
            'Active',
            '7435'
        ))

        # Insert data into userfiletb
        cur.execute('''
            INSERT INTO userfiletb (id, fid, OwnerName, FileName, prkey, Username, status, ImageName, Imagedkey, Unhidekey, Decryptkey)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            1,
            '1',
            'san',
            '65576.jpg',
            '9aa81e5ffec3630caa94d190076705d9ae43d40f24b1671b24364c6fe58ed7a8',
            'san',
            'Approved',
            '253gg3.png',
            '975d76762e5c362b39ed62eddbc3ea11eee553d0c5647e76aeff526117e22245',
            '123',
            'VE9WXMrc8d9SkRGvsRiXO0VB9yfjTzyGP4pV1e7JN4c='
        ))

        # Commit changes
        conn.commit()
        print("Data inserted successfully into all tables.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()

if __name__ == '__main__':
    insert_data()