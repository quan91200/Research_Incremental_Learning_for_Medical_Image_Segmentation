
import os
import numpy as np
import nibabel as nib
from tqdm import tqdm

# Đường dẫn tới folder chứa case_00000, case_00001, ...
input_dir = "/home/cobham/Research_Incremental_Learning_for_Medical_Image_Segmentation//Dataset/kits23/dataset"
output_img_dir = "/home/cobham/Research_Incremental_Learning_for_Medical_Image_Segmentation/Dataset/kits23_IL/phase1/kits"
output_lbl_dir = "/home/cobham/Research_Incremental_Learning_for_Medical_Image_Segmentation/Dataset/kits23_IL/phase1/labels"

os.makedirs(output_img_dir, exist_ok=True)
os.makedirs(output_lbl_dir, exist_ok=True)

cases = sorted(os.listdir(input_dir))
for idx, case in enumerate(tqdm(cases)):
    case_path = os.path.join(input_dir, case)
    img_path = os.path.join(case_path, "imaging.nii.gz")
    lbl_path = os.path.join(case_path, "segmentation.nii.gz")

    # Load .nii.gz
    img = nib.load(img_path).get_fdata()
    lbl = nib.load(lbl_path).get_fdata()
    
    # Save dưới dạng .npy
    np.save(os.path.join(output_img_dir, f"{idx}.npy"), img.astype(np.float32))
    np.save(os.path.join(output_lbl_dir, f"{idx}.npy"), lbl.astype(np.uint8))

    print(f"✔ Saved: {idx}.npy")
