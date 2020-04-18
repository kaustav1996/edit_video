const youtubedl = require('youtube-dl');

function getVideo(videoUrl, filename){
    return new Promise(async (resolve,reject) => {
        try {

            const video = youtubedl(videoUrl,
            // Optional arguments passed to youtube-dl.
            ['--format=18'],
            // Additional options can be given for calling `child_process.execFile()`.
            { cwd: __dirname })
            
            // Will be called when the download starts.
            let inf = {};
            video.on('info', function(info) {
                inf = info
                console.log('Download started')
                console.log('filename: ' + info._filename)
                console.log('size: ' + info.size)
            });
            let filename = `${Math.floor(Math.random() * 100000000000)}.mp4`;
            
            video.pipe(fs.createWriteStream(`./media/${filename}`));




        } catch(err){

        }
    });
}

module.exports = {
    getVideo
}