#!/bin/bash
#YHK 安装Python

#安装路径

#yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make


yum install libffi-devel -y

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

tar -zxvf Python-3.7.0.tgz
cd Python-3.7.0
./configure
make&&make install

mv /usr/bin/python /usr/bin/python.bak
ln -s /usr/local/bin/python3 /usr/bin/python
mv /usr/bin/pip /usr/bin/pip.bak
ln -s /usr/local/bin/pip3 /usr/bin/pip

python
pip -V


sed -i "1c#! /usr/bin/python2.7" /usr/libexec/urlgrabber-ext-down
sed -i "1c#! /usr/bin/python2.7" /usr/bin/yum