# Precision-AI-Stack

A self-hosted, private AI stack running on local hardware with web search capabilities and remote access.

## Hardware
- CPU: Intel 9th Gen i7 vPro
- RAM: 64GB DDR4
- GPU: NVIDIA RTX 3090 24GB (Dell OEM)
- Storage: 512GB NVME (OS), 2x 4TB HDD
- OS: Ubuntu 24.04 LTS

## Stack
- **Ollama** - Local LLM runner
- **Qwen3 30B** - Primary AI model
- **SearXNG** - Self-hosted web search
- **Open WebUI** - Chat interface
- **Tailscale** - Secure remote access

## Access
- Local: http://192.168.12.144:3000
- Remote: http://100.65.229.127:3000 (via Tailscale)

## Roadmap
- [ ] NAS setup with Samba
- [ ] Image generation with ComfyUI
- [ ] Agent capabilities with Open Interpreter
