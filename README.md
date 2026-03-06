# DSP Animal Species Recognition and Human Detection

This repository contains a Streamlit app and utilities for detecting wildlife species and humans in images or video using a YOLO-based model.

**Quick Overview**

**Setup (Windows)**
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
streamlit run app.py
```

**Notes on Streamlit & inotify errors**
  - Remove any large folders from the repository (datasets, `venv/`, `env/`, image folders). Use a `.gitignore` to prevent re-committing them. A `.gitignore` has been added to the repo.
  - Or disable Streamlit's file watcher by adding `.streamlit/config.toml` with:

```toml
[server]
fileWatcherType = "none"
```


**Repository files of interest**

**Typical workflow**

**Deploying to Streamlit Sharing or similar**

**Troubleshooting**
  - Activate the virtual environment before installing or running.
  - Verify `yolo_corrected.pt` is present and readable.

**Contact / Next steps**
  - Commit and push the `README.md` for you.
  - Help remove any large files from Git history if your repo contains datasets or virtualenvs.
