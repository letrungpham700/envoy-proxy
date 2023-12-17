# Envoy Proxy
![Logo](https://www.envoyproxy.io/docs/envoy/latest/_static/envoy-logo.png)

Tổng quan về Envoy Proxy, cách Setup vs Config Envoy Proxy

### Envoy Proxy là gì?
Envoy là một proxy phân tán hiệu suất cao được viết bằng C ++. Nó có thể được sử dụng như một bộ cân bằng tải L4 hoặc L7 và được thiết kế để xây dựng các service mesh phân tán lớn và các microservice. Nó đơn giản hóa việc xây dựng khả năng quan sát trong các dịch vụ quy mô lớn với khả năng tạo mạng lưới dịch vụ Envoy, có hỗ trợ gốc cho việc theo dõi phân tán và cung cấp khả năng giám sát wire-level của MongoDB, DynamoDB và các dịch vụ khác. Có hỗ trợ hạng nhất cho HTTP / 2 và gRPC trên mạng lưới và Envoy cung cấp các API để quản lý service mesh theo thời gian thực.

### Envoy Proxy làm được gì ?
Envoy là một proxy cung cấp các tính năng như load balancing, routing, mức độ cao, và nhiều tính năng khác. Mặc dù Envoy không chủ động phát hiện và ngăn chặn các cuộc tấn công như một hệ thống bảo mật chuyên sâu, nhưng nó có thể giúp trong việc đối phó với một số tình huống bảo mật.

Dưới đây là một số cách mà Envoy có thể đóng góp vào bảo mật hệ thống:

- Rate Limiting: Envoy hỗ trợ rate limiting, giúp ngăn chặn lưu lượng đến từ nguồn hoặc đích cụ thể, giảm nguy cơ tấn công DDoS (Distributed Denial of Service).

- Access Logging: Envoy có khả năng ghi lại thông tin chi tiết về mọi yêu cầu và phản hồi qua các access log. Thông qua việc theo dõi log, bạn có thể phát hiện các hoạt động bất thường hoặc tấn công.

- TLS (Transport Layer Security): Envoy có thể cấu hình để yêu cầu sử dụng TLS/SSL cho các kết nối, cung cấp lớp bảo mật cho dữ liệu truyền tải qua mạng.

- Header Manipulation: Envoy có thể kiểm soát và thậm chí thay đổi các header của yêu cầu và phản hồi. Điều này có thể hữu ích trong việc ngăn chặn một số loại tấn công như các loại tấn công injection.

- Web Application Firewall (WAF): Mặc dù Envoy không phải là một WAF, nhưng bạn có thể tích hợp Envoy với các giải pháp bảo mật bổ sung để tăng cường khả năng phát hiện và ngăn chặn các loại tấn công web.
### Adding Envoy Repository
```bash
sudo apt update

sudo apt install apt-transport-https gnupg2 curl lsb-release

curl -sL 'https://deb.dl.getenvoy.io/public/gpg.8115BA8E629CC074.key' | sudo gpg --dearmor -o /usr/share/keyrings/getenvoy-keyring.gpg

echo a077cb587a1b622e03aa4bf2f3689de14658a9497a9af2c427bba5f4cc3c4723 /usr/share/keyrings/getenvoy-keyring.gpg | sha256sum --check

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/getenvoy-keyring.gpg] https://deb.dl.getenvoy.io/public/deb/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/getenvoy.list
```
### Installing Envoy Proxy
```bash
sudo apt update

sudo apt install -y getenvoy-envoy
```
#### Create user non-root
```bash
useradd --no-create-home --shell /bin/false envoy
```
#### Check Version Envoy Proxy
```bash
envoy --version
```
#### Clone Config Envoy Proxy
```bash
git clone https://github.com/letrungpham700/envoy-proxy.git
```
#### Setup Config
```bash
cd envoy-proxy

mkdir /etc/envoy

chown envoy:envoy -R /etc/envoy

cp config/envoy.yaml /etc/envoy/envoy.yaml
```
#### Check Config Envoy Proxy
```bash
envoy --mode validate -c /etc/envoy/envoy.yaml
```
#### Run Envoy Proxy
```bash
envoy -c envoy.yaml
```
#### Run Service with Systemd
```bash
nano /etc/systemd/system/envoy-proxy.service
```

```bash
[Unit]
Description=Envoy Proxy Service
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
WorkingDirectory=/etc/envoy/
ExecStart=/usr/bin/envoy -c /etc/envoy/envoy.yaml
ExecReload=/bin/kill -HUP $MAINPID
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
```