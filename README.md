# ADK-3: Google ADK + Gemini + MCP Integration

This repository contains a complete workflow demonstrating how to build, run, and manage LLM-powered agents using Google ADK, Gemini models, retry-safe API calls, and MCP Tool integrations.

## 🚀 What This Notebook Solves

### 1. **Google ADK Setup**

* Loads Google API keys using `UserSecretsClient`
* Initializes environment variables for Gemini models
* Ensures a clean and reusable configuration for any ADK project

### 2. **Agent Creation Using Google ADK**

* Builds an `LlmAgent` using Gemini models (`google.adk.models.google_llm.Gemini`)
* Configures sessions, runners, and message passing
* Shows how to orchestrate agents programmatically

### 3. **Robust API Retry Mechanism**

* Implements `HttpRetryOptions` with:

  * Custom retry attempts
  * Exponential backoff
  * Status-code-based retry logic
* Helps avoid failures caused by 429/500/503/504 rate-limit errors

### 4. **MCP (Model Context Protocol) Integration**

* Demonstrates connecting to an external MCP server/toolset
* Uses:

  * `McpToolset`
  * `StdioConnectionParams`
  * `StdioServerParameters`
* Example setup using an Everything Server with Node (`npx`)
* Shows how to extend an LLM agent with additional tool capabilities

### 5. **UUID-Based Conversation & Session Management**

* Uses unique IDs for:

  * Tracking runs
  * Agent session management
  * Organized conversation logs

### 6. **End-to-End LLM Workflow Execution**

* Running the configured agent using `Runner`
* Taking inputs → generating responses → handling retries → using tools
* Shows a production-like pipeline for LLM agents

---

## 📁 File Structure

```
adk-3.ipynb   # Complete notebook with ADK + Gemini + MCP pipeline
```

---

## 🛠️ Technologies Used

* **Google ADK** (Agent Development Kit)
* **Google Gemini API (google.genai)**
* **MCP (Model Context Protocol)**
* **Python**
* **UUID for session handling**
* **Retry-safe API interaction**

---

## ▶️ How to Run

1. Install dependencies:

   ```bash
   pip install google-genai google-adk
   ```
2. Set your API key:

   ```bash
   export GOOGLE_API_KEY="YOUR_KEY"
   ```
3. Open the notebook:

   ```bash
   jupyter notebook adk-3.ipynb
   ```

---

## 📌 Key Highlights

* Clean ADK initialization workflow
* Full example of Gemini agent creation
* Reliable retry mechanism
* Tool augmentation via MCP
* Production-ready execution pipeline

---

## 📜 License

This project is released under MIT License.

---

If you want a more detailed README with diagrams, badges, or installation scripts, request an updated version.
