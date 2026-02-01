# Day 23 – Virtual Environments

## What I Learned
- What a virtual environment is
- Why we use virtual environments in Python
- How to create and activate a venv
- How to install packages inside a venv
- Why venv should NOT be pushed to GitHub

## Commands Used

Create virtual environment:
```bash
python -m venv venv


#Activate (Mac/Linux)
source venv/bin/activate


#Install packages 
pip install flask


#Check installed packages 
pip freeze

#Deactivate 
deactivate
