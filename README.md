# Đồ án cuối kỳ môn Nhập môn khoa học dữ liệu
## Thông tin nhóm 6

| **STT** | **Họ và tên** | **MSSV** | 
|-------|---------------|---------|
| 1     | Nguyễn Thành Đức | 22120070 | 
| 2     | Đinh Viết Lợi | 22120188 |  |
| 3     | Nguyễn Trần Lợi | 22120190 |
| 4     | Nguyễn Nhật Long | 22120194 |
| 5     | Nguyễn Tiến Quốc | 22120300 |


---
# Tổng quan đề tài

* Sản phẩm là đồ án được yêu cầu bởi giảng viên thực hành Lê Nhựt Nam thuộc lớp Nhập môn Khoa học dữ liệu lớp CQ2024/21 trường Đại học Khoa học Tự Nhiên. Đồ án là một tiêu chí đánh giá và ứng dụng quá trình học tập tại lớp trong học kì I năm học 2024-2025.

* Dự đoán mức lương việc làm là một nhu cầu quan trọng trong thị trường lao động hiện đại, giúp ứng viên chuẩn bị tốt hơn và hỗ trợ nhà tuyển dụng đưa ra chính sách lương cạnh tranh. Mức lương bị ảnh hưởng bởi nhiều yếu tố như kỹ năng, kinh nghiệm, vị trí địa lý, và ngành nghề, tạo nên thách thức lớn trong việc định giá chính xác.

* Nhóm muốn sử dụng công nghệ học máy và phân tích dữ liệu, mô hình dự đoán mức lương giúp cung cấp giá trị cho ứng viên, nhà tuyển dụng và các nhà hoạch định chính sách đồng thời hỗ trợ giải quyết nhu cầu tìm kiếm và nâng cao giá trị cho bản thân.

---
# Cụ thể đồ án

**Đề tài**: Phân tích về thị trường lao động và dự đoán mức lương của các đơn tuyển dụng tại thị trường Việt Nam.

**Nguồn dữ liệu**: Dữ liệu được thu thập tại website CareerViet bằng phương pháp Selenium và Beautiful Soup. Tập dữ liệu bao gồm hơn 25000 công việc và hơn 20 thuộc tính.

Đường dẫn website: https://careerviet.vn/

**Ý tưởng**: Thông qua quy trình xây dựng và giải quyết một bài toán khoa học dữ liệu cơ bản:
* Thu thập dữ liệu
* Tiền xử lý dữ liệu
* Khám phá dữ liệu
* Trực quan hóa dữ liệu
* Mô hình hóa dữ liệu, đánh giá và cải thiện các mô hình

**Trang web deploy mô hình:** https://predictsalarymodel.onrender.com/
---
# Tổ chức GitHub
```
├── README.md                                <- Information for this project
│
├── dataset
│   ├── data_for_visual.csv                  <- Data used for visualization
│   ├── job_data_new                         <- Raw data crawled from links
│   ├── job_links.csv                        <- Links of every job application
│   ├── Defined_salary.csv                   <- Example that have numeric salary
│   ├── Unefined_salary.csv                  <- Example that have "competitive" salary
├── Utils                            
│   ├── Trans_Tokenize.py                    <- Python file for translate and tokenize text 
├── CollectingData                            
│   ├── CrawlData.ipynb                      <- Notebook for collecting data
├── ExploringData                            
│   ├── ExploringData.ipynb                  <- Notebook for exploring data and preprocessing for visualization
│   ├── VisualizationData.ipynb              <- Notebook for visualizing data
├── ModellingData                            
│   ├── dataPreprocessing.ipynb              <- Notebook for preprocessing data before modelling
│   ├── models.ipynb                         <- Notebook for modelling data and evaluating
├── DeployModel
│   ├── app.py
│   ├── predict_salary_random_forest.pkl
│   ├── prediction_history.json
│   ├── requirement.txt
│   ├── index.html