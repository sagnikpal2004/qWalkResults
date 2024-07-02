RESULT_FILE = ""
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Utils for qWalkResults. Debug mode')

    help = "File path"
    parser.add_argument('--file', type=str, help=help, required=True)
    
    args = parser.parse_args()

    import os
    if not os.path.exists(args.file):
       raise FileNotFoundError(f"The file {args.file} does not exist.")
    if not args.file.endswith('.csv'):
       raise ValueError(f"The file {args.file} is not a CSV file.")
    RESULT_FILE = args.file

class qWalkResult:
    def __init__(self):
        self.result_file = ""
        self.file = open(self.result_file)

    def setFile(self, filename = RESULT_FILE):
        self.result_file = filename
        self.parseFile()
    def parseFile(self):
        pass
    def writeFile(self):
        pass

    def setMetadata(self):
        pass
    def setProbability(self, timestep, ):
        pass
    
    from enum import Enum
    class DisplayMode(Enum):
        PASS = "PASS"
    def displayResult(mode: DisplayMode):
        pass

import csv
def writeToCSV(filename: str, time: int, data: list[float]):
  with open(filename, mode="a", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow([time] + data)