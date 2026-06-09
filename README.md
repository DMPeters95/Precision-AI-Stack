# Precision-AI-Stack

A fully self-hosted, private AI workstation built on consumer hardware. No cloud, no subscriptions, no data leaving your network.

## Hardware
- **CPU:** Intel Core i7-9700 (9th Gen vPro) @ 3.00GHz
- **RAM:** 64GB DDR4
- **GPU:** NVIDIA RTX 3090 24GB (Dell OEM)
- **Storage:** 512GB NVMe (OS) + 2x 4TB HDD
- **OS:** Ubuntu 24.04 LTS

## Stack
| Service | Purpose | Port |
|---|---|---|
| Ollama | Local LLM runner | 11434 |
| Qwen3 30B | Primary AI model | - |
| SearXNG | Self-hosted web search | 8080 |
| Open WebUI | Chat interface | 3000 |
| Monitoring API | Hardware stats | 8585 |
| YouTube to MP3 | Audio downloader | 5001 |

## Features
- Private local AI with live web search
- Real-time hardware monitoring
- Remote access via Tailscale from anywhere in the world
- YouTube to MP3 converter with embedded album art
- GPU accelerated inference (CUDA 13.0)

## Remote Access
Accessible from any device via Tailscale VPN. No ports exposed to the internet.

## Roadmap
- [ ] ComfyUI image generation
- [ ] SAM2 AI rotoscoping
- [ ] Image to STL pipeline for 3D printing
- [ ] LoRA fine tuning
- [ ] Agent capabilities

## Setup
See individual service directories for configuration details.
