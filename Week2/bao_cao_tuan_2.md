
# BÁO CÁO TIẾN ĐỘ – TUẦN 2

**Sinh viên:** Nguyễn Minh Quân  
**MSSV:** 21010617  
**Lớp:** CNTT1  
**Khóa:** K15  
**Ngành:** Công nghệ thông tin  
**Cơ sở thực tập:** IDSAI Lab – Trường CNTT PHENIKAA  

**Thời gian thực tập:** 09/06 – 20/07/2025  
**Báo cáo tuần 2:** 16/06 – 22/06/2025  

---

## NỘI DUNG CÔNG VIỆC

### ✅ Mục tiêu:
Đọc và phân tích mô hình Hermes từ bài báo “Training Like a Medical Resident”; tìm hiểu cách mô hình xử lý heterogeneity trong medical segmentation.

### ✅ Kết quả:

#### 1. Vấn đề đang giải quyết

Trong bối cảnh phân đoạn ảnh y tế, dữ liệu thường rất không đồng nhất (đa dạng về vùng cơ thể, bệnh lý và loại ảnh y khoa như CT, MRI…).  
Việc xây dựng các mô hình riêng lẻ cho từng nhiệm vụ rất tốn công sức và khó mở rộng.

→ Mục tiêu là tìm hiểu mô hình **Hermes** – một giải pháp phân đoạn ảnh y tế phổ quát (Universal Medical Image Segmentation),  
có khả năng học đa nhiệm và bổ sung nhiệm vụ mới mà **không quên kiến thức cũ** (Incremental Learning – IL).

#### 2. Phương pháp giải quyết

Mô hình Hermes sử dụng cơ chế **context-prior learning** với 3 thành phần chính:

- **Task Prior**:  
  Gán mỗi nhiệm vụ (VD: phân đoạn gan, tim, khối u...) một vector học được (token prior), giúp mô hình hiểu đang cần phân đoạn đối tượng gì.

- **Modality Prior**:  
  Với mỗi loại ảnh y khoa (CT, MRI, PET…), Hermes học một **modality token** giúp mô hình thích nghi với tính chất hình ảnh riêng.

- **Prior Fusion**:  
  Kết hợp các token prior (task + modality) với đặc trưng ảnh từ backbone thông qua **attention hai chiều**, tạo ra posterior prototype để phân đoạn ảnh.

➡️ Trong học tăng dần, Hermes chỉ cần **thêm token mới** cho nhiệm vụ mới mà không phải huấn luyện lại toàn bộ mô hình.  
→ Điều này giúp mở rộng dễ dàng và **tránh hiện tượng quên kiến thức cũ (catastrophic forgetting)**.

#### 3. Kết quả đạt được

- Hiểu chi tiết cơ chế **context-prior learning** của Hermes qua bài báo *Training Like a Medical Resident (CVPR 2024)* và mã nguồn trên GitHub:  
  [`yhygao/universal-medical-image-segmentation`](https://github.com/yhygao/universal-medical-image-segmentation)

- Biết cách Hermes xử lý dữ liệu không đồng nhất thông qua token ngữ cảnh.

- Nắm được cách mô hình hỗ trợ **Incremental Learning** hiệu quả, không cần fine-tune toàn bộ mô hình.

- So với Transfer Learning truyền thống, Hermes tỏ ra hiệu quả hơn, đặc biệt khi dữ liệu mới rất ít (1–10%).

---

## 📌 NHẬN XÉT CỦA GIÁO VIÊN HƯỚNG DẪN

*… (để trống cho GVHD nhận xét) …*
