import csv
import statistics

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data(self):
        try:
            # Attempt to open the CSV file and read data
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)  # Assuming the first row is a header
                # Convert each row into a dictionary with column names as keys
                self.data = [dict(zip(header, map(str, row))) for row in reader]
                print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")

    def display_summary_statistics(self):
        if not self.data:
            print("No data to analyze. Load data first.")
            return

        # Identify numeric columns
        numeric_columns = [col for col in self.data[0] if all(row[col].replace('.', '').isdigit() for row in self.data)]
        
        if not numeric_columns:
            print("No numeric columns found in the data.")
            return

        print("\nSummary Statistics:")
        # Calculate mean and standard deviation for each numeric column
        for column in numeric_columns:
            values = [float(row[column]) for row in self.data]
            print(f"{column} - Mean: {statistics.mean(values)}, Std Dev: {statistics.stdev(values)}")

def main():
    file_path = "example_data.csv"  # Replace with the path to your CSV file
    data_analyzer = DataAnalyzer(file_path)

    data_analyzer.load_data()
    data_analyzer.display_summary_statistics()

if __name__ == "__main__":
    main()

