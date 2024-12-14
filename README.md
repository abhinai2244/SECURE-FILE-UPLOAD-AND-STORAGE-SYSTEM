# Secure File Upload and Storage System

## Project Overview
The Secure File Upload and Storage System is designed to securely upload and store small text and image files in a database. The system uses encryption techniques to protect the confidentiality of the files and implements user management and access control features.

This project leverages object-oriented programming (OOP) concepts in **Python** (or **C++**) to build a secure, user-friendly file management system. It uses strong encryption algorithms like **AES-256** for file encryption and ensures that user passwords are stored securely using one-way hashing functions.

## Features

### 1. **User Management**
   - User registration and profile management.
   - Secure password hashing using **bcrypt** with a random salt for authentication.

### 2. **File Upload**
   - Users can upload small text (.txt) and image (.jpg, .png) files to the system.
   - A user-friendly interface for file selection and upload progress tracking.

### 3. **Encryption**
   - **Client-side encryption** using **AES-256** to protect file content.
   - Users can choose a password or passphrase to encrypt the file before uploading.
   - Encrypted file content is stored securely in the database.

### 4. **Secure Password Storage**
   - Passwords are hashed using **bcrypt** with a random salt, ensuring they are never stored in plain text.

### 5. **Access Control**
   - Basic access control mechanisms, allowing users to define who can view their uploaded files.
   - Role-based access control (RBAC) can be implemented for more granular access permissions (optional).

### 6. **Database Design**
   - **Users Table**: Stores user details (ID, username, email, hashed password, and optional details).
   - **Files Table**: Stores file information (ID, filename, upload date, owner ID, encrypted file content, and access control).

### 7. **Object-Oriented Programming**
   - The system is designed using OOP principles to create well-defined classes for users, files, encryption, and access control.
   - The OOP structure ensures modularity, maintainability, and scalability of the system.

## Technology Stack
- **Programming Language**: Python (or C++)
- **Database**: Relational database (e.g., SQLite, MySQL, or PostgreSQL)
- **Encryption Algorithm**: AES-256 (Advanced Encryption Standard)
- **Password Hashing**: bcrypt
- **Libraries/Frameworks**: 
  - Python: `cryptography`, `flask`, `bcrypt`, etc.
  - C++: OpenSSL (for AES encryption)

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhinai2244/Secure-File-Upload-and-Storage.git
   cd Secure-File-Upload-and-Storage
