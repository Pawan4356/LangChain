# Main Components of LangChain  

### 1. **Models**  
- Core component responsible for interaction with AI models.  
- Two main types:  
  - **Language Models (LLMs):** Generate and understand text.  
  - **Embedding Models:** Convert text into vector representations (used in semantic search, similarity, and retrieval).  

---

### 2. **Prompts**  
- Define **how you communicate with models**.  
- Can be **static or dynamic** (filled with variables at runtime).  
- Key features:  
  - **Reusable and modular.**  
  - **Role-based prompts** (system, user, assistant).  
  - **Few-shot prompting** to provide examples and guide model behavior.  

---

### 3. **Chains**  
- A way to **connect multiple components together** into a pipeline.  
- Example: output from one step can automatically become the input for the next.  
- Can be designed as:  
  - **Sequential Chains** (linear flow).  
  - **Parallel Chains** (multiple tasks at once).  
  - **Conditional Chains** (flow changes based on conditions).  

---

### 4. **Indexes**  
- Help connect LLMs to **external knowledge sources**.  
- Typically used for retrieval-based tasks like Q&A.  
- Built using four building blocks:  
  1. **Document Loader** (to load raw data).  
  2. **Text Splitter** (to break data into chunks).  
  3. **Vector Store** (to store embeddings efficiently).  
  4. **Retriever** (to fetch relevant context when needed).  

---

### 5. **Memory**  
- Since LLM API calls are **stateless**, memory enables **contextual conversations**.  
- Types of memory:  
  - **ConversationBufferMemory:** Stores full conversation (can grow large quickly).  
  - **ConversationBufferWindowMemory:** Keeps only the last *N* messages.  
  - **ConversationSummaryMemory:** Summarizes old context to keep conversations manageable.  
  - **Custom Memory:** Developer-defined for specific use cases.  

---

### 6. **Agents**  
- Go beyond static chains by adding **reasoning and decision-making**.  
- Agents can decide **which tool or chain to call** based on the input.  
- Examples include:  
  - **Tool-using agents** (search engine, calculator, API calls).  
  - **Chain-of-thought reasoning agents.**  
  - Custom-built task-specific agents.  

---

✨ In short:  
- **Models** = brains  
- **Prompts** = instructions  
- **Chains** = pipelines  
- **Indexes** = knowledge connectors  
- **Memory** = context keeper  
- **Agents** = smart decision-makers  