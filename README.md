# VoltAI — Electronics Engineering Copilot

VoltAI is a local AI assistant designed for **Electrical and Electronics Engineering students**.
It combines **large language models, engineering computation tools, and multi-agent workflows** to help analyze circuits, understand theory, and visualize signals.

VoltAI runs **fully locally** using Ollama and Llama 3.1.

---

# Features

### Engineering Tools

* Voltage divider calculations
* Ohm’s law solver
* RC filter cutoff analysis
* Control system step responses
* Antenna wavelength and Friis equation
* DSP utilities (Nyquist, aliasing, FFT)

### AI Reasoning

* Local LLM (Llama 3.1 via Ollama)
* Engineering knowledge retrieval (RAG)
* Multi-agent architecture for domain specialization

### Visualization

* Bode plots
* Step responses
* Signal plots

### Interface

* Local web UI
* Interactive engineering assistant
* Inline plot generation

---

# Architecture

VoltAI uses a **multi-agent AI architecture**.

User queries are routed to specialized engineering agents.

```
User
 │
 ▼
VoltAI Supervisor
 │
 ▼
Intent Router
 │
 ├── CircuitAgent
 ├── DSPAgent
 ├── ControlAgent
 └── AntennaAgent
```

Each agent uses dedicated engineering tools to compute results.

---

# Installation

Clone the repository.

```
git clone https://github.com/YOUR_USERNAME/VoltAI.git
cd VoltAI
```

Run VoltAI.

```
python app.py
```

The launcher will:

* install Python dependencies
* verify Ollama
* download the required LLM model
* launch the UI

---

# Usage

After launching, open:

```
http://127.0.0.1:7860
```

Example queries:

```
Calculate voltage divider Vin=12 R1=2k R2=1k
```

```
Explain Nyquist sampling theorem
```

```
Plot RC filter bode R=1k C=100n
```

```
Wavelength for 2.4 GHz
```

---

# CLI Mode

VoltAI also supports terminal usage.

```
python cli.py
```

Example:

```
VoltAI > Explain aliasing in DSP
```

---

# Tech Stack

* Python
* LangGraph
* LangChain
* Ollama
* Llama 3.1
* FAISS vector database
* SentenceTransformers
* Gradio UI

---

# Roadmap

Future improvements:

* circuit diagram understanding
* SPICE simulation integration
* symbolic circuit solving
* engineering document ingestion

---

# Author

Gurnoor Singh
