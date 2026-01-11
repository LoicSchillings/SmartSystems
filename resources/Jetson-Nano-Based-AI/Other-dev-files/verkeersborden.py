from edge_impulse_linux.image import ImageImpulseRunner
import cv2

model_path = "/home/jetsonnanoo/SmartSystemsBitchhhh/inebdg-project-1-linux-aarch64-v2.eim"

runner = ImageImpulseRunner(model_path)
runner.init()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
print(cap.isOpened())
      
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        features, _ = runner.get_features_from_image(frame)
        result = runner.classify(features)

        preds = result["result"]["classification"]
        if preds:
            label = max(preds, key=preds.get)
            confidence = preds[label]

            if confidence > 0.7:
                print(f"{label} ({confidence:.2f})")

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    cap.release()
    runner.stop()
