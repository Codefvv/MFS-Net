# MFS-Net

MFS-Net is proposed to solve problems of high similarity between defects and background, extreme defect scales and large variations in defect scales in chip substrate defect detection.
This repository contains the implementation for MFS‑Net for chip substrate surface defect detection.

## Repository Structure

```text
MFS-Net/
├── ultralytics/
│   ├── cfg/
│   │   ├── models/NET/          # Net.yaml, backbone.yaml, neck.yaml
│   │   └── database/            # CHIP.yaml, chipsurface.yaml, NEU_DET.yaml
│   ├── nn/modules/
│   │   ├── block.py             
│   │   └── conv.py              
│   └── ...                      
├── data/                        # dataset root
├── preweight/                   # pretrained weights
├── runs/                        # training and validation outputs
├── train.py                     # training entry point
├── test.py                      # evaluation entry point
├── tests/                       # Ultralytics test suite
└── README.md
```

## Environment

```bash
conda create -n mfsnet python=3.10 -y
conda activate mfsnet

# Install the PyTorch build matching your CUDA version first, then:
pip install numpy opencv-python pillow pyyaml matplotlib pandas scipy psutil tqdm requests
```

No MMDetection/MMCV/MMRotate installation is required. The custom blocks use the local `ConvModule` and
`DeformConv2d` implementations in `ultralytics/nn/modules/`.

A CUDA-capable GPU is recommended. The provided training script uses a single GPU with `imgsz=1024`.

## Dataset Preparation

The full industrial dataset used in this study is not publicly available due to confidentiality restrictions. A subset is openly available at <https://doi.org/10.5281/zenodo.19675661>. If you need the complete dataset for academic research, please contact the authors with a brief description of your intended use; reasonable requests will be considered.

Public datasets used or supported by the provided configurations:

| Dataset | Link |
| --- | --- |
| Chip surface defect dataset | <https://github.com/HiHiAllen/Chip-surface-defect-dataset> |
| NEU-DET | <https://ieee-dataport.org/documents/neu-det> (DOI: 10.21227/j84r-f770) |

The dataset configuration files are:

| Config | Classes |
| --- | --- |
| `ultralytics/cfg/database/CHIP.yaml` | damage, particle, dent |
| `ultralytics/cfg/database/chipsurface.yaml` | broken, crack, pollution |
| `ultralytics/cfg/database/NEU_DET.yaml` | crazing, inclusion, patches, pitted_surface, rolled-in_scale, scratches |

Set the `path` field in the YAML file to your local dataset root before training. Images and labels should follow the YOLO detection layout:

```text
data/
└── CHIP/
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── val/
    │   ├── images/
    │   └── labels/
    └── test/
        ├── images/
        └── labels/
```

Labels use the standard YOLO format: `class_id center_x center_y width height`, normalized to `[0, 1]`.

## Training

Set the model definition in `train.py` to the MFS-Net configuration:

Then run:

```bash
python train.py
```


## Evaluation

Update the checkpoint path in `test.py`, then run:

```bash
python test.py
```

The script evaluates the trained model on the validation set defined in the dataset YAML and reports standard detection metrics such as mAP50 and mAP50-95.
