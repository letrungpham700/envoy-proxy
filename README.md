# Envoy Proxy
![Logo](https://www.envoyproxy.io/docs/envoy/latest/_static/envoy-logo.png)

Tổng quan về Envoy Proxy, cách Setup vs Config Envoy Proxy

### Envoy Proxy là gì?
Envoy là một proxy phân tán hiệu suất cao được viết bằng C ++. Nó có thể được sử dụng như một bộ cân bằng tải L4 hoặc L7 và được thiết kế để xây dựng các service mesh phân tán lớn và các microservice. Nó đơn giản hóa việc xây dựng khả năng quan sát trong các dịch vụ quy mô lớn với khả năng tạo mạng lưới dịch vụ Envoy, có hỗ trợ gốc cho việc theo dõi phân tán và cung cấp khả năng giám sát wire-level của MongoDB, DynamoDB và các dịch vụ khác. Có hỗ trợ hạng nhất cho HTTP / 2 và gRPC trên mạng lưới và Envoy cung cấp các API để quản lý service mesh theo thời gian thực.

### Setup Envoy Proxy
```bash
sudo apt update

sudo apt install apt-transport-https gnupg2 curl lsb-release

curl -sL 'https://deb.dl.getenvoy.io/public/gpg.8115BA8E629CC074.key' | sudo gpg --dearmor -o /usr/share/keyrings/getenvoy-keyring.gpg

echo a077cb587a1b622e03aa4bf2f3689de14658a9497a9af2c427bba5f4cc3c4723 /usr/share/keyrings/getenvoy-keyring.gpg | sha256sum --check

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/getenvoy-keyring.gpg] https://deb.dl.getenvoy.io/public/deb/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/getenvoy.list

sudo apt update

sudo apt install -y getenvoy-envoy
```

#### Check Version Envoy Proxy
```bash
envoy --version
```
### Clone Config Envoy Proxy
```bash
git clone https://github.com/letrungpham700/envoy-proxy.git
```
#### Setup Config
```bash
cd envoy-proxy

mkdir /etc/envoy

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