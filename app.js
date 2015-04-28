var multer = require('multer'),
    express = require('express'),
    app = express();

app.use(multer({ 
  dest:'./uploads/',
  rename: function (fieldname, filename) {
    return filename.replace(/\W+/g, '-').toLowerCase() + Date.now()
  } 
}));

app.use(express.static('public'));

app.get('/', function(req, res) {
  res.sendFile('index.html');
});

app.post('/file-upload', function(req, res, next) {
  console.log(req.body)
  console.log(req.files)
  
  res.status(204).end()
});

app.listen(3000, function() {
  console.log("Listening on 3000...");
});
