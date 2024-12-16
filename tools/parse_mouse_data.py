import re
import csv

# Input and output file paths
input_file = "/Users/dario/OneDrive/Documents/PlatformIO/Projects/esp32_mouse_hid_simulator/data/mouse_data.txt"
output_csv = "/Users/dario/OneDrive/Documents/PlatformIO/Projects/esp32_mouse_hid_simulator/data/cleaned_data.csv"


try:
    with open(input_file, "r", encoding="utf-8") as infile, open(output_csv, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Type", "X", "Y", "Delay"])  # CSV headers

        for line in infile:
            line = line.strip()
            if line.startswith("Sleep"):
                # Parse Sleep commands for delays
                delay = re.search(r"Sleep, (\d+)", line)
                if delay:
                    writer.writerow(["WAIT", 0, 0, delay.group(1)])
            elif line.startswith("Click"):
                # Parse Click commands for mouse actions
                match = re.search(r"Click, (-?\d+), (-?\d+) Left, (Down|Up)", line)
                if match:
                    x, y, action = match.groups()
                    type_ = "LEFT_DOWN" if action == "Down" else "LEFT_UP"
                    writer.writerow([type_, x, y, 0])
            elif line.startswith("Send"):
                # Skip keyboard commands like Send, {F9}
                continue

    print(f"Parsed mouse data saved to '{output_csv}'.")

except FileNotFoundError:
    print(f"Error: The input file '{input_file}' was not found. Make sure it exists.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
