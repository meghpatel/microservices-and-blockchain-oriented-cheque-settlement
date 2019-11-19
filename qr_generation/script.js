var fs = require('fs'); 

const {Storage} = require('@google-cloud/storage');

  // Creates a client
const storage = new Storage();

// var readMe = fs.readFileSync('readMe.txt', 'utf-8'); 

// var firebaseConfig = {
//     apiKey: 'AIzaSyAIRwJz5kWIkTi6BJv-ILVfqdx708uoYk8',
//     authDomain: 'bocs-demo123.firebaseapp.com',
//     databaseURL: 'https://bocs-demo123.firebaseio.com',
//     storageBucket: 'bocs-demo123.appspot.com'
//   };

// firebase.initializeApp(firebaseConfig);

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