# Ollama-Apify-MCP

Bring powerful **local AI** into your Apify workflows.

This project connects **Ollama’s locally-run language models** with the **Model Context Protocol (MCP)** and Apify’s scraping & automation platform. It enables you to process scraped data, extract insights, and generate intelligent responses — all **without external APIs**.

---

## 🧠 Overview

The **Ollama-Apify-MCP Actor** bridges Apify workflows with local LLMs via MCP, allowing AI-driven analysis and reasoning while preserving privacy and reducing costs.

---

## 🚀 Key Features

- 🔗 **Local LLM integration** — Run models like *Llama, Mistral, CodeLlama,* and more using Ollama  
- 🧩 **MCP-based communication** — Standards-compliant protocol for tool interaction  
- ⚙️ **Automatic context & preprocessing** — Improves model response quality  
- 🛠️ **Extensible tool architecture** — Easily add custom MCP tools & resources  
- 🔁 **Robust error handling & retries** — Reliable execution in workflows  

---

## 📦 Quick Start

Use as in cursor, copilot, claude code or desktop

```
{
  "mcpServers": {
      "ollama-apify-mcp": {
        "url": "https://lenticular-negative--ollama-apify-mcp.apify.actor/mcp?token={YOUR_TOKEN}"
      }
    }
  }
```

### 💻 Run Locally

```bash
pip install -r requirements.txt
APIFY_META_ORIGIN=STANDBY python -m src
```

Server runs at:

```
http://localhost:3000/mcp
```

---

### ☁️ Deploy to Apify

1. Push the repo to GitHub  
2. Add it as an Actor in Apify Console  
3. Enable **Standby Mode**  
4. Deploy

MCP endpoint:

```
https://lenticular-negative--ollama-apify-mcp.apify.actor/mcp
```

Include your API token:

```
Authorization: Bearer <APIFY_TOKEN>
```


## 🎯 Use Cases

- 📊 Analyze & summarize scraped web data  
- 🔐 Privacy-first local LLM processing  
- ⚡ Low-latency on-device inference  
- 🧱 Build AI tools inside Apify workflows  

---

## 🧩 Requirements

- Python 3.7+  
- Ollama installed locally  
- Apify CLI (for deployment)

---

## ❤️ Contributing

PRs and feature ideas are welcome — feel free to extend tools, improve docs, or share sample workflows.

---

## 📄 License

MIT License
