[Unit]
Description=Photo gen
After=network.target

[Service]
Type=simple
User=root
Group=<группа пользователя от которого вы запускаете скрипты>

Environment=PYTHONPATH=</full/path/to/directory/with/your/script> 
WorkingDirectory=</full/path/to/directory/with/your/script>
ExecStart=</full/path/to/python> </full/path/to/your/script>
Restart=always
RestartSec=5

[Install]
WantedBy=network.target