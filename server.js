var express = require('express'),
    multer = require('multer');

var app = express()
app.use(express.static(__dirname));
app.get('/', function(req, res) {
  res.send('hello world');
});

app.post('/', function(req, res) {
    console.log(req.body);
    console.log(req.files);
    res.status(204).end();
});

app.listen(3000);
