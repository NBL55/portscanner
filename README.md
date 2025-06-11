# 🔍 Port Scanner in Python

A simple TCP port scanner built in Python using the `socket` module. Scans open ports in a given range on a target host.

## 🚀 How It Works
- Connects to ports using TCP (`socket.connect_ex`)
- Shows open ports in the specified range
- Uses a 1-second timeout per port to avoid hanging

## 📦 Features
- Scans ports from `start_port` to `end_port`
- Times how long the scan took
- Easily extendable for logging, service lookup, or GUI

## ⚙️ Setup

```bash
git clone https://github.com/your-username/port-scanner-python.git
cd port-scanner-python
python3 port_scanner.py
```

## 🔧 Configuration
Update these in `port_scanner.py`:

```python
target = "127.0.0.1"
start_port = 20
end_port = 100
```

## 🧠 Ideas to Extend
- Add service name lookup using `socket.getservbyport`
- Export results to a CSV or JSON file
- Build a simple Tkinter GUI

## 📄 License
MIT
