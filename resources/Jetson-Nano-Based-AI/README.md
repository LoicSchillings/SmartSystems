# Jetson Nano Based AI System

This folder contains all files related to the development of a **Jetson Nano–based AI system** for image and live camera processing.  
The project evolved through multiple stages, experiments, and technical challenges, which are documented below to explain **how and why these files exist**.

---

## 📖 Project Origin & Development Story

The project originally started using **Jupyter Notebooks** on the **NVIDIA Jetson Nano**.

### 1. Environment & Library Setup
- `get-pip.py`  
- `LibraryInstallation.ipynb`  

These files were used to install **pip** and all required Python libraries on the Jetson Nano.  
At this stage, the goal was simply to prepare the device so it could run computer vision and AI-related code.

We were unaware that all code had to be in one notebook.

---

### 2. Camera & Image Testing
- `TestImageLoadingAndLiveVideo.ipynb`  

After installing the libraries, we tested:
- Image loading
- Live camera input

This confirmed that the Jetson Nano camera and OpenCV setup worked correctly.

---

### 3. Main AI System Attempt
- `main.ipynb`  

Once the camera tests were successful, development moved to the main notebook where the **entire AI system** was supposed to run:
- Loading the AI model
- Processing camera frames
- Running inference

#### ⚠️ Major Problem Encountered
At this stage, a critical issue appeared:
- The Jupyter Notebook Python kernel tried using **more RAM than the Jetson Nano provides**
- This caused the kernel to **crash repeatedly**
- As a result, development inside notebooks became unreliable

Jetson Nanos running an AI typically have 4GB of RAM while ours only had 2GB.

This forced a complete rethink of the project approach.

---

### 4. Switching to a Virtual Environment (Final Approach)
To solve the memory issues:
- A **virtual environment** was created directly in the Jetson Nano file system
- The notebook-based approach was abandoned
- All required libraries were reinstalled inside the virtual environment

Relevant files and folders:
- `ei-env` – Virtual environment setup
- `.eim` files – Edge Impulse AI models

In this environment:
- The camera worked
- The AI model ran successfully
- Inference was stable without crashes

To open this environment run these commands in terminal:

```bash
- python3.8 -m venv ei-env
- source ei-env/bin/activate
- Then install all libraries
```



---

### 5. Dataset Limitation
Although the system worked correctly, the final limitation was:
- The dataset was **too small**
- This caused the model to be **less accurate**

With more images, the AI model would have performed significantly better.

---

## 📁 File Overview

| File / Folder | Purpose |
|---------------|--------|
| `get-pip.py` | Installs pip on the Jetson Nano |
| `LibraryInstallation.ipynb` | Installs required Python libraries |
| `TestImageLoadingAndLiveVideo.ipynb` | Tests image loading and live camera feed |
| `main.ipynb` | Initial full AI system attempt |
| `traffic_sign_classifier.keras` | Trained AI model |
| `.eim` files | Edge Impulse AI models |
| `edgeImpulseDatasetINELOIC` | Dataset used for training |
| `ei-env` | Virtual environment setup |
| Other files | Individual code experiments and tests |

---

## 🧪 About the Remaining Files

All remaining files in this repository are **experiments or tests** of individual components, such as:
- Camera handling
- Model loading
- Inference logic
- Library compatibility

These were created to validate specific parts before integrating them into the main system.

---

## 🖥️ System Requirements

- NVIDIA Jetson Nano
- Python 3
- OpenCV
- TensorFlow / Edge Impulse libraries
- Camera module

---

## 🚀 Final Notes

- The final working solution runs **outside Jupyter Notebooks**
- Memory constraints were the main technical challenge
- The project successfully demonstrated AI inference on embedded hardware
- A larger dataset would significantly improve results

This project documents not just the final result, but the **real development journey**, challenges, and lessons learned.
