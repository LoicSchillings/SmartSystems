
<h1 align="center">
  <a href="#"> Smart Systems Project </a>
</h1>

<p align="center">

  <img alt="Stars" src="https://img.shields.io/github/stars/LoicSchillings/SmartSystems?style=social">
  
  <a href="https://github.com/LoicSchillings/SmartSystems">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/LoicSchillings/SmartSystems">
  </a>
</p>

![Project Banner](./resources/images/image-1.png)

<h4 align="center"> 
   Status: 🧪 Prototype
</h4>

<p align="center">
 <a href="#about">About</a> •
 <a href="#technical-approach">Technical Approach</a> • 
 <a href="#installation">Installation</a> •
 <a href="#roadmap">Roadmap</a> • 
 <a href="#project-requirements">Project Requirements</a> • 
 <a href="#documentation">Documentation</a> •
 <a href="#contributors">Contributors</a>
</p>

---

## 🧭 About <a name="about"></a>
This project uses a camera and artificial intelligence to recognize traffic signs in real time. The system runs on a Jetson Nano and uses a model trained with Edge Impulse to process images directly on the device.

We made this project to learn how computer vision and edge AI work in practice, and to show that traffic sign recognition can be done without using cloud services. Running the model locally makes the system fast and reliable.


---

## 🚀 Technical Approach <a name="technical-approach"></a>
### Hardware
- ✨ NVIDIA — _Jetson Nano_
  - ARM — _AArch64_
  - GPU — _CUDA cores_
- 🧩 Camera — _Logitech_
  - USB — _HD 720P_

### Software
- ⚙️ Ubuntu Linux — _OS_

### Programming Language
- 📱 Python3

### Machine Learning / AI
- 🌡️ Edge Impulse Studio
  - Dataset management
  - Labeling
  - Training

### Model Runtime
- 📡 Edge Impulse Linux SDK — _edge-impulse-linux_
- 🔋 Model Format — _.eim format_

---

## 🛠️ Installation <a name="installation"></a>

```bash
# Clone this repository
git clone https://github.com/MauroDeBruyn/REPO-NAME.git

# Navigate into the project folder
cd REPO-NAME

# Install dependencies
# Example for np, pip, python, etc.
npm install
# or
pip install -r requirements.txt

# Run the app
npm start
# or
python app.py
```

---

## 🗺️ Roadmap <a name="roadmap"></a>
- ✅ **Completed**
   - _Camera sees signs clearly_
   - _AI-model can define sign types with some accuracy_

- 🔄 **Ongoing**
   - _Creating larger and preciser dataset for better AI accuracy_

---

## ⚙️ Project Requirements <a name="project-requirements"></a>
- **Requirement 1 :** _The Jupyter Notebook has a clear representation of the workings of the project_
- **Requirement 2 :** _The Notebook works out of the box_
- **Requirement 3 :** _The Notebook shows a step-by-step operation of the project_
- **Requirement 4 :** _Notebook can be presented/demonstrated clearly_

---

## 📚 Documentation <a name="documentation"></a>
- See README about PC based AI and Jetson Nano based AI in their respective folders for better explanations.
- Jetson Nano based AI:(https://github.com/LoicSchillings/SmartSystems/tree/main/resources/Jetson-Nano-Based-AI)
- PC based AI: (https://github.com/LoicSchillings/SmartSystems/tree/main/resources/PC-Based-AI)

---

## 👥 Contributors <a name="contributors"></a>
  
- **Ine Beddegenoots** – Student – [GitHub](https://github.com/inebdg)  
- **Loic Schillings** – Student – [GitHub](https://github.com/LoicSchillings)
- **Mauro De Bruyn** – Author – [GitHub](https://github.com/MauroDeBruyn)
