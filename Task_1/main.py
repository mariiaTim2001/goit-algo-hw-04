import argparse
import os
from handlers.copy import copy_and_categorize_files

def main():
    parser = argparse.ArgumentParser(description="Recursively copies and sorts files by extension")
    parser.add_argument('source_dir', type=str, help="Path to the source directory")
    parser.add_argument('destination_dir', nargs='?', default='dist', type=str, help="Path to the destination directory (default: 'dist')")
    
    args = parser.parse_args()
    
    source_dir = args.source_dir
    destination_dir = args.destination_dir
    
    print(f"▶️ Starting file copy...")
    print(f"Source Directory: {os.path.abspath(source_dir)}")
    print(f"Destination Directory: {os.path.abspath(destination_dir)}")
    
    copy_and_categorize_files(source_dir, destination_dir)
    
    print("✅ Copying finished.")

if __name__ == "__main__":
    main()