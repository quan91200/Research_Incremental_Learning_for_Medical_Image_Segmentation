# BÁO CÁO TIẾN ĐỘ – TUẦN 4

**Sinh viên:** Nguyễn Minh Quân  
**MSSV:** 21010617  
**Lớp:** CNTT1  
**Khóa:** K15  
**Ngành:** Công nghệ thông tin  
**Cơ sở thực tập:** IDSAI Lab – Trường CNTT PHENIKAA  

**Thời gian thực tập:** 09/06 – 20/07/2025  
**Báo cáo tuần 4:** 30/06 – 06/07/2025  

---

## 🗂 NỘI DUNG CÔNG VIỆC

### ✅ Mục tiêu:
Áp dụng mô hình **Hermes** trong môi trường **Incremental Learning (IL)**,  
huấn luyện theo từng phase, lưu trữ kết quả và mô hình tương ứng.

---

### ✅ Kết quả thực hiện

1. **Xây dựng pipeline IL huấn luyện theo phase**
   - Tạo tập dữ liệu huấn luyện riêng cho từng phase dựa trên annotation KiTS23 (`annotation-1`, `annotation-2`, `annotation-3`)
   - Phase 1: chỉ thận (`kidney`)
   - Phase 2: thêm khối u (`tumor`)
   - Phase 3: đầy đủ nhãn

2. **Huấn luyện mô hình Hermes với dữ liệu tăng dần**
   - Sử dụng checkpoint đầu ra của mỗi phase làm đầu vào cho phase tiếp theo
   - Giữ lại token đã học và thêm token mới tương ứng với lớp mới

3. **Ghi nhận kết quả và đánh giá**
   - Theo dõi các chỉ số chính theo từng phase:  
     - Dice score, accuracy, loss  
     - Tốc độ hội tụ, hiệu quả giữ lại kiến thức cũ (IL hiệu quả hơn fine-tuning)
   - Quan sát hiệu suất khi tăng số class (class-increment)

4. **Lưu mô hình và log huấn luyện**
   - Checkpoint mô hình sau mỗi phase
   - Ghi log huấn luyện theo thời gian thực với `wandb`/`tensorboard` (nếu dùng)

---

## 📌 GHI CHÚ

- Mô hình Hermes chạy ổn định với dữ liệu CT (KiTS23), sẵn sàng áp dụng cho các bộ dữ liệu khác như AMOS, CHAOS
- Dự định trong tuần tới sẽ đánh giá hiệu năng mô hình, so sánh với baseline (huấn luyện toàn bộ/lặp lại) để kiểm tra ảnh hưởng của Incremental Learning

---

## 📌 NHẬN XÉT CỦA GIÁO VIÊN HƯỚNG DẪN

*… (để trống cho GVHD nhận xét) …*
