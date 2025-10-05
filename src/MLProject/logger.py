# logger.py
import logging
import os
from datetime import datetime

# 1️⃣ Create logs directory (if it doesn't exist)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# 2️⃣ Define a unique log file name
log_filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"


# 3️⃣ Full path to the log file
log_filepath = os.path.join(logs_dir, log_filename)

# 4️⃣ Configure logging
logging.basicConfig(
    filename=log_filepath,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)