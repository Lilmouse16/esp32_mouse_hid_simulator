import csv

# Input and output file paths
input_csv = "/Users/dario/OneDrive/Documents/PlatformIO/Projects/esp32_mouse_hid_simulator/data/cleaned_data.csv"
output_header = "/Users/dario/OneDrive/Documents/PlatformIO/Projects/esp32_mouse_hid_simulator/include/movement_sequence.h"

try:
    with open(input_csv, "r") as csvfile, open(output_header, "w") as headerfile:
        reader = csv.DictReader(csvfile)
        output_lines = []

        for row in reader:
            type_ = row["Type"]
            x = row["X"]
            y = row["Y"]
            delay = row["Delay"]
            output_lines.append(f"{{MovementStep::{type_}, {x}, {y}, {delay}}}")

        header_content = f"""
#ifndef MOVEMENT_SEQUENCE_H
#define MOVEMENT_SEQUENCE_H

struct MovementStep {{
    enum Type {{ MOVE, LEFT_DOWN, LEFT_UP, WAIT, KEY_PRESS }};
    Type type;
    int x, y, delay_ms;
}};

const MovementStep sequence[] = {{
    {', '.join(output_lines)}
}};

#endif
"""
        headerfile.write(header_content)
        print(f"Header file '{output_header}' generated successfully.")

except Exception as e:
    print(f"Error: {e}")
