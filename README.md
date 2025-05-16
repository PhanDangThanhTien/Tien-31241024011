# Tien-31241024011
1.Ứng dụng AI trong nhận diện món ăn và tính tiền tự động tại căn tin

Các hệ thống AI như nhận diện vật thể và tính giá sản phẩm hiện đã phổ biến tại các cửa hàng tiện lợi hiện đại. Tuy nhiên, những giải pháp này thường dựa vào việc quét mã vạch hoặc nhận diện các sản phẩm có bao bì sẵn, điều vốn không phù hợp với môi trường căn tin – nơi món ăn được chế biến tại chỗ, thay đổi mỗi ngày và không gắn nhãn.

Trong bối cảnh đó, nhóm nghiên cứu đã phát triển một hệ thống thông minh sử dụng camera và mô hình học sâu để nhận diện trực tiếp các món ăn trên khay cơm, từ đó xác định tên món và giá tiền tương ứng. Hệ thống hoạt động hoàn toàn tự động, không cần can thiệp thủ công, giúp giảm thời gian thanh toán, hạn chế sai sót và nâng cao trải nghiệm tại các căn tin trường học, bệnh viện hay khu công nghiệp.

Hệ thống vận hành dựa trên sự tích hợp giữa hai công nghệ cốt lõi: YOLO – một giải pháp phát hiện vật thể hiện đại, đảm nhiệm việc xác định chính xác từng món ăn trên khay, và CNN – mạng nơ-ron tích chập được huấn luyện chuyên biệt, có khả năng phân biệt chính xác nhiều loại món ăn khác nhau. Sau khi hoàn tất quá trình nhận diện và phân loại, hệ thống sẽ tự động tra cứu giá từng món trong cơ sở dữ liệu đã thiết lập và tính toán tổng chi phí. Để tối ưu trải nghiệm người dùng, hệ thống còn tạo ra mã QR dẫn đến giao diện thanh toán mô phỏng, đơn giản và trực quan.

2. Hướng dẫn cài đặt:

Bước 1: Cài đặt Python 3.8 trở lên trong trang chính thức https://www.python.org/downloads/

Bước 2: Cài đặt Visual Studio Code 

Bước 3: Tải mã nguồn dự án từ GitHub hoặc copy vào máy.

Bước 4: Mở thư mục dự án bằng Visual Studio Code

Bước 5: Tạo ra môi trường ảo 

• Mở terminal và chạy lệnh: python -m venv venv

• Kích hoạt môi trường:

 Windows: .\venv\Scripts\activate o macOS/Linux: source venv/bin/activate

Bước 6: Cài đặt các thư viện cần thiết bằng lệnh: pip install -r requirements.txt

3. Hướng dẫn sử dụng:

Bước 1: Đảm bảo mô hình CNN đã được huấn luyện và lưu với tên model.h5 trong thư mục dự án.

Bước 2: Chạy chương trình bằng lệnh: python app.py

Bước 3: Giao diện xuất hiện, cho phép chọn ảnh khay cơm.

Bước 4: Hệ thống thực hiện các bước:

• Phát hiện món ăn bằng YOLO.

• Phân loại từng món bằng CNN.

• Hệ thống đưa ra các món ăn và giá cả.
