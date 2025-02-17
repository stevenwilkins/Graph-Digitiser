# Graph Digitizer Wizard - README

## Overview
The Graph Digitizer Wizard is a Python application that allows you to manually extract data points from a graph image. It includes features such as multiple series capture, zoom functionality, axis calibration, and CSV export.

## Requirements
- Python 3.9 or later
- Pillow (Image handling)
- Tkinter (GUI framework)

## Installation
1. Install Python 3 from [python.org](https://www.python.org/).
2. Install required modules:
   ```bash
   pip install pillow
   ```

## How to Use
### Step 1: Launch the App
Run the script using:
```bash
python graph_digitizer.py
```

### Step 2: Load Graph Image
A file dialog will appear. Select your graph image (JPG or PNG).

### Step 3: Calibrate the Axes
- **Origin:** Click on the (0,0) point on the graph.
- **X-axis Extreme:** Click on the far-right end of the x-axis, then enter the maximum x value.
- **Y-axis Extreme:** Click on the highest point on the y-axis, then enter the maximum y value.

### Step 4: Record Points
Click on points along the graph curve. Each point will be marked with a red dot.
- Use the mouse wheel to **zoom** in and out for accuracy.

### Step 5: Save Series
- Click the **Save Series** button to save the current series of points.
- You will be prompted to add another series or finish.

### Step 6: Export All Series
- When finished, choose a CSV file location to export all recorded series.
- The CSV format will include:
  ```csv
  series,x_scaled,y_scaled
  1,10.5,15.2
  1,12.1,17.3
  2,9.8,14.5
  ```

## Features Summary
- **Multiple Series Recording:** Collect multiple sets of data points from a single graph.
- **Axis Calibration:** Accurately scale data based on axis extremes.
- **Zoom Functionality:** Use the mouse wheel for better precision.
- **CSV Export:** Save results in an organized spreadsheet format.

## License
This project is licensed under the MIT License.

## Contact
For suggestions or issues, feel free to reach out via GitHub or email.

---
Enjoy digitizing your graphs!
