# Cerebro | Local AI Knowledge Assistance

> Cerebro serves as a knowledge assistant that operates locally. It indexes, enhance, stores, and retrieves your documentation using local LLMs, giving you full control over your data.

## The idea

My goal is to run a local LLM model without concerns about cots, privacy or internet connectivity. During my research, I discovered Ollama, which can run directly on my computer. This led me to think of integrate Ollama with my Obsidian vault, enable web search when necessary, create a personal local database, and develop an interface to communicate with the LLM.

I named the project after the X-Men's _Cerebro_ machine.

## Design Principles

- Local first - works offline by default.
- Markdown-native - Obsidian compatible.
- Persistence storage - SQLite database + markdown files.
- Query history.
- Optional fetching - Web search when needed.

## Overview

```
.md files (Obsidian)
Python App (Cerebro)
SQLite (metada index)
Ollama (LLM runtime)
```

**Important constrains**

- The model never accesses files or DB directly.

## Technology Stack

| Component             | Technology                 | Purpose                 |
| --------------------- | -------------------------- | ----------------------- |
| **Local LLM**         | Ollama                     | Model inference         |
| **Database**          | SQLite                     | Metadata storage        |
| **File Storage**      | Markdown files             | Document content        |
| **Orchestration**     | Python                     | System coordination     |
| **Knowledge Base**    | Obsidian                   | Interface to edit files |
| **Web Retrieval**     | Python requests/web search | External data fetching  |
| **API Communication** | HTTP/REST                  | Ollama API calls        |
