# Golf Score Tracker

A simple desktop application for tracking and analyzing your golf performance over time.

## Overview

Golf Score Tracker allows golfers to record details about their rounds, visualize their progress, set personal goals, and view performance statistics. The application provides an easy-to-use graphical interface for entering round data and viewing analytical insights.

## Features

- **Add Round Data**: Record information about your golf rounds including:
  - Course name
  - Date
  - Score
  - Number of putts
  - Fairways hit
  - Greens in regulation
  - Personal notes

- **Scoring Trends**: Visualize your scoring progress over time with an interactive graph

- **Goal Setting**: Set and track personal golfing goals

- **Statistics**: View key performance metrics including:
  - Total rounds played
  - Average score
  - Average putts per round

## Requirements

- Python 3.x
- Required Python libraries:
  - matplotlib
  - tkinter
  - json (included in Python standard library)

## Installation

1. Ensure that Python 3.x is installed on your system
2. Install required libraries:
   ```
   pip install matplotlib
   ```
   Note: tkinter is typically included with Python installations

3. Download the script file to your local machine
4. Run the application:
   ```
   python golf_score_tracker.py
   ```

## Usage

1. Click "Add Round" to enter data for a new golf round
2. Complete all the requested fields in the pop-up dialogs
3. Use "Show Scoring Trends" to view a graph of your scores over time
4. Set personal goals with the "Set Goals" button
5. View your overall performance statistics by clicking "Show Statistics"
6. Exit the application using the "Exit" button

## Data Storage

The application automatically saves your data to a file named `golf_data.json` in the same directory as the script. This ensures your golf round data is preserved between sessions.

## License

This project is free to use and modify for personal use.

