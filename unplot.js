var express = require('express');
var app = express();
var fs = require('fs');

app.get('/', function (req, res) {
  var html = "<!DOCTYPE html>
              <html>
                <head>
                  <title>Unplot</title>
                  <script src="js/dropzone.js"></script>
                  <link rel="stylesheet" type="text/css" href="style.css">
                </head>
                <body>
                  <div class="drop-container">
                    <form action="/file-upload" class="dropzone" id="dropzone">
                      <div class="fallback">
                        <input name="file" type="file" multiple />
                      </div>
                    </form>
                  </div>
                </body>
              </html>"
  response.send(html);
});


//need another app.get() here that responds to form submission
  fs.readFile(req.files.displayImage.path, function (err, data) {
    //This is going to end up overwriting like-named files...
    var newPath = __dirname + "uploads/"+req.files.displayImage.name;
    fs.rename(newPath, data, function (err) {
        res.redirect("back");
    });
  });

app.listen(8080);
