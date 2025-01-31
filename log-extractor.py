import os
import sys
import mmap
import datetime

class LogExtractor:
    def __init__(self, log_file_path):
        """
        Initialize the LogExtractor with the path to the log file.
        
        Args:
            log_file_path (str): Path to the large log file
        """
        self.log_file_path = log_file_path
        
        # Create output directory if it doesn't exist
        os.makedirs('output', exist_ok=True)
    
    def extract_logs_for_date(self, target_date):
        """
        Extract log entries for a specific date efficiently.
        
        Args:
            target_date (str): Date in format 'YYYY-MM-DD'
        
        Returns:
            str: Path to the output file with extracted logs
        """
        # Validate date format
        try:
            datetime.datetime.strptime(target_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        output_file = f'output/output_{target_date}.txt'
        
        # Use memory mapping for efficient file reading
        with open(self.log_file_path, 'r') as file:
            mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            
            with open(output_file, 'w') as output:
                # Read file line by line using memory mapping
                current_pos = 0
                while current_pos < mmapped_file.size():
                    # Move to next line
                    line_end = mmapped_file.find(b'\n', current_pos)
                    if line_end == -1:
                        break
                    
                    # Extract line
                    line = mmapped_file[current_pos:line_end].decode('utf-8')
                    
                    # Check if line starts with target date
                    if line.startswith(target_date):
                        output.write(line + '\n')
                    
                    current_pos = line_end + 1
        
        return output_file

def main():
    """
    Main function to handle command-line argument and log extraction
    """
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    target_date = sys.argv[1]
    
    try:
        extractor = LogExtractor('test_logs.log')
        output_path = extractor.extract_logs_for_date(target_date)
        print(f"Logs for {target_date} extracted to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
