var fs = require('fs'); 

const {Storage} = require('@google-cloud/storage');

  // Creates a client
const storage = new Storage();

const storage = gcloud.storage({
    projectId: '<projectID>',
    keyFilename: 'service-account-credentials.json',
});

const bucket = storage.bucket('<projectID>.appspot.com')

var storage = require('@google-cloud/storage')
// Get a reference to the storage service, which is used to create references in your storage bucket
// var storage = firebase.storage();

// Create a storage reference from our storage service
var storageRef = storage.ref();

// var file = ... // use the Blob or File API

fs.readFile('1.png', (err, data) => {
  if (err) throw err;
  console.log(data);
});

ref.put(file).then(function(snapshot) {
  console.log('Uploaded a blob or file!');
});