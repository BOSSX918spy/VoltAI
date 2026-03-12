import subprocess
import sys
import platform
import shutil


def run(cmd):
    subprocess.check_call(cmd)


python = sys.executable


def ensure_requirements():
    print("Installing dependencies...")
    run([python, "-m", "pip", "install", "-r", "requirements.txt"])


def ensure_ollama():

    if shutil.which("ollama") is not None:
        print("Ollama detected.")
        return

    system = platform.system()

    print("Ollama not found. Installing...")

    if system == "Darwin":  # macOS
        subprocess.check_call([
            "/bin/bash",
            "-c",
            "curl -fsSL https://ollama.com/install.sh | sh"
        ])

    elif system == "Linux":
        subprocess.check_call([
            "/bin/bash",
            "-c",
            "curl -fsSL https://ollama.com/install.sh | sh"
        ])

    elif system == "Windows":
        print("Opening Ollama installer for Windows...")
        subprocess.check_call([
            "powershell",
            "-Command",
            "Start-Process https://ollama.com/download/OllamaSetup.exe"
        ])
        input("Press ENTER after installing Ollama to continue...")

    else:
        raise RuntimeError("Unsupported OS")


def ensure_model():

    print("Checking LLM model...")

    models = subprocess.check_output(["ollama", "list"]).decode()

    if "llama3.1" not in models:

        print("Downloading llama3.1 model...")

        subprocess.check_call([
            "ollama",
            "pull",
            "llama3.1"
        ])

    else:
        print("Model already installed.")


def launch_ui():

    print("Launching VoltAI UI...")
    run([python, "-m", "ui.interface"])


if __name__ == "__main__":

    print("Starting VoltAI...")

    ensure_requirements()

    ensure_ollama()

    ensure_model()

    launch_ui()