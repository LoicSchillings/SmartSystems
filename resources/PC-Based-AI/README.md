# PC-Based AI Traffic Sign Recognition System

This project is a **PC-based AI system** that uses **TensorFlow / Keras** and **OpenCV** to train and run a **traffic sign classifier**.  
The system can recognize traffic signs (such as *bebouwde kom* and *einde bebouwde kom*) using a trained neural network model.

---

## 📁 Project Structure

```bash
SMARTSYSTEMS/
│
├── training/
│ ├── bebouwdekom/
│ ├── eindebebouwdekom/
│ └── ...
│
├── testing/
│ ├── bebouwdekom/
│ ├── eindebebouwdekom/
│ └── ...
│
├── traffic_sign_classifier.keras
├── jetsonnanotaak.ipynb
└── README.md
```

---

## 🧠 How It Works

1. **Training**
   - Images are loaded using `ImageDataGenerator`
   - Images are resized to **224x224**
   - A neural network is trained to classify traffic signs
   - The trained model is saved as:
     ```
     traffic_sign_classifier.keras
     ```

2. **Inference (Prediction)**
   - OpenCV captures or loads an image
   - The image is preprocessed
   - The trained model predicts the traffic sign class
   - The result is displayed or printed

---

## 💾 How to Download & Run (Quick Start)

### 1. Clone or Download the Files
- Download the repository or open the folder `SMART SYSTEMS`
- Make sure `traffic_sign_classifier.keras` is in the project folder

### 2. Install Requirements
```bash
pip install tensorflow opencv-python numpy
```

3. Run the Notebook

Open the Jupyter Notebook:

```bash
jetsonnanotaak.ipynb
```

Run all cells to:

Train the model (optional)

Load the trained model

Test predictions on images

🔁 How to Recreate This System From Scratch
Step 1: Prepare Dataset

Organize images like this:

```bash
training/
 ├── class_1/
 ├── class_2/
testing/
 ├── class_1/
 ├── class_2/
```

Step 2: Train the Model

- Use TensorFlow/Keras with:
- Image resizing (224x224)
- Normalization (rescale 1./255)
- CNN-based architecture

Step 3: Save the Model

```bash
model.save("traffic_sign_classifier.keras")
```

Step 4: Load & Predict
```bash
model = tf.keras.models.load_model("traffic_sign_classifier.keras")
```

🖥️ System Requirements

PC / Laptop (Windows, Linux, or macOS)
- Python 3.8+
- TensorFlow
- OpenCV
- Numpy

🚀 Future Improvements

- Real-time webcam detection
- More traffic sign classes
- GUI interface
- Model optimization for edge devices

📜 License

This project is for educational and experimental purposes.

Feel free to modify, improve, and expand it 👍