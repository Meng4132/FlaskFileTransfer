**Flask File Transfer**

License: [MIT License](LICENSE)

## Description
This is a lightweight HTTP-based file transfer tool, powered by `flask`.

**Features**:
- Easy setup with minimal dependencies
- Clean web interface with Bootstrap styling
- Supports file uploads and downloads via a web interface.
- Ideal for small-scale file sharing in local networks (e.g. home, office)

**Limitations**:
- Not designed for large-scale or public file transfers
- No built-in authentication or encryption (use only in trusted networks)

## Get started
### Preparations (Linux)
```bash
apt install git python3 python3-venv
```

1. Clone to the local
```bash
git clone https://github.com/Meng4132/FlaskFileTransfer.git
cd FlaskFileTransfer
```

2. Virtual environment (Recommended)
```bash
python3 -m venv venv_flask
```
Enter the virtual environment:
```bash
source ./venv_flask/bin/activate
```

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
use `Ctrl-C` to quit.

5. To quit the virtual environment:
```bash
deactivate
```

## Security Note
This tool is designed for trusted local networks only. Do not expose it to the Internet without additional security measures (e.g. HTTPS, authentication).

## Structure
```txt
FileTransfer/
├── .gitignore
├── flask_transfer.py                 # Main application script
├── requirements.txt                  # Python dependencies
├── static/
│   ├── css/                          # Bootstrap CSS
│   │   ├── bootstrap.min.css
│   │   └── bootstrap.min.css.map
│   └── js/                           # Bootstrap JS
│       └── bootstrap.bundle.min.js
├── templates/
│   └── index.html                    # Web interface template
└── uploads/                          # Created during the first run. Uploaded files will be here.
```

## Credits 
This project uses [Bootstrap](https://getbootstrap.com/) v5.1.3 for frontend styling and interactive components, licensed under the [MIT License](https://github.com/twbs/bootstrap/blob/main/LICENSE).

## License
This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.
