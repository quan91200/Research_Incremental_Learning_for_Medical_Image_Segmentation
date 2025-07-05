
# BÁO CÁO TIẾN ĐỘ – TUẦN 1

**Sinh viên:** Nguyễn Minh Quân  
**MSSV:** 21010617  
**Lớp:** CNTT1  
**Khóa:** K15  
**Ngành:** Công nghệ thông tin  
**Cơ sở thực tập:** IDSAI Lab – Trường CNTT PHENIKAA  

**Thời gian thực tập:** 09/06 – 20/07/2025  
**Báo cáo tuần 1:** 09/06 – 15/06/2025  

---

## 🗂 NỘI DUNG CÔNG VIỆC

### ✅ Mục tiêu:
Nghiên cứu lý thuyết về Incremental Learning (IL)  
Hiểu rõ nền tảng IL và vai trò trong thị giác máy tính, phân đoạn ảnh y tế  
So sánh IL với Transfer Learning

---

## 🧠 VẤN ĐỀ ĐẶT RA

Trong thị giác máy tính, đặc biệt là phân đoạn ảnh y tế, dữ liệu thường đến **theo từng giai đoạn**, ví dụ:

- Ảnh từ bệnh viện mới (domain khác)
- Dữ liệu về cơ quan/bệnh lý mới (class mới)
- Nguồn ảnh khác nhau (CT, MRI…)

🔸 Các mô hình học sâu truyền thống:
- Cần huấn luyện lại toàn bộ mô hình khi có dữ liệu mới
- Dễ quên kiến thức cũ (*catastrophic forgetting*)
- Khó triển khai thực tế do chi phí cao, mất thời gian

---

## 🔍 PHƯƠNG PHÁP GIẢI QUYẾT

### ✳️ Incremental Learning (IL)

Học liên tục theo từng **phase** (task), giúp giữ lại kiến thức cũ mà vẫn học được mới

#### Các thách thức:

- **Catastrophic Forgetting**: Mô hình quên lớp cũ sau khi học lớp mới
- **Dual Imbalance**:
  - *Inter-phase*: Lớp cũ < lớp mới
  - *Intra-phase*: Lớp phổ biến > lớp hiếm
- **Stability – Plasticity Dilemma**:
  - *Stability*: Giữ kiến thức cũ
  - *Plasticity*: Học cái mới

#### Phương pháp xử lý từ bài báo *Training Like a Medical Resident (CVPR 2024)*:

- **Gradient Reweighting**: Cân bằng gradient để giảm thiên lệch
- **DAKD (Distribution-Aware Knowledge Distillation)**:  
  Điều chỉnh trọng số loss theo tỷ lệ dữ liệu đã mất → giữ lại lớp cũ tốt hơn

---

### 🔄 So sánh IL vs Transfer Learning

| Tiêu chí             | Incremental Learning     | Transfer Learning         |
|----------------------|--------------------------|---------------------------|
| Học mới              | Tuần tự, từng lớp        | Một lần, toàn bộ          |
| Dữ liệu              | Theo giai đoạn           | Cần đầy đủ từ đầu          |
| Thách thức chính     | Forgetting, Imbalance    | Domain mismatch           |
| Tính thực tiễn       | Cao khi dữ liệu cập nhật | Tốt cho pretrain + finetune |

---

## ✅ KẾT QUẢ ĐẠT ĐƯỢC

- Đọc hiểu rõ khái niệm **Incremental Learning (IL)** và các phân loại:
  - class-incremental
  - task-incremental
  - domain-incremental

- Phân tích sâu các thách thức: catastrophic forgetting, dual imbalance

- Tổng hợp lại 2 cơ chế chính: **Gradient Reweighting** & **DAKD**

- So sánh chi tiết IL với Transfer Learning từ lý thuyết đến ứng dụng thực tế

---

## 📌 NHẬN XÉT CỦA GIÁO VIÊN HƯỚNG DẪN

*… (để trống cho GVHD nhận xét) …*
