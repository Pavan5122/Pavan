const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());
   

app.post('/api/login', (req, res) => {
     user login
});


app.listen(port, () => console.log(`Server running on port ${port}`));
