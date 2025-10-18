# 🎓 Hardi EdTech AI - Advanced Multi-Persona Teaching System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-green.svg)](https://langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](LICENSE)

> **Production-ready AI teaching assistant with adaptive personas, multi-tool reasoning, and RAG-enhanced knowledge base**

---

## 🌟 **Overview**

Hardi EdTech AI is an advanced educational assistant that combines multiple AI capabilities with adaptive teaching methodologies. Built specifically for technical education in programming, AI/ML, cybersecurity, and software development.

### **Key Innovation**
- **4 Adaptive Teaching Personas** that fundamentally change teaching approach
- **Multi-Tool Orchestration** for comprehensive answers using calculator, web search, Wikipedia, and PDF analysis
- **RAG-Enhanced Knowledge Base** with real-world content from Stack Overflow, arXiv, OWASP
- **Few-Shot Learning** for consistent, high-quality responses

---

## 🎯 **Features**

### **Core Capabilities**

| Feature | Description |
|---------|-------------|
| 🎭 **Multi-Persona System** | 4 teaching modes: Teacher, Researcher, TA, Security Expert |
| 🧮 **Calculator Tool** | Advanced mathematical computations with Python REPL |
| 🌐 **Web Search** | Real-time information via Tavily API |
| 📚 **Wikipedia** | Instant access to encyclopedic knowledge |
| 📄 **PDF Analysis** | Deep document Q&A using vector embeddings (FAISS) |
| 🧠 **Knowledge Base** | Curated content from Stack Overflow, arXiv, OWASP |
| 💬 **Conversation Memory** | Context-aware multi-turn dialogues |
| 📥 **Export** | Download chat history for reference |

### **Teaching Personas**

#### 🎓 **Teacher Mode**
- Step-by-step explanations
- Analogies and real-world examples
- Working code with comments
- Progressive difficulty
- Practice suggestions

#### 🔬 **Researcher Mode**
- Deep technical analysis
- Historical context and evolution
- Comparative studies
- Mathematical formulations
- Paper citations

#### 👨‍🏫 **Teaching Assistant Mode**
- Guided problem-solving
- Diagnostic questions
- Graduated hints
- Debugging assistance
- Encouragement

#### 🔒 **Security Expert Mode**
- Attack vector analysis
- Proof-of-concept code
- Defense mechanisms
- CVE references
- Ethical framing

---

## 🏗️ **Architecture**

```
┌─────────────────────────────────────────────┐
│        Streamlit Web Interface              │
│     (User Interaction & Presentation)       │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         Agent Core (LangChain)              │
│  • Persona Management                       │
│  • Tool Orchestration (max 15 iterations)   │
│  • Conversation Memory                      │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│       Enhanced Prompt System                │
│  • Few-Shot Examples                        │
│  • Knowledge Base Retrieval                 │
│  • Context-Aware Selection                  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│              Tool Layer                     │
│  ┌──────────┬──────────┬──────────┬────────┐│
│  │Calculator│Wikipedia │Web Search│PDF Q&A ││
│  └──────────┴──────────┴──────────┴────────┘│
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│       Local LLM (Ollama)                    │
│       Model: gpt-oss:20b                    │
│       Context: 4096 tokens                  │
└─────────────────────────────────────────────┘
```

---

## 🚀 **Quick Start**

### **Prerequisites**

- Python 3.10+
- 16GB RAM minimum (20GB recommended)
- Ollama installed
- Docker (optional)

### **Installation (5 Minutes)**

#### **Option 1: Docker (Recommended)**

```bash
# Clone repository
git clone <your-repo>
cd hardi-edtech

# Create .env file
echo "TAVILY_API_KEY=your_key_here" > .env

# Build and run
docker-compose up --build

# Access at http://localhost:8501
```

#### **Option 2: Local Setup**

```bash
# 1. Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# 2. Pull model (11GB download)
ollama pull gpt-oss:20b

# 3. Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# 4. Install dependencies
poetry install

# 5. Create .env
cp .env.example .env
# Edit .env and add TAVILY_API_KEY

# 6. Run
poetry run streamlit run main.py
```

---

## 📚 **Usage Guide**

### **Basic Usage**

1. **Select Teaching Mode** in sidebar
2. **Ask your question** in chat input
3. **Get adaptive response** based on persona
4. **Upload PDF** (optional) for document analysis

### **Example Queries**

#### **Programming Questions**
```
Teacher Mode: "Explain recursion step by step"
→ Gets: Detailed breakdown with analogies and code

TA Mode: "Help me fix this IndexError"
→ Gets: Guided debugging with hints

Researcher Mode: "Compare sorting algorithms"
→ Gets: Technical analysis with time complexity
```

#### **AI/ML Questions**
```
"What is overfitting in machine learning?"
→ Uses: Knowledge Base + Few-shot examples

"Explain transformer architecture"
→ Uses: KB retrieval + Research papers
```

#### **Security Questions**
```
Security Mode: "How does SQL injection work?"
→ Gets: Attack vectors + Defense + Ethical context

"Explain OWASP Top 10"
→ Gets: Detailed vulnerability analysis
```

#### **Multi-Tool Queries**
```
"Calculate 2^256 and explain its use in cryptography"
→ Uses: Calculator + Web Search + Synthesis

"Search for latest AI developments and summarize"
→ Uses: Web Search + Knowledge Base
```

#### **PDF Analysis**
```
Upload: research_paper.pdf
Query: "What is the methodology?"
→ Uses: Vector embeddings + Semantic search
```

---

## 🛠️ **Technical Stack**

### **Core Technologies**

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **LLM** | Ollama | Latest | Local inference |
| **Model** | gpt-oss | 20B | Language generation |
| **Framework** | LangChain | 0.3+ | Agent orchestration |
| **UI** | Streamlit | 1.39+ | Web interface |
| **Vector Store** | FAISS | 1.8+ | PDF embeddings |
| **Embeddings** | HuggingFace | all-MiniLM-L6-v2 | Semantic search |
| **Web Search** | Tavily | Latest | Real-time info |
| **Dependency Mgmt** | Poetry | 1.7+ | Package management |
| **Containerization** | Docker | Latest | Deployment |

### **Knowledge Base Sources**

- **Stack Overflow**: Programming patterns and best practices
- **arXiv**: Research papers (Attention mechanism, Adam optimizer)
- **OWASP**: Security vulnerabilities and prevention
- **LeetCode**: Algorithm patterns and solutions

---

## 📁 **Project Structure**

```
hardi-edtech/
├── main.py                      # Streamlit UI (primary entry point)
├── agent_core.py                # LangChain agent configuration
├── educational_prompts.py       # Persona definitions + few-shot examples
├── knowledge_base.py            # RAG knowledge entries
│
├── app/
│   ├── __init__.py
│   └── tools.py                 # Tool implementations
│
├── pyproject.toml               # Poetry dependencies
├── poetry.lock                  # Locked versions
├── .env                         # API keys (not in repo)
├── .env.example                 # Template for .env
│
├── Dockerfile                   # Container definition
├── docker-compose.yml           # Multi-service orchestration
├── .dockerignore               # Exclude from build
│
├── README.md                    # This file
├── LICENSE                      # Educational use license
│
├── data/                        # PDF storage (runtime)
├── logs/                        # Application logs (runtime)
└── models/                      # Model cache (runtime)
```

---

## ⚙️ **Configuration**

### **Environment Variables (.env)**

```env
# Required
TAVILY_API_KEY=your_tavily_api_key

# Optional (uses defaults if not set)
OLLAMA_MODEL=gpt-oss:20b
OLLAMA_HOST=http://localhost:11434
MAX_ITERATIONS=15
AGENT_TEMPERATURE=0.7
```

### **Getting API Keys**

**Tavily (Free Tier):**
1. Visit https://tavily.com
2. Sign up for free account
3. Get API key from dashboard
4. Add to `.env` file

---

## 🎯 **Advanced Features**

### **Multi-Tool Orchestration**

The agent can chain multiple tools in a single response:

**Query:** "Calculate the factorial of 10 and explain where it's used"

**Agent Process:**
1. Uses **Calculator** → Computes factorial(10) = 3,628,800
2. Uses **Knowledge Base** → Retrieves combinatorics info
3. Uses **Web Search** → Finds real-world applications
4. **Synthesizes** → Complete answer with calculation + context

### **RAG-Enhanced Responses**

Knowledge base automatically enriches responses:

**Query:** "What are Python decorators?"

**System Process:**
1. Detects programming keywords
2. Retrieves relevant KB entry (Stack Overflow pattern)
3. Combines KB content + Few-shot example + Persona style
4. Generates comprehensive, consistent answer

### **PDF Vector Search**

Upload any PDF and ask questions:

**Technical Process:**
1. **Load**: PyPDFLoader extracts text
2. **Chunk**: RecursiveCharacterTextSplitter (1000 chars, 200 overlap)
3. **Embed**: HuggingFace all-MiniLM-L6-v2
4. **Store**: FAISS vector index
5. **Query**: Semantic similarity search (top 4 chunks)
6. **Generate**: LLM synthesizes answer from relevant chunks

---

## 📊 **Performance**

### **Response Times**

| Query Type | Average | Target |
|------------|---------|--------|
| Simple question | 3-5s | <10s |
| Multi-tool query | 15-25s | <40s |
| PDF analysis | 5-10s | <15s |
| Knowledge base hit | +2s | +5s |

### **Resource Usage**

| Resource | Idle | Active | Peak |
|----------|------|--------|------|
| RAM | 2GB | 6GB | 8GB |
| CPU | 5% | 40% | 80% |
| Disk | 15GB | 20GB | 25GB |

### **Model Performance**

- **Context Window**: 4096 tokens
- **Max Iterations**: 15 (enables multi-tool use)
- **Temperature**: 0.7 (balanced creativity/accuracy)

---

## 🧪 **Testing**

### **Quick Test Suite**

```bash
# Test all personas
poetry run python -c "
from educational_prompts import ENHANCED_PERSONAS
print(f'Loaded {len(ENHANCED_PERSONAS)} personas')
"

# Test knowledge base
poetry run python -c "
from knowledge_base import get_knowledge_context
result = get_knowledge_context('Python decorators')
print(f'KB retrieval: {len(result)} chars')
"

# Test Ollama connection
curl http://localhost:11434/api/tags
```

### **Integration Test**

```bash
# Run Streamlit and test these queries:
1. "What is 2^16?" (Calculator test)
2. "Explain attention mechanism" (KB test)
3. "Latest AI news" (Web search test - needs API key)
4. Upload PDF + "What is this about?" (PDF test)
```

---

## 🐛 **Troubleshooting**

### **Common Issues**

#### **Issue 1: Ollama Connection Refused**

```bash
# Check if Ollama is running
ollama list

# If not, start it
ollama serve

# Verify model
ollama pull gpt-oss:20b
```

#### **Issue 2: Module Not Found**

```bash
# Ensure virtual environment is activated
poetry shell

# Reinstall dependencies
poetry install
```

#### **Issue 3: Web Search Not Working**

```bash
# Check .env file
cat .env | grep TAVILY

# Verify API key is valid at tavily.com
# Restart application after adding key
```

#### **Issue 4: PDF Upload Fails**

- Check file size (<50MB recommended)
- Verify PDF is not corrupted
- Ensure `data/` directory exists and is writable
- Check logs in `logs/hardi.log`

#### **Issue 5: Out of Memory**

```bash
# Reduce context window in agent_core.py
num_ctx=2048  # Down from 4096

# Or use smaller model
ollama pull mistral:7b
```

---

## 🔒 **Security & Ethics**

### **Educational Purpose**

This system is designed for **legitimate educational use**:

✅ **Appropriate Use:**
- Learning programming and security concepts
- Understanding vulnerabilities for defensive purposes
- Academic research and coursework
- Professional training and skill development

❌ **Prohibited Use:**
- Actual attacks on systems without authorization
- Creating malware for distribution
- Unauthorized access to data or systems
- Any illegal activities

### **Data Privacy**

- 🔒 All LLM processing is **local** (via Ollama)
- 📄 PDFs stored **temporarily**, deleted after session
- 💬 Conversations **not sent** to external servers (except web search)
- 🔐 No tracking, analytics, or data collection
- 🗑️ Clear chat history anytime

### **Responsible AI**

- Security content includes **ethical framing**
- Proof-of-concept code for **education only**
- Emphasizes **legal and ethical boundaries**
- Encourages **responsible disclosure**

---

## 📈 **Roadmap**

### **Current Version: 1.0**

✅ Multi-persona system  
✅ Multi-tool orchestration  
✅ Knowledge base with RAG  
✅ PDF analysis  
✅ Conversation memory  
✅ Export functionality

### **Planned for v2.0**

- [ ] Voice input/output
- [ ] Code execution sandbox
- [ ] Interactive coding challenges
- [ ] Multi-language support
- [ ] Progress tracking
- [ ] Quiz generation
- [ ] Fine-tuned models for specific domains
- [ ] Mobile app

---

## 🤝 **Contributing**

Contributions welcome! Focus areas:

1. **New Teaching Personas**: Add specialized teaching modes
2. **Additional Tools**: Integrate more data sources
3. **Knowledge Base**: Expand with more real-world content
4. **UI Improvements**: Enhance user experience
5. **Performance**: Optimize response times
6. **Documentation**: Improve guides and examples

---

## 📝 **License**

Educational Use License - For academic and learning purposes.

**Users are responsible for ensuring their use complies with applicable laws and ethical guidelines.**

---

## 👥 **Credits**

**Developed by:** Hardi_EdTech Team  
**Built with:** LangChain, Ollama, Streamlit, FAISS, HuggingFace  
**Inspired by:** Modern AI education needs

### **Acknowledgments**

- **LangChain** for agent framework
- **Ollama** for local LLM inference
- **Streamlit** for rapid UI development
- **FAISS** for efficient vector search
- **HuggingFace** for embeddings
- **Tavily** for web search capabilities

---

## 📞 **Support**

### **Documentation**
- **Setup Guide**: See Quick Start section
- **Usage Examples**: See Usage Guide section
- **API Reference**: See inline code documentation

### **Getting Help**
1. Check this README
2. Review `logs/hardi.log` for errors
3. Verify configuration in `.env`
4. Test Ollama: `ollama list`

---

## 🎓 **Academic Context**

This project demonstrates:

- **Multi-Agent AI Systems**: Tool orchestration and reasoning
- **RAG Architecture**: Retrieval-Augmented Generation
- **Persona-Based Interaction**: Adaptive system behavior
- **Production ML**: End-to-end AI application
- **Educational Technology**: AI for personalized learning

**Perfect for:**
- AI/ML course projects
- Software engineering portfolios
- Educational technology research
- LLM application development
- Production AI system design

---

## 📊 **Metrics & Stats**

- **Total Code**: ~1,500 lines (clean, documented)
- **Dependencies**: 15 core packages
- **Personas**: 4 adaptive teaching modes
- **Tools**: 4 integrated (Calculator, Wikipedia, Web, PDF)
- **Knowledge Entries**: 15+ curated topics
- **Response Quality**: Enhanced with few-shot learning
- **Context Window**: 4,096 tokens
- **Max Iterations**: 15 (multi-tool support)

---

## 🌟 **Why Hardi EdTech?**

1. **Adaptive**: Changes teaching style based on context
2. **Comprehensive**: Multiple tools working together
3. **Educational**: Designed specifically for learning
4. **Privacy-First**: Local processing, no data leaks
5. **Production-Ready**: Docker, logging, error handling
6. **Well-Documented**: Clear code and extensive docs
7. **Extensible**: Easy to add personas, tools, content

---

**Version:** 1.0.0  
**Status:** Production Ready ✅  
**Release Date:** October 2025  
**Last Updated:** October 2025

---

<div align="center">

**Ready to transform technical education? Start learning with Hardi!** 🚀

[Quick Start](#-quick-start) • [Features](#-features) • [Documentation](#-usage-guide) • [Support](#-support)

</div>