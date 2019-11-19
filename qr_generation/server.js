var express = require("express");
var otpGenerator = require('otp-generator');
var qrcode = require('qrcode');
const fs = require('fs');
var base64Img = require('base64-img');

const {Storage} = require('@google-cloud/storage');
const storage = new Storage({keyFilename: "key.json"});
const bucketName = 'bocs-demo123.appspot.com';


a0='0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1';
a1='0xFFcf8FDEE72ac11b5c542428B35EEF5769C409f0';
a2='0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b';
a3='0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d';
a4='0xd03ea8624C8C5987235048901fB614fDcA89b117';
a5='0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC';
a6='0x3E5e9111Ae8eB78Fe1CC3bb8915d5D461F3Ef9A9';
a7='0x28a8746e75304c0780E011BEd21C72cD78cd535E';
a8='0xACa94ef8bD5ffEE41947b4585a84BdA5a3d3DA6E';
a9='0x1dF62f291b2E969fB0849d99D9Ce41e2F137006e';

addr_list=[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9];

var app = express();
const bodyParser = require('body-parser'); 
app.use(bodyParser.json());


app.get("/url", (req, res, next) => {
    otp = otpGenerator.generate(6, { upperCase: false, specialChars: false, alphabets:false });
    data = {name:'megh', otp};
    console.log(data);
    res.json(data);
});

app.post('/encrypt', async function(req, res) {
    var user = req.body;
    // console.log(req);
    console.log(user);
    // var para1 = addr_list[Math.floor(Math.random() * addr_list.length)];

    var para2 = user.num ;
    
    
    var temp = getRandom(addr_list,5);
    for (var i = 0; i<5; i++){
        console.log(temp[i]);
        await encrypt(temp[i],para2+i,i);
    }
    res.json({
        success:"True"
    })
});


app.listen(3001, () => {
 console.log("Server running on port 3001");
});

async function encrypt(para1,para2,i) {
    var CryptoJS = require("crypto-js");
    var ciphertext = CryptoJS.AES.encrypt(para1, para2.toString());
    run(para1, para2); 
      
}

async function run(para1, para2) {
    const res = await qrcode.toDataURL(para1);
  
    fs.writeFileSync('qr.jpg', `${res}`);
    console.log('Wrote to qr.html');
    name = '_' + para2.toString();
    base64Img.img(`${res}`, '', name, function(err, filepath) {});
    uploadFile(`${name}.png`)
}

function getRandom(arr, n) {
    var result = new Array(n),
        len = arr.length,
        taken = new Array(len);
    if (n > len)
        throw new RangeError("getRandom: more elements taken than available");
    while (n--) {
        var x = Math.floor(Math.random() * len);
        result[n] = arr[x in taken ? taken[x] : x];
        taken[x] = --len in taken ? taken[len] : len;
    }
    return result;
}


async function uploadFile(filename) {
    // Uploads a local file to the bucket
    await storage.bucket(bucketName).upload(filename, {
      // Support for HTTP requests made with `Accept-Encoding: gzip`
      gzip: true,
      // By setting the option `destination`, you can change the name of the
      // object you are uploading to a bucket.
      metadata: {
        // Enable long-lived HTTP caching headers
        // Use only if the contents of the file will never change
        // (If the contents will change, use cacheControl: 'no-cache')
        cacheControl: 'public, max-age=31536000',
      },
    });

    console.log(`${filename} uploaded to ${bucketName}.`);
  }
