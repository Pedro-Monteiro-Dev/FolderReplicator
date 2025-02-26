import sys
import argparse
import logging
import os
import shutil
import time

import hashlib

def calculate_md5(file_path):
    """
    Simple md5 calculation
    """
    md5_hash = hashlib.md5()
    
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    
    return md5_hash.hexdigest()

def compare_files(source_file, replica_file):
    """
    Compare the files to see if they are different
    """
    #Check if it's a different size (It's more efficient for comparing large files)
    if os.path.getsize(source_file) != os.path.getsize(replica_file):
        return False
    
    #Confirm md5
    return calculate_md5(source_file) == calculate_md5(replica_file)

def sync_folders(source_folder, replica_folder):
    """
    Synchronize the source and replica folders
    """

    try:

        #Syncs Files
        for root, dirs, files in os.walk(source_folder):
            for file_name in files:
                source_file = os.path.join(root, file_name)
                
                relative_path = os.path.relpath(source_file, source_folder)
                replica_file = os.path.join(replica_folder, relative_path)

                if not os.path.exists(replica_file):
                    os.makedirs(os.path.dirname(replica_file), exist_ok=True)
                    shutil.copy2(source_file, replica_file)
                    print(f"Created new file -> {replica_file}")
                    logging.info(f"Created new file -> {replica_file}")
                elif not compare_files(source_file, replica_file):
                    shutil.copy2(source_file, replica_file)
                    print(f"Updated File -> {replica_file}")
                    logging.info(f"Updated File -> {replica_file}")

        #Check For removed or additional files
        for root, dirs, files in os.walk(replica_folder,topdown=False):
            for file_name in files:
                replica_file_path = os.path.join(root, file_name)

                relative_path = os.path.relpath(replica_file_path, replica_folder)
                source_file_path = os.path.join(source_folder, relative_path)

                if not os.path.exists(source_file_path):
                    
                    os.remove(replica_file_path)
                    
                    print(f"Deleted File -> {replica_file_path}")
                    logging.info(f"Deleted File -> {replica_file_path}")
            
            #Clean Empty Folders
            for dir_name in dirs:
                replica_dir_path = os.path.join(root, dir_name)

                relative_dir_path = os.path.relpath(replica_dir_path, replica_folder)
                source_dir_path = os.path.join(source_folder, relative_dir_path)

                if not os.path.exists(source_dir_path) and not os.listdir(replica_dir_path):
                    os.rmdir(replica_dir_path)
    except Exception as e:
        print(f"Error syncing folders: {e}")
    


def main():

    parser = argparse.ArgumentParser(description="")

    parser.add_argument('source', type=str, help='Path to the source folder')
    parser.add_argument('replica', type=str, help='Path to the replica folder')
    parser.add_argument('interval', type=int, help='Synchronization interval in seconds')
    parser.add_argument('log', type=str, help='Path to the log file')

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.realpath(__file__))

    source_folder = os.path.abspath(os.path.join(script_dir, args.source)) if not os.path.isabs(args.source) else args.source
    replica_folder = os.path.abspath(os.path.join(script_dir, args.replica)) if not os.path.isabs(args.replica) else args.replica
    interval = args.interval
    #log_file = args.log
    log_file = os.path.abspath(os.path.join(script_dir, args.log)) if not os.path.isabs(args.log) else args.log
    

    #Check If Folders Exist

    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        sys.exit(1)

    log_dir = os.path.dirname(log_file)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder, exist_ok=True)

    #Logging

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )

    print("Program Initialized!")

    try:
        while True:
            
            sync_folders(source_folder, replica_folder)

            time.sleep(interval)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()