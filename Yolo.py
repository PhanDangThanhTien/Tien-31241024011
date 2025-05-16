import os
import cv2
import shutil
import matplotlib.pyplot as plt
from ultralytics import YOLO
from ultralytics.utils import SETTINGS

# Tránh lỗi ghi log
os.environ['YOLO_CACHE_DIR'] = '/kaggle/working/yolo_cache'
SETTINGS.update({'runs_dir': '/kaggle/working/ultralytics_logs'})

# XÓA ẢNH CŨ TRƯỚC KHI CHẠY LẠI
shutil.rmtree("/kaggle/working/bowls_cropped", ignore_errors=True)
shutil.rmtree("/kaggle/working/dishes_cropped", ignore_errors=True)
os.makedirs("/kaggle/working/bowls_cropped", exist_ok=True)
os.makedirs("/kaggle/working/dishes_cropped", exist_ok=True)

# Copy model detect bowl (YOLOv11n)
bowl_model_src = "/kaggle/input/model-yolo-and-model-cnn/yolo11n.pt"
bowl_model_dst = "/kaggle/working/yolo11n.pt"
shutil.copy(bowl_model_src, bowl_model_dst)
bowl_model = YOLO(bowl_model_dst)

# Copy model detect dish (YOLOv8)
dish_model_src = "/kaggle/input/model-yolo-and-model-cnn/model.pt"
dish_model_dst = "/kaggle/working/model.pt"
shutil.copy(dish_model_src, dish_model_dst)
dish_model = YOLO(dish_model_dst)

# Ảnh khay ăn đầu vào (sửa tại đây nếu cần)
image_path = "/kaggle/input/foodtestproject/z6582828713710_ced79b72a267840543f889cb7e593fae.jpg"
image_name = os.path.splitext(os.path.basename(image_path))[0]
img = cv2.imread(image_path)

# Detect bowl từ ảnh gốc
bowl_crop_dir = "/kaggle/working/bowls_cropped"
results = bowl_model.predict(source=image_path, conf=0.3)

for i, r in enumerate(results):
    for j, box in enumerate(r.boxes):
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        class_name = bowl_model.names[cls_id].lower()

        if "bowl" not in class_name:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        crop = img[y1:y2, x1:x2]
        crop_name = f"{image_name}_bowl_{j}_conf{conf:.2f}.jpg"
        crop_path = os.path.join(bowl_crop_dir, crop_name)
        cv2.imwrite(crop_path, crop)

        plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
        plt.title(f"CROP BOWL: {crop_name}")
        plt.axis("off")
        plt.show()

# Detect dish từ từng ảnh tô đã crop
dish_crop_dir = "/kaggle/working/dishes_cropped"
for fname in os.listdir(bowl_crop_dir):
    if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    bowl_path = os.path.join(bowl_crop_dir, fname)
    bowl_img = cv2.imread(bowl_path)
    bowl_name = os.path.splitext(fname)[0]

    results = dish_model.predict(source=bowl_path, conf=0.3)

    for i, r in enumerate(results):
        for j, box in enumerate(r.boxes):
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = dish_model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            crop = bowl_img[y1:y2, x1:x2]
            crop_name = f"{bowl_name}_dish_{class_name}_{j}_conf{conf:.2f}.jpg"
            crop_path = os.path.join(dish_crop_dir, crop_name)
            cv2.imwrite(crop_path, crop)