const express = require('express');
const app = express();

app.use(express.json());

app.post('/mcp/action', (req, res) => {
  const { action, params } = req.body;
  console.log('Received MCP action:', action);

  if (action === 'getData') {
    res.json({ data: "Here's your MCP data from server!" });
  } else {
    res.status(400).json({ error: "Unknown action" });
  }
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`MCP Server running on http://localhost:${PORT}`));
