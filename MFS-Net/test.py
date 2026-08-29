from ultralytics.models import YOLO

if __name__ == "__main__":
    model = YOLO('runs/detect/trainv11s-seed3/weights/best.pt')
        
    model.val(data='ultralytics/cfg/database/CHIP.yaml')
