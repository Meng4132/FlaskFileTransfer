Project Name: Flask File Transfer
License: [MIT License](LICENSE)

## Description
This is a lightweight file transfer tool. After installing `flask`, you can start server and visit it through your browser.
However, this program may ONLY be applicable for simple LAN(Local Area Network) file transfer. and is NOT suitable for large-scale file transfers involving a large number of users.

### Get started
## Preparations:

# Linux
```bash
apt install git python
```

1. Clone to the local
```bash
git clone https://github.com/Meng4132/FlaskFileTransfer.git
cd FlaskFileTransfer
```
2. As a network service, it's better to create a virtual environment.
```bash
python3 -m venv venv_flask
```
Enter the virtual environment:
`source ./venv_flask/bin/activate`
3. Install `flask`
```bash
pip install flask
```
or
```bash
pip install -r requirements.txt
```
4. Start server
```bash
python3 flask_transfer.py
```

## Structure
```txt
FileTransfer/
├── .gitignore
├── flask_transfer.py
├── requirements.txt
├── static/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── bootstrap.min.css.map
│   └── js/
│       └── bootstrap.bundle.min.js
├── templates/
│   └── index.html
└── uploads/ # ->  Created during the first run. Uploaded files will be here.
```
## License
This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.
