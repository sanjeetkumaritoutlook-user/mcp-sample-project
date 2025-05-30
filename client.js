const axios = require('axios');

async function fetchData() {
  try {
    const response = await axios.post('http://localhost:4000/mcp/action', {
      action: 'getData',
      params: {}
    });
    console.log('Response from MCP server:', response.data);
  } catch (error) {
    console.error('Error fetching data from MCP server:', error.message);
  }
}

fetchData();
