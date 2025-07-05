
# KẾ HOẠCH THỰC TẬP TẠI CƠ SỞ

**Sinh viên:** Nguyễn Minh Quân  
**MSSV:** 21010617  
**Lớp:** CNTT1  
**Khóa:** K15  
**Hệ:** Chính quy  
**Ngành:** Công nghệ thông tin  
**Tên cơ sở thực tập:** Lab Nghiên cứu liên ngành về Khoa học dữ liệu và trí tuệ nhân tạo (IDSAI Lab)

---

## 📆 KẾ HOẠCH THEO TUẦN

| Tuần | Thời gian | Nội dung/Kế hoạch thực tập | Kết quả thực hiện | Ghi chú |
|------|-----------|-----------------------------|--------------------|---------|
| **1** | 09/06/2025 – 15/06/2025 | Nghiên cứu lý thuyết về Incremental Learning (IL) | Hiểu rõ nền tảng IL và vai trò trong thị giác máy tính và phân đoạn ảnh y tế. So sánh IL với Transfer Learning |  |
| **2** | 16/06/2025 – 22/06/2025 | Đọc và phân tích mô hình Hermes từ bài báo “Training Like a Medical Resident”; tìm hiểu cách mô hình xử lý heterogeneity trong segmentation | Hiểu cách Hermes sử dụng context-prior learning cho IL: task prior, modality prior, prior fusion. Dùng GitHub: `yhygao/universal-medical-image-segmentation` |  |
| **3** | 23/06/2025 – 29/06/2025 | Phát triển bộ dữ liệu phù hợp để mô phỏng môi trường Incremental Learning trong phân đoạn ảnh y tế | Chia dataset thành nhiều phase tăng dần số lớp (label), có annotation rõ ràng từng phase. AMOS, CHAOS, KiTS… là nguồn dữ liệu phù hợp |  |
| **4** | 30/06/2025 – 06/07/2025 | Áp dụng mô hình Hermes trong môi trường Incremental Learning, huấn luyện theo từng phase, lưu trữ kết quả và mô hình | Chạy thành công IL pipeline, ghi nhận kết quả theo từng phase, quan sát hiệu suất mô hình khi tăng class. Điều chỉnh code Hermes để huấn luyện tuần tự |  |
| **5** | 07/07/2025 – 13/07/2025 | Đánh giá mô hình Hermes trong thiết lập Incremental Learning, so sánh với baseline (full training / fine-tuning) | Có đồ thị Dice, ACC, Forgetting Rate theo từng phase, đánh giá ảnh hưởng của IL trong segmentation. Có thể thử thêm kỹ thuật từ bài báo Gradient Reweighting |  |
| **6** | 14/07/2025 – 20/07/2025 | Đề xuất cải tiến mô hình cho bài toán phân đoạn ảnh y tế trong môi trường IL, viết báo cáo tổng kết nghiên cứu và kết quả thực nghiệm | Báo cáo gồm tổng quan, thiết kế, kết quả, đánh giá, đề xuất mở rộng. Có thể đề xuất kết hợp với kỹ thuật Re-weighting từ bài He (CVPR'24) |  |

---

**Hà Nội, ngày 10 tháng 06 năm 2025**  

**Giảng viên hướng dẫn**  
(Ký, ghi rõ họ tên)

**Sinh viên thực tập**  
(Ký, ghi rõ họ tên)  
**Nguyễn Minh Quân**
