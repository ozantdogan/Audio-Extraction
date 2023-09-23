from settings import(
    log_folder_name
)
import datetime
import logging
import os

os.makedirs(log_folder_name, exist_ok=True)
log_file_path = os.path.join(log_folder_name, 'logging.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')
logger = logging.getLogger()

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def process_started_message(filename):
    message = f"({filename}) Process started."
    logger.info(message)

def conversion_started_message(filename, file_extension, output_path):
    message = f"({filename}) Converting {filename}{file_extension} to {output_path}"
    logger.info(message)

def audio_extracted_message(filename):
    message = f"({filename}) Audio extracted."
    logger.info(message)

def silent_removed_message(filename):
    message = f"({filename}) Silent segment at the end removed successfully."
    logger.info(message)

def no_merge_performed_message(filename):
    message = f"({filename}) No valid segments found. No merge performed."
    logger.info(message)

def audio_chunks_generated_message(filename, *args):
    info = ""
    if len(args) == 1 and all(isinstance(arg, int) for arg in args):
        info = f"{args[0]}"

    message = f"({filename}) Audio file split into {info} chunks."
    logger.info(message)

def audio_chunks_cleaned_message(filename):
    message = f"({filename}) Audio chunks deleted."
    logger.info(message)

def process_completed_message(filename):
    message = f"({filename}) Process completed successfully."
    logger.info(message)