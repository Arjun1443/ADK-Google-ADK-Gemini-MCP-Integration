# Run and deploy the Streamlit companion

## Entry point

Repository: `Arjun1443/ADK-Google-ADK-Gemini-MCP-Integration`  
Branch: `main`  
Main file: `streamlit_app/app.py`  
Python: **3.11**

## Local setup

```bash
git clone https://github.com/Arjun1443/ADK-Google-ADK-Gemini-MCP-Integration.git
cd ADK-Google-ADK-Gemini-MCP-Integration
python -m venv .venv
# Activate the virtual environment before continuing.
python -m pip install -r streamlit_app/requirements.txt
python -m streamlit run streamlit_app/app.py
```

Dependencies are scoped to the app directory. Existing notebooks and their dependencies are preserved.

## Community Cloud

1. Sign in to https://share.streamlit.io/ with an account authorized for this GitHub repository.
2. Select **Create app**, then deploy from the repository above.
3. Use branch `main` and main file `streamlit_app/app.py`.
4. In Advanced settings, select Python 3.11 and configure secrets only where needed.
5. Deploy and wait for a successful build. Test the main interaction on the live app before adding its URL as a portfolio demo.

No live deployment URL is claimed in this document. Official deployment guidance: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Runtime configuration

Configure only a dedicated demonstration server:

```toml
MCP_SERVER_URL = "https://your-approved-server.example/mcp"
MCP_ALLOWED_TOOLS = "read_only_tool_name"
# Optional, only if required by the server:
MCP_AUTH_TOKEN = "your-demo-server-token"
```

Every allowed tool is callable by app visitors under these credentials. Use a read-only demo account/server or restrict access. Leave secrets unset to deploy the explanatory interface without a live connection. The app supports Streamable HTTP, not the notebook’s stdio server.

## Implementation scope

Live tools require an owner-approved HTTPS Streamable HTTP server plus an explicit tool allowlist. No live server was configured or tested.

## Validation

The app was checked locally with Streamlit AppTest for initial rendering. The tabular apps were also exercised through training and scenario prediction. Digit predictions, catalog similarity, currency calculation, and GRPO reward edge cases were checked locally. Credential-dependent and heavyweight model flows are identified above and are not covered by a successful initial-render test.

Dependency ranges are not a complete lockfile. Validate the hosted environment and resource use after deployment. Do not put keys in repository files.
