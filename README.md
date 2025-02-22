# AWS-IAM-USER-PROJECT
# AWS IAM User Management Project  

This project simplifies the process of creating IAM users, generating login credentials, and attaching AWS policies using Python and Boto3.  

## Features  
- Creates IAM Users (With a prefix to avoid naming conflicts)  
- Generates a secure random password (Meeting AWS password policy)  
- Attaches AWS Policies based on user selection  
- Checks if a user already exists before creating one  

## Prerequisites  
Before running the script, ensure you have:  
- AWS CLI configured (`aws configure`)  
- Python installed (Recommended: Python 3.9+)  
- Boto3 installed (`pip install boto3`)  
- IAM permissions to create users and attach policies  

## Setup & Usage  
### 1. Clone the Repository  
```bash
git clone https://github.com/Extraordinarytechy/AWS-IAM-USER-PROJECT.git
cd AWS-IAM-USER-PROJECT
```

### 2. Install Dependencies  
```bash
pip install -r requirements.txt
```
(If `requirements.txt` is missing, just install `boto3` manually: `pip install boto3`)  

### 3. Run the Script  
```bash
python iam_project.py
```

### 4. Follow the Prompts  
- Enter the IAM username  
- Select policy numbers (comma-separated)  
- The script will create the user (if not already present) and display login credentials  

### 5. IAM User Details Output  
Once successful, you’ll see:  
- IAM User Created  
- Temporary Password Generated  
- AWS Console Login URL  
- Policies Attached  

## GitHub Workflow (How We Pushed It)  
If you want to push your updates to GitHub, follow these steps:  

### 1. Initialize Git (Only if Not Initialized)  
```bash
git init
```

### 2. Add & Commit Your Changes  
```bash
git add .
git commit -m "Initial commit - IAM user project"
```

### 3. Push to GitHub  
If pushing for the first time:  
```bash
git branch -M main
git remote add origin https://github.com/Extraordinarytechy/AWS-IAM-USER-PROJECT.git
git push -u origin main
```

If you get a push rejection error, use:  
```bash
git fetch origin
git rebase origin/main
git push origin main --force
```

---

## Next Steps 
- Improve error handling  
- Add logging for tracking IAM user creation  
- Implement a UI for user-friendly interaction  

Feel free to contribute or raise issues! Happy coding!  
