# Google ADK, Gemini, and MCP Tool Integration

A notebook demonstrating agent setup, conversation sessions, retry settings, and an MCP toolset connection.

## Why this project matters

Tool integration lets an agent operate beyond text generation; session management and error handling make that integration easier to reason about.

## Technical focus

Python · Google ADK · Gemini · MCP · stdio tool transport · session identifiers

## Explore the implementation

Open [the notebook](<ADK-3 Google ADK + Gemini + MCP Integration.ipynb>) to inspect preprocessing, implementation, and saved outputs.

## Run locally

```bash
git clone https://github.com/Arjun1443/ADK-Google-ADK-Gemini-MCP-Integration.git
cd ADK-Google-ADK-Gemini-MCP-Integration
python -m venv .venv
# Activate .venv before continuing.
python -m pip install google-adk google-genai jupyter
python -m jupyter notebook
```

Select `ADK-3 Google ADK + Gemini + MCP Integration.ipynb` in Jupyter and review its configuration before executing cells in order.

## Reproducibility notes

The notebook uses Kaggle Secrets; adapt credential loading if running outside Kaggle. Its stdio MCP example also requires Node.js and `npx`. Review the external server command before execution. This is an integration demonstration, not a validated production deployment. No LICENSE file is present in the inspected tree; no new license is granted by this README.

Saved notebook outputs describe a prior execution; they are not an independently reproduced benchmark. Dependency versions are not locked, so compatibility may require adjustment.


## Author

[Naga Anweesh Reddy](https://github.com/Arjun1443/Naga-Anweesh-Reddy) · AI development and technical training
