from ultralytics.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld

if __name__ == "__main__":
    model = YOLO('ultralytics/cfg/models/NET/NET.yaml')
    model.load(r'preweight/yolov8s.pt')  

    model.train(data='ultralytics/cfg/database/CHIP.yaml',  
                cache=True,  
                imgsz=1024,  
                epochs=400,  
                #batch=16,  
                batch=8,  
                close_mosaic=10,  
                workers=8,  
                patience=50,  
                device='0',  
                # optimizer='SGD',  
                optimizer='SGD',
                seed=3,
                )
