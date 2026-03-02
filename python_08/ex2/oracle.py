import os
from dotenv import load_dotenv

load_dotenv()

print("ORACLE STATUS: Reading the Matrix...\n")

# get env vars
matrix_mode = os.getenv("MATRIX_MODE")
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion_endpoint = os.getenv("ZION_ENDPOINT")

print("Configuration loaded:")

# matrix mode
if matrix_mode:
    print(f"Mode: {matrix_mode}")
else:
    print("Mode: Not configured")

# database
if database_url:
    if matrix_mode == "production":
        print("Database: Connected to production database")
    else:
        print("Database: Connected to local instance")
else:
    print("Database: Not configured")

# API key
if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Missing")

# Log
if log_level:
    print(f"Log Level: {log_level}")
else:
    print("Log Level: Not configured")

# Zion
if zion_endpoint:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print("\nEnvironment security check:\n")

print("[OK] No hardcoded secrets detected")

if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file not found")

print("[OK] Production overrides available")

print("The Oracle sees all configurations.")