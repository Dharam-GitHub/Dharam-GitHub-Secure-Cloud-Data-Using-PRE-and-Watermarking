# Secure Cloud File Sharing with Watermarking & Proxy Re-Encryption

## 🚀 Overview
A high-security Full-Stack cloud platform designed for confidential file sharing. Unlike traditional cloud storage, this project implements **Zero-Knowledge** principles, ensuring that even the cloud provider cannot access user data.

The project integrates **Computer Vision (Steganography)** for ownership verification and **Advanced Cryptography** for secure data delegation.

## 🛠️ Technical Stack
- **Backend:** Python, Flask
- **Database:** MySQL (Relational data management)
- **Security:** ECIES (Elliptic Curve Integrated Encryption Scheme), AES, RSA
- **Advanced Crypto:** PyUmbral (Proxy Re-Encryption)
- **Computer Vision:** OpenCV & Pillow (LSB Watermarking)

## ✨ Key Features

### 1. Proxy Re-Encryption (PRE)
Implemented using the **PyUmbral** library. This allows a file owner to delegate access to another user without decrypting the file or sharing private keys. The server transforms the ciphertext directly, ensuring end-to-end privacy.

### 2. Invisible Digital Watermarking
Uses **LSB (Least Significant Bit) Steganography**. A unique identifier is embedded into the pixels of image files. This watermark is invisible to the human eye but can be extracted to prove ownership if the data is leaked.

### 3. Role-Based Access Control (RBAC)
A secure authentication system for three distinct roles:
- **Owner:** Can upload, watermark, and delegate access.
- **User:** Can request access and decrypt shared files.
- **Admin:** Manages system logs and user permissions.

### 4. Hybrid Encryption
Uses **AES** for fast bulk data encryption and **ECIES/RSA** for secure key exchange, balancing performance with top-tier security.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Dharam-GitHub/Dharam-GitHub-Secure-Cloud-Data-Using-PRE-and-Watermarking.git](https://github.com/Dharam-GitHub/Dharam-GitHub-Secure-Cloud-Data-Using-PRE-and-Watermarking.git)
   cd Dharam-GitHub-Secure-Cloud-Data-Using-PRE-and-Watermarking

2. **Install Dependencies:**

pip install -r requirements.txt

3. **Database Configuration:**

-Ensure your MySQL server is running.

-Update the database credentials in app.py.

4. **Run the Application:**

python app.py