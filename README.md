# odoo
\\wsl$
Install odoo 15 on ubuntu 22 LTS
source: [https://computingforgeeks.com/install-odoo-ubuntu-focal-with-lets-encrypt-ssl/](https://huongdan.azdigi.com/cai-dat-odoo-15-tren-ubuntu-22-04/)

Bước 1: Cập nhật hệ thống

sudo apt update -y && apt upgrade -y

Bước 2: Cài đặt python3 và các thành phần cần thiết

sudo apt install python3-pip  wget python3-dev python3-venv python3-wheel libxml2-dev libpq-dev libjpeg8-dev liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential git libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libblas-dev libatlas-base-dev -y

Bước 3: Cài đặt và cấu hình PostgreSQL

sudo apt install postgresql -y

cài xong chỉnh pg_hba.conf file.

# "local" is for Unix domain socket connections only
local       all       all       trust

sudo su - postgres -c "createuser -s odoo15"
sudo useradd -m -d /opt/odoo15 -U -r -s /bin/bash odoo15

Bước 5: Cài đặt wkhtmltopdf

sudo apt-get install wkhtmltopdf -y
wkhtmltopdf --version

Bước 6: Cài đặt và cấu hình Odoo 15

su - odoo15
git clone https://www.github.com/odoo/odoo --depth 1 --branch 15.0 /opt/odoo15/odoo
cd /opt/odoo15
Tạo môi trường ảo theo lệnh:
python3 -m venv myodoo15-venv

Kích hoạt môi trường ảo theo lệnh:

source myodoo15-venv/bin/activate
Bên trong môi trường ảo, bạn cài đặt các module python cần thiết theo lệnh:
pip3 install wheel
pip3 install -r odoo/requirements.txt
Thoát môi trường ảo ra theo lệnh:
deactivate
mkdir /opt/odoo15/custom-addons

exit
sudo nano /etc/odoo15.conf

[options]
; This is the password that allows database operations:
admin_passwd = admin_password
db_host = False
db_port = False
db_user = odoo15
db_password = False
xmlrpc_port = 8069
logfile = /var/log/odoo15/odoo.log
addons_path = /opt/odoo15/odoo/addons,/opt/odoo15/custom-addons

------
mkdir /var/log/odoo15
chown odoo15:root /var/log/odoo15

Để dễ dàng quản lý Odoo15, các bạn cần tạo một file systemd theo lệnh:
sudo nano /etc/systemd/system/odoo15.service

[Unit]
Description=Odoo15
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo15
PermissionsStartOnly=true
User=odoo15
Group=odoo15
ExecStart=/opt/odoo15/myodoo15-venv/bin/python3 /opt/odoo15/odoo/odoo-bin -c /etc/odoo15.conf
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target

------

sudo systemctl daemon-reload
sudo systemctl enable --now odoo15

reboot wls
Get-Service LxssManager | Restart-Service




