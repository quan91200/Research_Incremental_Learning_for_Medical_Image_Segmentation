# Tóm tắt ngắn gọn bài báo Hermes về Universal Medical Image Segmentation (CVPR 2024)
[openaccess.thecvf.com](openaccess.thecvf.com)

## Mục tiêu và bối cảnh: 

-Hermes hướng tới xây dựng một mô hình phân đoạn ảnh y tế “phổ quát” có thể xử lý nhiều nhiệm vụ và loại ảnh khác nhau trong cùng một mạng, thay vì huấn luyện riêng lẻ từng mô hình cho từng nhiệm vụ như truyền thống.

- Cách tiếp cận này lấy cảm hứng từ chương trình đào tạo bác sĩ X quang, khi thực tập sinh luân khoa qua nhiều bộ ảnh (vùng cơ thể, bệnh lý, `modality`) để tích lũy kiến thức nền tảng rộng.
.
### Task prior: Mỗi nhiệm vụ phân đoạn (ví dụ một cơ quan hoặc loại tổn thương cụ thể) được gán một vector ngữ cảnh học được đại diện cho tác vụ đó

- Tập hợp các `task prior` này giúp mô hình `Hermes` linh hoạt chuyển đổi hoặc kết hợp nhiều nhiệm vụ phân đoạn khác nhau trong một mô hình duy nhất tùy theo mục tiêu lâm sàng.
.
### Modality prior: 

- Tương tự, mỗi loại ảnh y khoa (CT, MRI T1/T2, PET, cine MRI, v.v.) đều có các vector ngữ cảnh theo `modality` học được để đặc trưng hóa những khác biệt về đặc tính hình ảnh (cường độ, nhiễu, cấu trúc) của `modality` đó
- Những `modality prior` này được nối cùng với `task prior` tương ứng của ảnh, giúp Hermes thích nghi với dữ liệu đa dạng đa modal một cách hiệu quả

### Prior fusion: 

- Module kết hợp prior sử dụng cơ chế `attention` hai chiều để trộn lẫn các token ngữ cảnh (`task` & `modality`) với đặc trưng ảnh từ `backbone`

- Quá trình này đồng thời cập nhật các `prior` theo ngữ cảnh từng ảnh và truyền kiến thức nền tảng vào đặc trưng thị giác, tạo ra các `prototype` phân đoạn cuối cùng cho từng lớp cần nhận diện

## Hiệu quả phân đoạn đa nhiệm: 

- Nhờ khai thác tính đa dạng và điểm chung giữa các nhiệm vụ, `Hermes` đạt hiệu suất rất cao trên bộ dữ liệu huấn luyện hợp nhất (11 dataset, 2.438 ảnh 3D thuộc 5 `modality`) với một mô hình duy nhất, vượt trội so với các mô hình chuyên biệt huấn luyện riêng lẻ.

- Mô hình chung này đạt độ chính xác `SOTA` (Dice trung bình cao hơn) trên tất cả các tập dữ liệu kiểm thử và cho thấy khả năng mở rộng mô hình tốt hơn – khi tăng kích thước `backbone`, hiệu năng `Hermes` cải thiện đáng kể, trái ngược với mô hình truyền thống dễ bão hòa do dữ liệu đơn nguồn hạn chế.


## Tổng quát hóa và thích ứng:

- Hermes thể hiện khả năng tổng quát hóa và thích ứng vượt trội sang nhiệm vụ mới. Cụ thể, khi `fine-tune` (`transfer learning`) sang một bài toán phân đoạn khác (ví dụ phân đoạn tụy và khối u), `Hermes` đạt kết quả cao hơn rõ rệt so với khởi tạo hoặc tiền huấn luyện từ từng bộ dữ liệu đơn lẻ, kể cả trong trường hợp dữ liệu mới rất ít (1-10% bộ huấn luyện).

- Đồng thời, `Hermes` hỗ trợ học bổ sung nhiệm vụ (`incremental learning`) hiệu quả: có thể thêm nhiệm vụ mới bằng cách tinh chỉnh nhẹ các token ngữ cảnh mà vẫn giữ vững kiến thức về các nhiệm vụ cũ, đạt độ chính xác cao hơn các phương pháp so sánh, đặc biệt ở kịch bản dữ liệu hạn chế.

- Mô hình huấn luyện đa nhiệm cũng cho thấy độ bền vững khi áp dụng trực tiếp lên dữ liệu chưa thấy: khi thử nghiệm trên bộ dữ liệu khác vùng (ví dụ huấn luyện trên `StructSeg` và đánh giá trên `SegTHOR`), `Hermes` vẫn dẫn đầu về kết quả so với mô hình chỉ huấn luyện đơn nhiệm.

- Kết quả nổi bật & ứng dụng thực tế: `Hermes` không chỉ đạt `SOTA` trên mọi tập dữ liệu thử nghiệm mà các prior học được còn phản ánh đúng mối quan hệ phức tạp giữa các cơ quan và giữa các `modality`, phù hợp với hiểu biết giải phẫu và nguyên lý hình ảnh y khoa thực tế.

- Với phương pháp học ngữ cảnh ưu tiên độc đáo này, `Hermes` mở ra tiềm năng xây dựng các mô hình nền tảng cho phân đoạn ảnh y tế, nơi một mô hình chung có thể phục vụ nhiều nhiệm vụ chẩn đoán khác nhau, giảm nhu cầu phát triển và bảo trì hàng loạt mô hình riêng lẻ trong lâm sàng.