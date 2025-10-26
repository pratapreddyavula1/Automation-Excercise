import logging
import os

# Ensure Logs directory exists
logs_dir = os.path.join(os.getcwd(), "Logs")
os.makedirs(logs_dir, exist_ok=True)

# File path
log_file = os.path.join(logs_dir, "automation.log")

# Create logger
logger = logging.getLogger("AutomationLogger")
logger.setLevel(logging.DEBUG)  # Capture all levels: DEBUG, INFO, WARNING, ERROR

# Formatter
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

# File Handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
