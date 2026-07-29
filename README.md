# KeyPulse

KeyPulse is a keyboard activity monitor. It tracks the volume of keystrokes over time to analyze productivity patterns without recording the actual keys pressed, ensuring absolute user privacy.₹ And is super simple to understand and use. Now go on try it out and spy on your key time with KeyPulse

Unlike a keylogger, KeyPulse does not record which keys are pressed. It only adds a counter. The resulting log contains only timestamps and integers (e.g., `2026-07-29 21:04:45, 13`), making it impossible to reconstruct sensitive data or passwords.

Note: Please run this project only using python3.12, not the latest 3.14 as the dependencies and binaries are not yet supported for it, so make sure you have it

## System Architecture

The system consists of two primary modules:

1.  **Tracking Daemon (`main.py`)**: 
    - A background process that hooks into system-level keyboard events using `pynput`.
    - Uses a thread-safe `threading.Lock` to ensure counts are accurate across OS event threads.
    - Flushes data to `keystroke_log.csv` every 60 seconds and resets the atomic counter.
2.  **Visualization Engine (`plot_activity.py`)**: 
    - An analysis script that processes the CSV using `Pandas`.
    - Generates a high-resolution Timeline Plot (KPM over time).
    - Generates an Hourly Heatmap to visualize peak activity periods throughout the day.

## Setup & Installation

### Prerequisites
- **Python 3.12** (Recommended for stability and pre-compiled binary support).
- **macOS Permissions**: macOS requires explicit permission to monitor keyboard events.

### Installation Steps (macOS)

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/lkprathika1102/KeyPulse>
   cd key-pulse
   ```

2. **Install Python 3.12** (via Homebrew):
   ```bash
   brew install python@3.12
   ```

3. **Initialize a Virtual Environment**:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 🛠️ Usage

### 1. Start Tracking
Run the daemon to begin capturing activity:
```bash
python main.py
```
The daemon will log activity to the console every minute. Press `Ctrl+C` to stop.

### 2. Generate Visuals
Once you have collected data, run the visualization script:
```bash
python plot_activity.py
```
This will produce two files in the project root:
- `activity_timeline.png`: A linear graph of your typing volume.
- `activity_heatmap.png`: A grid showing your most active hours.

## Troubleshooting macOS Permissions( what I basically faced)
If the tracker runs but records `0` keystrokes:
1. Open System Settings $\rightarrow$ Privacy & Security $\rightarrow$ Accessibility
2. Find your Terminal (or VS Code) in the list.
3. Toggle the switch to ON.
4. Restart the terminal and run `python main.py` again.

 For Windows It just works directly 
## Testing Guide

1. **Daemon Test**: Run `main.py` and type for 2 minutes. Verify that the console prints `Recorded X keystrokes` every 60 seconds.
2. **Privacy Audit**: Open `keystroke_log.csv`. Confirm that no actual characters/text are being stored.
3. **Visualization Test**: Run `plot_activity.py` and verify that the two PNG files are generated with correct data.
4. **Edge Case Test**: Delete `keystroke_log.csv` and run `plot_activity.py` to confirm the script handles missing data 


You should get something like this

<img width="3600" height="1800" alt="activity_timeline" src="https://github.com/user-attachments/assets/178edf17-5023-4b22-8ecd-6e7039a3ed99" />

