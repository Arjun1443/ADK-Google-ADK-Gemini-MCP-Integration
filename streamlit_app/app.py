import asyncio,json
import streamlit as st
from ui import page,secret

page('MCP Tool Observatory','Inspect an MCP server’s tool schemas and invoke a selected tool with explicit JSON arguments.','AGENT TOOLING')
endpoint=secret('MCP_SERVER_URL')
token=secret('MCP_AUTH_TOKEN')
allowed={name.strip() for name in secret('MCP_ALLOWED_TOOLS').split(',') if name.strip()}
st.caption('The server endpoint is configured by the app owner in Streamlit secrets. Visitors cannot redirect the app to arbitrary hosts.')
async def execute(name=None,args=None):
    from mcp import ClientSession
    from mcp.client.streamable_http import streamablehttp_client
    headers={'Authorization':f'Bearer {token}'} if token else None
    async with streamablehttp_client(endpoint,headers=headers) as (read,write,_):
        async with ClientSession(read,write) as session:
            await session.initialize()
            if name is None:
                result=await session.list_tools()
            return [t.model_dump(mode='json') for t in result.tools if t.name in allowed]
            # Only tools explicitly approved by the owner can be called.
            
            
            if name not in allowed: raise ValueError('Tool is not in the owner allowlist.')
            result=await session.call_tool(name,arguments=args)
            return result.model_dump(mode='json')
if not endpoint:
    st.info('Connect an owner-approved Streamable HTTP MCP server through MCP_SERVER_URL in app secrets to enable live tools.')
else:
    if not allowed:
        st.info('Add a comma-separated MCP_ALLOWED_TOOLS allowlist in app secrets to enable tool access.')
    if not endpoint.startswith('https://'):
        st.error('The configured server must use HTTPS.'); st.stop()
    if st.button('Connect and discover tools',type='primary'):
        try:
            st.session_state.tools=asyncio.run(asyncio.wait_for(execute(),timeout=35))
        except Exception:
            st.error('Could not list tools. Check the server URL, authentication, and protocol support.')
    tools=st.session_state.get('tools',[])
    if tools:
        selected=st.selectbox('Server tool',range(len(tools)),format_func=lambda i:tools[i]['name'])
        tool=tools[selected]
        st.write(tool.get('description',''))
        st.json(tool.get('inputSchema',{}))
        arguments=st.text_area('Arguments (JSON object)',value='{}',max_chars=10000)
        approved=st.checkbox('I understand this call may change data on the configured server.')
        if st.button('Invoke selected tool',disabled=not approved):
            try:
                parsed=json.loads(arguments)
                if not isinstance(parsed,dict): raise ValueError('Arguments must be an object.')
                st.json(asyncio.run(asyncio.wait_for(execute(tool['name'],parsed),timeout=35)))
            except (ValueError,json.JSONDecodeError): st.error('Enter a valid JSON object.')
            except Exception: st.error('The tool call failed or timed out. Check the server logs.')
with st.expander('Deployment scope',expanded=True):
    st.markdown("""This companion app uses a Streamable HTTP MCP client. The original notebook combines Google ADK, Gemini, and a stdio server; it remains the source for that integration experiment.

Do not configure a privileged MCP server on a public app. Any visitor with access to this app can invoke the server tools exposed by its credentials. Use a dedicated read-only demonstration server or restrict app access before adding credentials. An unchecked box is a UI safeguard, not authentication.
""")
