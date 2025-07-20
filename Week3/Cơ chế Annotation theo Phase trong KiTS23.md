# Mục tiêu của annotation nhiều phase

## Bộ dữ liệu KiTS23 được thiết kế để:

- Tăng dần chất lượng và độ chi tiết của phân đoạn (segmentation)

- Cho phép phân tích sự khác biệt giữa nhiều annotator (người chú thích)

- Dễ dàng xây dựng pipeline học theo pha (incremental learning) hoặc semi-supervised

## Cách tổ chức thư mục dữ liệu

- Sau khi tải bằng `kits23_download_data` hoặc `python -m kits23.download`, ta được cấu trúc thư mục như sau:
```
dataset/
└── case_00476/
    ├── imaging.nii.gz
    ├── segmentation.nii.gz  ← Mặt nạ tổng hợp (majority vote)
    └── instances/
        ├── kidney_instance-1_annotation-1.nii.gz
        ├── kidney_instance-1_annotation-2.nii.gz
        ├── kidney_instance-1_annotation-3.nii.gz
        ├── kidney_instance-2_annotation-1.nii.gz
        ├── ...
        ├── tumor_instance-1_annotation-1.nii.gz
        └── ...
```
## Giải thích ý nghĩa từng phần tên tệp
- Ví dụ: kidney_instance-1_annotation-2.nii.gz

| Thành phần     | Ý nghĩa                                                |
| -------------- | ------------------------------------------------------ |
| `kidney`       | Cấu trúc được phân đoạn (label)                        |
| `instance-1`   | Một đối tượng cụ thể (VD: thận trái hoặc phải)         |
| `annotation-2` | Người chú thích thứ 2 (hoặc phiên bản phân đoạn thứ 2) |

- Có thể có nhiều instance cho `kidney` (thận trái/phải), `tumor`, `cyst`,...

- Mỗi instance được `annotated` bởi tối đa 3 annotators, tạo ra 3 annotation phase.

## Tổng hợp nhiều annotation thành segmentation chính

- Tệp `segmentation.nii.gz` là **kết quả tổng hợp** từ nhiều annotation:

- Sử dụng **majority voting** hoặc `aggregate_case()` trong mã nguồn

- Được coi là “ground truth” chính thức để huấn luyện baseline

## Ứng dụng vào Incremental Learning

| Phase   | Nội dung có thể huấn luyện                   | Tệp dùng                |
| ------- | -------------------------------------------- | ----------------------- |
| Phase 1 | Chỉ dùng `annotation-1`, label ít & đơn giản | `*_annotation-1.nii.gz` |
| Phase 2 | Thêm `annotation-2`, có thể nhiều label hơn  | `*_annotation-2.nii.gz` |
| Phase 3 | Đầy đủ `annotation-3` – annotation cuối cùng | `*_annotation-3.nii.gz` |

- pipeline:

   - Pha 1: Huấn luyện với 1–2 lớp như kidney

   - Pha 2: Thêm tumor

   - Pha 3: Thêm cyst, refine hơn, tăng độ chi tiết

## Tóm lại

- Annotation theo `annotation-1`, `-2`, `-3` là **tăng dần mức độ hoàn thiện hoặc annotator khác nhau**

- Các tệp `.nii.gz` trong `instances/` đại diện cho **mỗi đối tượng anatomical**