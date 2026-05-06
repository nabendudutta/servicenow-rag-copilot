const vscode = require('vscode');
const axios = require('axios');

function activate(context) {

  const cmd = vscode.commands.registerCommand('sn.copilot', async () => {

    const panel = vscode.window.createWebviewPanel(
      'snCopilot',
      'ServiceNow Copilot',
      vscode.ViewColumn.One,
      { enableScripts: true }
    );

    panel.webview.html = `
      <h2>SN Copilot</h2>
      <input id="q" style="width:80%" placeholder="Ask something..." />
      <button onclick="ask()">Ask</button>
      <pre id="out"></pre>

      <script>
        const vscode = acquireVsCodeApi();

        function ask() {
          const q = document.getElementById('q').value;
          vscode.postMessage({q});
        }

        window.addEventListener('message', e => {
          document.getElementById('out').innerText += "\\n\\n" + e.data;
        });
      </script>
    `;

    panel.webview.onDidReceiveMessage(async m => {
      const res = await axios.post('http://localhost:8000/chat', {
        question: m.q
      });
      panel.webview.postMessage(res.data.answer);
    });

  });

  context.subscriptions.push(cmd);
}

exports.activate = activate;