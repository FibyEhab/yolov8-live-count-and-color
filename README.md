# YOLOv8 Detect · Count · Colorize 🎨

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=flat&logo=yolo&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

---

## 📋 About

Real-time object detection system using **YOLOv8** that does three things at once:
- 🔍 **Detects** objects from your webcam using YOLOv8
- 🔢 **Counts** the total number of detected objects live on screen
- 🎨 **Colorizes** each object class with its own unique persistent color

Each class gets a random color on first detection and **keeps that exact color for every frame**, making it effortless to visually distinguish between classes.

**Key Features:**
- ⚡ Real-time detection at 25–60 FPS (depends on model + hardware)
- 🎨 **Unique persistent color per class** — consistent across all frames
- 🔢 **Live object counter** displayed on screen at all times
- 🏷️ Confidence scores shown on every bounding box
- 📹 Live webcam stream processing
- 🖥️ Auto full-screen window on launch
- 🧹 Clean modular code — easy to read and extend

---

## 🎨 What Makes This Different?

Most object detection demos use a fixed color list. This project assigns a **random color to each class dynamically**:

```
First time "person" detected  →  random color assigned (e.g. Green)
Every next "person" frame     →  same Green used
First time "car" detected     →  different random color (e.g. Blue)
Every next "car" frame        →  same Blue used
```

**Result:** Every class always has its own color — no confusion, no repetition.

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Object Detection** | YOLOv8 (Ultralytics) |
| **Computer Vision** | OpenCV 4.8+ |
| **Language** | Python 3.10+ |
| **Deep Learning Framework** | PyTorch (auto-installed) |

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- Webcam connected to your computer
- 4 GB+ RAM (8 GB recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/yolov8-detect-count-colorize.git
cd yolov8-detect-count-colorize
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

> **First run:** YOLOv8s model (~22 MB) downloads automatically.

---

## 🚀 Usage

### Run
```bash
python main.py
```

### What Happens
1. **Webcam opens** at 1920×1080 resolution
2. **YOLOv8 processes** each frame in real-time
3. **Objects detected** — bounding box drawn per object
4. **Color assigned** — first detection of each class gets a unique random color
5. **Counter updated** — total object count shown live on screen
6. **Press `Q`** to quit

### Output Example
```
[INFO] Loading model: yolov8s.pt
[INFO] Camera opened at 1920×1080
[INFO] Press  Q  to quit.
[INFO] Quit signal received — exiting.
```

---

## 💡 How the Color System Works

### Color Assignment Logic
```python
class_colors = {}  # stores: class_id → BGR color

for box in result.boxes:
    cls_id = int(box.cls[0])

    # First detection of this class → assign random color
    if cls_id not in class_colors:
        class_colors[cls_id] = [random.randint(80, 255) for _ in range(3)]

    # All frames → use the same stored color
    color = class_colors[cls_id]
```

### Why This Matters
- **Easy visual tracking** — same class always looks the same
- **Professional appearance** — organized, consistent visualization
- **No conflicts** — each class has its own unique color
- **Memory efficient** — only one color stored per class

---

## 🎨 Customization Guide

### Option 1: Manual Color Assignment
```python
class_colors = {
    0: [0, 255, 0],    # Person  → Green
    2: [255, 0, 0],    # Car     → Blue (BGR)
    16: [0, 0, 255],   # Dog     → Red
}
```

### Option 2: Reproducible Colors (Fixed Seed)
```python
random.seed(42)  # Add before the while loop — same colors every run
```

### Option 3: Adjust Confidence Threshold
```python
CONFIDENCE = 0.7  # Higher = fewer false positives (default: 0.5)
```

### Option 4: Change Resolution
```python
FRAME_WIDTH  = 640   # Faster processing
FRAME_HEIGHT = 480
```

### Option 5: Use Different YOLOv8 Variant
```python
MODEL_PATH = "yolov8n.pt"  # Nano  — fastest
MODEL_PATH = "yolov8s.pt"  # Small — balanced ⭐ default
MODEL_PATH = "yolov8m.pt"  # Medium
MODEL_PATH = "yolov8l.pt"  # Large
MODEL_PATH = "yolov8x.pt"  # Extra Large — most accurate
```

### Option 6: Process a Video File Instead of Webcam
```python
cap = cv2.VideoCapture("path/to/video.mp4")
```

---

## 📊 Performance Reference

| Model | Size | FPS (CPU) | FPS (GPU) | Accuracy |
|-------|------|-----------|-----------|----------|
| YOLOv8n | 6 MB | 40–50 | 100+ | ★★ |
| YOLOv8s | 22 MB | 30–40 | 80+ | ★★★ |
| YOLOv8m | 50 MB | 20–30 | 60+ | ★★★★ |
| YOLOv8l | 83 MB | 15–20 | 50+ | ★★★★★ |
| YOLOv8x | 131 MB | 10–15 | 40+ | ★★★★★ |

**Detectable classes:** 80 (COCO Dataset) — person, car, dog, chair, laptop, and more.

---

## 🔧 Advanced Configuration

### GPU Acceleration
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Better Performance on Slow Hardware
```python
MODEL_PATH   = "yolov8n.pt"
FRAME_WIDTH  = 640
FRAME_HEIGHT = 480
```

### Frame Skipping for Low-End Devices
```python
frame_count = 0
while True:
    ret, frame = cap.read()
    if frame_count % 2 == 0:           # Process every other frame
        results = model.predict(...)
    frame_count += 1
```

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'ultralytics'`
```bash
pip install --upgrade ultralytics opencv-python
```

### Webcam not detected
```bash
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"
# Should print: True
```

### FPS too low
1. Switch to `yolov8n.pt` or `yolov8s.pt`
2. Reduce resolution to 640×480
3. Enable GPU acceleration
4. Close background applications

### `CUDA out of memory`
```python
MODEL_PATH = "yolov8s.pt"  # Use a smaller model
```

### Camera permission denied (Mac / Linux)
- **Mac:** System Preferences → Security & Privacy → Camera → Terminal ✓
- **Linux:** `sudo usermod -a -G video $USER`

---

## 📚 Learning Resources

- [YOLOv8 Official Docs](https://docs.ultralytics.com/) — Complete documentation
- [OpenCV Tutorials](https://docs.opencv.org/) — Computer vision basics
- [COCO Dataset](https://cocodataset.org/) — 80 detectable classes list
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html) — Deep learning framework

---

## 🚀 Next Steps / Extensions

1. **Add Object Tracking** — Use DeepSORT to track objects across frames with IDs
2. **Add Recording** — Save the detection video to a file
3. **Add Per-Class Statistics** — Count how many of each class per minute
4. **Add GUI** — Build a desktop app with Tkinter or PyQt
5. **Add Web Interface** — Stream detections via Flask or FastAPI
6. **Add Alert System** — Trigger notifications when a specific class is detected

---

## 📁 Project Structure

```
yolov8-detect-count-colorize/
├── main.py              # Main detection script
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignores weights, venvs, cache
└── README.md            # This file
```

---

## 🤝 Contributing

Found a bug? Have an idea? Contributions are welcome!

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

**YOLOv8 Model:** Licensed under AGPL-3.0 by Ultralytics.

---

## 👨‍💻 Author

**Your Name** — AI / Computer Vision Enthusiast

📧 **Email:** your@email.com
💼 **LinkedIn:** [Your Name](https://linkedin.com/in/your-profile)
🐙 **GitHub:** [@your-username](https://github.com/your-username)

Feel free to reach out for questions, suggestions, or collaborations!

---

## ⭐ Support This Project

If this project helped you:
- **⭐ Star** this repository
- **🍴 Fork** it for your own use
- **📢 Share** it with others learning computer vision

Every star motivates me to keep building! 🙏

---

**Made with ❤️ for the AI & Computer Vision community**
