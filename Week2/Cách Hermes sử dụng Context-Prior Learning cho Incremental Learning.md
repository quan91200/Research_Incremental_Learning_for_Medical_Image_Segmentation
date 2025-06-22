# Cơ chế Context-Prior Learning trong mô hình Hermes cho phân đoạn ảnh y tế

## 1. Các thành phần chính của Hermes và cơ chế context-prior learning

### `Task Prior` (Tiền tố nhiệm vụ):

* Mô hình `Hermes` xem mỗi nhiệm vụ phân đoạn (ứng với mỗi loại đối tượng **ROI** cần phân đoạn) như một nhiệm vụ nhị phân tách biệt, và gán cho mỗi nhiệm vụ một `token prior` riêng biệt được học trong quá trình train.

* Cụ thể, `Hermes` khởi tạo một bộ chứa các token nhiệm vụ (`task prior pool`) – một tập các vector/tham số học được, mỗi vector tương ứng với một lớp cần phân đoạn.

* Trong tập dữ liệu tổng hợp huấn luyện, `Hermes` xác định ID của nhiệm vụ (dựa trên **ROI** được gắn nhãn trong ảnh) làm `“oracle”` để chọn ra `token` nhiệm vụ tương ứng từ `pool` và điều kiện hóa mô hình trên token đó.

* Nhờ cơ chế này, `Hermes` có thể linh hoạt kết hợp các `token` nhiệm vụ tùy theo mục tiêu lâm sàng: 

* Ví dụ:

* Nếu ảnh yêu cầu phân đoạn gan và khối u, mô hình có thể lấy các `token prior` tương ứng với `“gan”` và `“khối u”` để sử dụng trong quá trình suy luận. Mỗi `token` nhiệm vụ học được đại diện cho đặc trưng của một lớp (**ROI**) dựa trên toàn bộ dữ liệu huấn luyện;

* Trong suy luận, `token` này sẽ được cập nhật dựa trên đặc trưng ảnh cụ thể (nhờ khối `fusion`) để tạo thành `prototype` hậu nghiệm phù hợp với trường hợp ảnh hiện tại.

* Cách thiết kế `token` nhiệm vụ như vậy giúp `Hermes` tận dụng kiến thức chuyên biệt cho từng cấu trúc giải phẫu và tái sử dụng kiến thức đó khi thêm nhiệm vụ mới mà không ảnh hưởng đến nhiệm vụ cũ.

### `Modality Prior` (tiền tố phương thức hình ảnh):
* Bên cạnh sự đa dạng về nhiệm vụ, dữ liệu y tế cũng rất đa dạng về phương thức chụp ảnh `(CT, MRI T1, MRI T2, PET, v.v.)`, mỗi loại có phân bố cường độ và nhiễu đặc trưng riêng. `Hermes` do đó bổ sung các `vector prior` cho từng `modality` nhằm cung cấp ngữ cảnh về loại ảnh.

* Cụ thể, mô hình khởi tạo một bộ chứa các `token modality` (`modality prior pool`) – ví dụ với 5 modality khác nhau sẽ có 5 tham số `vector` (hoặc một chuỗi `vector`) tương ứng.

* Mỗi `modality token` này được học trong quá trình `train` để mã hóa những đặc trưng điển hình của ảnh thuộc `modality` đó (ví dụ: ảnh CT có độ tương phản và nhiễu khác MRI).

* Khi mô hình nhận một ảnh đầu vào, dựa trên thông tin `modality` của ảnh (biết trước từ dữ liệu), `Hermes` sẽ chọn `token modality` phù hợp từ `pool` và ghép nó cùng với `token` nhiệm vụ đã chọn ở trên.

* Việc sử dụng `prior` theo `modality` giúp giảm độ phức tạp cho mô hình, vì model không phải tự học phân biệt tất cả mọi kiểu ảnh từ đầu mà đã có `“gợi ý”` về đặc thù hình ảnh qua `token` này. 

* *(Trong kiến trúc `Hermes`, mỗi `modality` có thể được biểu diễn bằng một hoặc một nhóm `token` độ dài `$l$`; thí nghiệm cho thấy độ dài `token modality` dài hơn cải thiện kết quả nhưng hiệu quả sẽ bão hòa dần – vì vậy họ chọn độ dài `$l=10$` cho mỗi `token modality` trong bài báo ).*

## 2. Hermes hỗ trợ Incremental Learning (học tăng dần) như thế nào?

### Mở rộng dễ dàng với nhiệm vụ mới bằng cách thêm `token prior`:

* Nhờ thiết kế token hóa nhiệm vụ, `Hermes` có khả năng mở rộng sang nhiệm vụ phân đoạn mới chỉ bằng cách thêm `token prior` mới, thay vì phải thay đổi kiến trúc hay thông số của các phần khác. 

* Cụ thể, khi xuất hiện một lớp mục tiêu mới (ví dụ một cơ quan hoặc loại tổn thương chưa có trong tập huấn luyện ban đầu), ta có thể khởi tạo một `token` nhiệm vụ mới cho lớp này và thêm vào `“pool”` `token` nhiệm vụ hiện có. Các `token prior` cũ vốn đã học cho các nhiệm vụ trước đó được giữ nguyên, do đó mô hình không bị ghi đè hay `“quên”` kiến thức cũ. 

* Trong giai đoạn huấn luyện bổ sung cho nhiệm vụ mới, `Hermes` chỉ cần điều kiện hóa trên `token mới` (và token `modality` tương ứng) – mô hình học cách phân đoạn đối tượng mới mà không làm suy giảm hiệu suất trên các đối tượng cũ.

* Điều này tương tự cách bác sĩ nội trú học thêm một bệnh mới nhưng không quên kiến thức về bệnh cũ, nhờ kho kiến thức đã tích lũy được giữ vững và chỉ bổ sung cái mới. 

### Huấn luyện riêng `token` mới hoặc `fine-tune` nhẹ khi dữ liệu mới ít: 

* Một lợi thế lớn của `Hermes` đối với học tăng dần là khả năng giữ cố định phần `backbone` và chỉ huấn luyện nhẹ nhàng những tham số liên quan đến nhiệm vụ mới. 

* Trong thí nghiệm `incremental learning`, các tác giả **đóng băng toàn bộ** `backbone` và các `token prior cũ`, sau đó chỉ `fine-tune token` nhiệm vụ mới (và các thành phần liên quan trực tiếp như `prototype` của nó) trên dữ liệu của nhiệm vụ mới.

* Nhờ backbone đã được huấn luyện đa nhiệm trước đó rất tổng quát và giàu khả năng biểu diễn, ngay cả khi dữ liệu mới rất ít (ví dụ 1% hay 10% dữ liệu của bộ mới), Hermes vẫn đạt được kết quả phân đoạn khá tốt cho nhiệm vụ mới.

* Quan trọng hơn, vì chỉ cập nhật một phần rất nhỏ tham số, phương pháp này hạn chế tối đa việc làm lệch các trọng số cũ, do đó tránh được quên sót (`catastrophic forgettin`g) – mô hình giữ được hiệu suất cao trên các nhiệm vụ đã học trước đó mà không cần huấn luyện lại chúng. 

* Đây là ưu điểm vượt trội so với cách `fine-tune` truyền thống, vốn thường cần `learning rate` rất thấp hoặc kỹ thuật đặc biệt để không làm hỏng hiệu suất nhiệm vụ cũ. 

### Hiệu quả IL so với `fine-tune` hoặc `pretrain` truyền thống: 

* Kết quả thực nghiệm cho thấy `Hermes` vượt trội các phương pháp truyền thống trong kịch bản `incremental learning`, đặc biệt khi dữ liệu mới khan hiếm. Chẳng hạn, trên bộ dữ liệu `Pancreas-Tumor` (MSD), `Hermes` (Hermes-R) khi chỉ `fine-tune token` mới đã đạt `Dice` tương đương hoặc cao hơn so với việc huấn luyện lại toàn bộ mô hình hay so với các phương pháp có điều kiện `một-hot` (DoDNet) hoặc dùng `CLIP prompt`.

* Điều này chứng tỏ kiến trúc `universal` của `Hermes` học được từ đa nguồn dữ liệu giúp tổng quát hóa tốt: `backbone` như một `model` nền tảng lưu giữ kiến thức chung, còn các `token prior` như `“cổng”` để kích hoạt kiến thức phù hợp cho từng nhiệm vụ. 

* So với `pre-training` truyền thống (huấn luyện mô hình chung rồi `fine-tune` cho từng `task`), cách tiếp cận của `Hermes` hiệu quả hơn vì mô hình học đồng thời đa nhiệm ngay từ đầu, các nhiệm vụ hỗ trợ lẫn nhau trong quá trình học.

* Nhờ đó, khi thêm nhiệm vụ mới, `Hermes` chỉ cần **thêm một lượng rất nhỏ tham số** nhưng vẫn **nhanh chóng thích nghi**, trong khi vẫn **giữ vững hiệu năng trên nhiệm vụ cũ** – một đặc tính rất quan trọng trong các ứng dụng thực tế nơi không muốn phải huấn luyện lại mô hình từ đầu khi có dữ liệu mới.

## 3. Đối chiếu lý thuyết với triển khai mã nguồn GitHub (`yhygao/universal-medical-image-segmentation`)

### Các module chính hiện thực Task Prior, Modality Prior và Fusion:
* Trong mã nguồn chính thức của `Hermes` (được cung cấp trên `GitHub`), các khái niệm `token prior` được hiện thực dưới dạng tham số học được trong mô hình. Cụ thể, code khởi tạo một ma trận `embedding` cho `task prior` với kích thước `[Số_nhiệm_vụ × Chiều_dài_token]` – tương ứng với `task prior pool` chứa các `vector` cho từng nhiệm vụ.

* Tương tự, một ma trận `embedding` cho `modality prior` được tạo với kích thước `[Số_modalities × l × Chiều_dài_token]` (với `$l$` là số `token` dành cho mỗi `modality`, có thể `$l=1$` hoặc lớn hơn).

* Những `embedding` này thường được khai báo như `nn.Parameter` hoặc `nn.Embedding` trong lớp mô hình, và được khởi tạo ngẫu nhiên rồi học dần trong quá trình train. Bên cạnh đó, module **Prior Fusion** được cài đặt dựa trên` attention đa đầu` (multi-head attention) hoặc `cross-attention` hai chiều. Trong trường hợp `backbone` là **CNN** (ResUNet), code chèn một lớp `cross-attention` hai chiều sau mỗi khối `conv` của `encoder` ở các mức `downsample (4×, 8×, 16×)`.

* Module `cross-attention` này có thể được định nghĩa như một lớp riêng (ví dụ `BiCrossAttention`) nhận đầu vào gồm tập `token` và `feature map`, và trả ra `feature map` cùng `token` đã cập nhật. Nếu `backbone` là **Transformer** (như **MedFormer**), code sẽ hợp nhất trực tiếp các `token prior` vào các lớp `self-attention` của **transformer** (bằng cách nối chuỗi `token` vào `sequence input`).

* Tất cả những thành phần này (`backbone` + `token pool` + `fusion module`) được đóng gói trong lớp mô hình `Hermes` (ví dụ có thể đặt tên là `HermesModel`), cho phép tối ưu chung cả `backbone` và các `token priors` trong quá trình huấn luyện.

### Tổ chức `“token pool”`, cơ chế chọn `token` và luồng forward: 

* Mã nguồn được tổ chức sao cho `dataloader` cung cấp cả ảnh, nhãn và thông tin oracle (ID nhiệm vụ, loại modality) cho mỗi mẫu. Trong hàm forward của mô hình, dựa trên các ID này, mô hình sẽ truy xuất các `token` phù hợp từ `pool`. Ví dụ giả sử trong code có các biến `self.task_prior_pool` và `self.modality_prior_pool` là các ma trận `embedding`, thì khi forward một batch ảnh, mô hình thực hiện:

```
# Pseudocode minh họa cách chọn token prior theo ID
task_token = self.task_prior_pool[task_id]         # vector token cho nhiệm vụ hiện tại
mod_token  = self.modality_prior_pool[modality_id] # vector (hoặc chuỗi vector) cho modality ảnh
prior_tokens = concat(task_token, mod_token)       # hợp nhất token nhiệm vụ và token modality
```

* Ở bước tiếp theo, **feature map** $X$ từ `backbone` và chuỗi `prior_tokens` ở trên sẽ được đưa vào module **prior fusion**. Module này thực hiện `cross-attention` để tạo ra `posterior_tokens` (chính là `token prior` đã cập nhật thành token hậu nghiệm `$P'$`) và **feature map đã được truyền prior $F'$**

* Code có thể triển khai bước này như:
```
posterior_tokens, F_prime = self.prior_fusion(prior_tokens, X)
```

* Sau đó, `posterior_tokens` được đưa qua một MLP (thường gồm một vài lớp Linear) để chuyển thành **posterior prototypes** – mỗi token hậu nghiệm cho ra một `prototype` vector độ dài bằng số kênh của feature map decoder.

* Giả sử `self.prototype_mlp` là module MLP đó, ta có:
```
posterior_prototypes = self.prototype_mlp(posterior_tokens)  
# posterior_prototypes: tensor kích thước [Tổng_số_token_prior × C_feat]
```

* Cuối cùng, mã nguồn tính đầu ra phân đoạn bằng cách tính tích trong giữa mỗi `prototype` và từng vị trí trên **feature map** $F'$ (thực chất là một phép nhân ma trận giữa `prototype` với `tensor` đặc trưng) rồi đưa qua `sigmoid` để được xác suất. Nếu coi mỗi `prototype` tương ứng một lớp, thì kết quả là một bản đồ xác suất cho lớp đó (cùng kích thước không gian với ảnh gốc). Mã giả cho bước này có thể là:

```
# Sử dụng posterior_prototypes làm kernel để tính logit đầu ra cho mỗi lớp
logits = torch.einsum('n c, b c h w -> b n h w', posterior_prototypes, F_prime) 
pred = torch.sigmoid(logits)  # xác suất phân đoạn cho mỗi lớp (nhiệm vụ)
```

* *(Trong trường hợp `Hermes` coi mỗi lần chỉ có ***một nhiệm vụ (một ROI) active*** cho mỗi mẫu – như mô hình được huấn luyện theo kiểu từng lớp một – thì `posterior_tokens` sẽ chỉ chứa `token` cho ***ROI*** đó, và đầu ra ***pred*** sẽ là bản đồ nhị phân tương ứng. Với ảnh chứa nhiều ***ROI*** cần phân đoạn đồng thời, `prior_tokens` có thể chứa nhiều `token` nhiệm vụ, khi đó mô hình tính ra nhiều bản đồ nhị phân cho các ***ROI*** tương ứng.)*

* Quy trình trên được lặp tại các tầng khác nhau nếu có fusion đa tầng. Code sẽ thu thập các `prototype` từ mỗi tầng, có thể nối chúng lại và qua một MLP cuối cùng để ra kết quả `segmentation` tổng hợp.

* Nhìn chung, luồng xử lý (forward pass) trong code `Hermes` bám sát mô tả lý thuyết: 

* (1) trích xuất đặc trưng ảnh
* (2) chọn token nhiệm vụ & modality phù hợp 
* (3) thực hiện attention giữa token và đặc trưng để trộn ngữ cảnh (prior fusion)
* (4) chuyển token hậu nghiệm thành bộ trọng số phân loại (prototype)
* (5) áp dụng chúng để tính kết quả phân đoạn

### Bổ sung nhiệm vụ mới hoặc huấn luyện tăng dần trong code:
* Mặc dù mã nguồn hiện tại chưa cung cấp sẵn hàm tiện ích để thêm nhiệm vụ mới, ta có thể dễ dàng thực hiện bằng cách mở rộng `token pool`. Ví dụ, để thêm một nhiệm vụ với ID mới (giả sử mô hình ban đầu có **42 task tokens**, muốn thêm **task thứ 43**), ta có thể tạo một `vector` tham số mới và nối vào `task_prior_pool`. Mã minh họa:

```
# Giả sử model.task_prior_pool là nn.Parameter kích thước [42 × C]. 
# Thêm một token mới (1 × C) cho nhiệm vụ mới:
new_token = torch.nn.Parameter(torch.randn(1, C))
model.task_prior_pool = torch.nn.Parameter(torch.cat([model.task_prior_pool.data, new_token], dim=0))
```

* Sau đó, đóng băng các tham số `backbone` và `token cũ`, chỉ **huấn luyện token mới** (và có thể lớp MLP cuối) trên dữ liệu nhiệm vụ mới. Thực nghiệm của tác giả cho thấy cách làm này giúp `Hermes` đạt **hiệu năng gần bằng huấn luyện full model**, đồng thời **giữ nguyên được kết quả trên các nhiệm vụ cũ**.

* Như vậy, cấu trúc module tách biệt của `Hermes` (`backbone` chung và các `token prior` riêng lẻ) rất thuận lợi cho **Incremental Learning**: việc thêm kiến thức mới tương đương với mở rộng “bộ nhớ” của model bằng một ô nhớ mới (token mới), thay vì phải ghi đè hoặc làm xáo trộn những gì đã học. Điều này xác thực triết lý thiết kế của `Hermes` và được kiểm chứng bởi mã nguồn và kết quả thực nghiệm: mô hình có **tính linh hoạt và mở rộng cao**, phù hợp với mục tiêu xây dựng **mô hình nền tảng (foundation model)** cho phân đoạn y tế phổ quát.

## Tóm lại

- Sự kết hợp giữa thiết kế lý thuyết và triển khai thực tế của `Hermes` cho thấy mô hình đã giải quyết hiệu quả bài toán phân đoạn ảnh y tế đa nhiệm và học tăng dần. Các `task prior token` và `modality token` được mã nguồn cài đặt rõ ràng, đóng vai trò như những “hướng dẫn” ngữ cảnh giúp mô hình tập trung vào mục tiêu cần phân đoạn, còn **prior fusion module** thực hiện nhiệm vụ hòa trộn thông tin linh hoạt giữa kiến thức nền và dữ liệu ảnh mới. Nhờ đó, `Hermes` vừa đạt **hiệu suất SOTA trên nhiều bộ dữ liệu khác nhau**, vừa cho thấy **khả năng mở rộng và tổng quát hóa vượt trội** (transfer learning, incremental learning) trong lĩnh vực phân đoạn ảnh y tế.

## Nguồn tham khảo

- Các thông tin trên được tổng hợp và đối chiếu từ bài báo gốc của Hermes (CVPR 2024) (paper)[https://openaccess.thecvf.com/content/CVPR2024/supplemental/Gao_Training_Like_a_CVPR_2024_supplemental.pdf#:~:text=,4%C3%97%2C%208%C3%97%2C%20and%2016%C3%97] và mã nguồn chính thức trên GitHub của nhóm tác giả. (github)[https://github.com/yhygao/universal-medical-image-segmentation]