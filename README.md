# FabLabFCFM Telegram Bot
Python based telegram bot that manages the IoT network of the FCFM's FabLab (University of Chile).

### Installing

It is highly advised that you use a **Python Virtual Environment** to install the modules, also make sure you are using Python 3.10 and above.

1. Creating the virtual environment

    ```bash
    # installing virtualenv
    pip install virtualenv

    # create a virtual env for the project
    virtualenv .venv
    ```

2. Activating the virtual environment

    Windows

    ```powershell
    .venv\Scripts\activate
    ```

    Linux/MacOS

    ```bash
    source .venv/bin/activate
    ```

3. Installing modules via pip

    ```bash
    pip install -r requirements.txt
    ```

### Executing

```bash
python bot.py
```
