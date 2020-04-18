const fs = require('fs')

var express = require('express');
const { exec } = require("child_process");
var app = express();
var path = require('path');

app.use('/media', express.static(path.join(__dirname, 'media')));
app.use('/output', express.static(path.join(__dirname, 'output')));

app.get('/postVideo', async (req, res)=>{
    try{

        let {videoUrl, from, to, caption} = req.query;

        

        await exec(`python3 ./edit_video/edit.py ${filename} ${from} ${to} '${caption}' ./output/${filename} ${videoUrl}`, (err, stdout, stderr) => {
            if (err) {
            //   result = "Error found";
                console.error(err);
            } else {
                return res.json({status: 'Successful', filename, url: `http://192.168.0.101:3004/output/${filename}`});
            }
          });



    } catch(err){
        console.log(err);
        res.json({err});
    }
});


app.listen(3004, () => {
    console.log("Listenning at 3004");
});


