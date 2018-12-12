@echo off
e:
cd E:\program\Python37\Scripts
start java -jar selenium-server-standalone-3.141.59.jar -role hub -port 8089
::休眠三十秒，等待远程机器的服务启动
choice /t 30 /d y /n >nul
e:
cd e:\workspace\PyCharmProjects\Selenium\chapter06
python mixed_os_execute.py