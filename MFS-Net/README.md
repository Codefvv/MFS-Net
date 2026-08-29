Project Overview
This repository contains the implementation for MFS‑Net for surface defect detection.
Project Structure
plaintext
├── data/                # Place your dataset here
├── ultralytics/
│   └── models/          # Model weight files are stored here
├── train.py             # Model training script
├── test.py              # Model evaluation & testing script
├── predict.py           # Model inference script
└── README.md

Train the model
python train.py
You can modify training hyper‑parameters inside train.py or pass arguments via command line.

Test / Evaluate the trained model
python test.py
This script computes mAP50, mAP50‑95 and other evaluation metrics on test set.
Make sure the trained model weights are placed under runs/.

Run inference
python predict.py
Used for image inference. You can adjust input image path, confidence threshold in this script.

Dataset Setup
Put dataset images and annotations inside the data/ directory.
Create your dataset configuration yaml under ultralytics/cfg/database and make sure file paths in yaml are correctly set.