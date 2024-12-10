
@echo off
powershell -NoProfile -ExecutionPolicy Bypass -Command "& {cd 'E:\Adrian\Tools\DIY\Logbook'; start python app.py; Start-Sleep -Seconds 5; Start-Process 'http://127.0.0.1:5000/'}"

