const express = require('express'); //need to install express npm install express
const fs = require('fs'); //this is used to read in from the prompts.json file
const cors = require('cors')
const app = express();
const port = 5213; //this is the port the server is running on

const corsOptions = {
  origin: 'http://127.0.0.1:3000',
  optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}

let prompts;

try {
  const promptsData = fs.readFileSync('prompts.json');
  prompts = JSON.parse(promptsData);
} 
catch (error) {
  console.error('Error reading prompts.json:', error.message); //error if prompts.json file does not exist
  prompts = [];
}

app.get('/prompts', cors(corsOptions), (req, res) => {
  //creates new array without id
  const promptfiltered = prompts.map(({ id, title, prompt }) => ({ id, title, prompt }));
  res.json(promptfiltered);
});

app.get('/prompts/:promptId', cors(corsOptions), (req, res) => {
  const promptId = parseInt(req.params.promptId);
  const prompt = prompts.find((p) => p.id === promptId); //compares promptid in http get with promptid in json

  //if the prompt does not exist
  if (!prompt) {
    return res.status(404).json({ error: 'Prompt not found' });
  }

  //sets a new const with out promptId
//  const { id, ...promptfiltered } = prompt;
//  res.json(promptfiltered);
  res.json(prompt);
});

//checks if there is an app listen error
app.listen(port, (error) => {
  if (error) {
    //will return error in consel if there is an error with the server
    console.error('Server encountered an error:', error);
  } 
  else {
    //logs in console where the server is running with port
    console.log(`Server is running on http://localhost:${port}`);
  }
});