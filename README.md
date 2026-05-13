# Wildlife Species Recognition & Human Detection

A real-time deep learning application for detecting and classifying wildlife species and identifying potential poachers in aerial thermal infrared (TIR) surveillance footage. Built with **YOLOv11** and deployed as an interactive **Streamlit** dashboard.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?logo=streamlit&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-v11-00FFFF?logo=yolo&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Monitoring protected areas to curb illegal activities like poaching is a monumental task. Advances in unmanned aerial vehicles (UAVs) and thermal infrared cameras have made real-time data acquisition easier, especially at night when poaching typically occurs. However, processing large volumes of TIR data accurately and quickly remains a challenge.

This project leverages deep learning to:
- **Detect and classify** wildlife species (Elephant, Lion, Giraffe) from aerial TIR video.
- **Identify humans** (potential poachers) in surveillance footage and raise alerts.
- **Visualize detection analytics** through an interactive web dashboard with confidence plots, heatmaps, and species summaries.

## Features

| Feature | Description |
|---|---|
| **YOLO-based Detection** | Fine-tuned YOLOv11 model (2.59M params) achieving **0.633 mAP** at 5.44 FPS |
| **Video Upload & Processing** | Upload `.avi`/`.mp4` videos for real-time object detection |
| **Poacher Alert System** | Automatic warning when a human is detected in footage |
| **Detection Heatmap** | Spatial visualization of bounding-box locations across frames |
| **Confidence Analytics** | Per-frame confidence plots broken down by species |
| **Species Summary** | Min/max count per species across all video frames |
| **Downloadable Output** | Export processed video with bounding-box overlays |
| **EDA Dashboard** | Class distributions, bounding-box area analysis, and location heatmaps |

## Tech Stack

- **Deep Learning** — [Ultralytics YOLOv11](https://docs.ultralytics.com/), PyTorch
- **Computer Vision** — OpenCV (grayscale, Canny edges, adaptive thresholding)
- **Web App** — Streamlit
- **Data Visualization** — Plotly, Matplotlib, Seaborn
- **Dataset** — [BIRDSAI](https://lila.science/datasets/birdsai/) (Benchmarking IR Dataset for Surveillance with Aerial Intelligence)

## Project Structure

```
├── app.py                  # Main Streamlit application
├── src/
│   ├── __init__.py
│   ├── preprocessing.py    # Frame preprocessing pipeline
│   └── visualization.py    # Heatmap generation & class mappings
├── models/
│   └── yolo_corrected.pt   # Fine-tuned YOLOv11 weights
├── assets/                 # Static images used in the dashboard
│   ├── cover.png
│   ├── birdsai.png
│   └── *.png               # EDA plots
├── scripts/
│   └── inspect_model.py    # Utility to inspect model class names
├── .streamlit/
│   └── config.toml         # Streamlit server configuration
├── requirements.txt        # Python dependencies
├── packages.txt            # System-level dependencies (for deployment)
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/Wildlife-Species-Recognition-Human-Detection.git
cd Wildlife-Species-Recognition-Human-Detection

# Create and activate a virtual environment
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`.

## Usage

1. **Home Page** — Project overview and contact information.
2. **Dataset Description** — Details about the BIRDSAI thermal IR dataset.
3. **Exploratory Data Analysis** — Visualizations of class distributions, bounding-box sizes, and spatial heatmaps.
4. **Test Your Video** — Upload a thermal IR video to run detection. View confidence plots, heatmaps, species summaries, and download the annotated output video.

## Dataset

The [BIRDSAI dataset](https://lila.science/datasets/birdsai/) contains nighttime long-wave thermal infrared imagery of animals and poachers in Southern Africa. Species covered include Elephant, Lion, Giraffe, Hippo, Zebra, Rhino, Crocodile, and Dog, along with human annotations.

## Acknowledgments

- **Supervisor:** Dr Riyaz Ahamed, Universiti Malaya
- **Dataset:** BIRDSAI — Labeled Information Library of Alexandria: Biology and Conservation (LILA BC)

## License

This project is licensed under the [MIT License](LICENSE).
