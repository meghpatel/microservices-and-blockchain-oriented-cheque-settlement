 // Imports the Google Cloud client library
  const {Storage} = require('@google-cloud/storage');

  // Creates a client
  // const storage = new Storage();
  // Creates a client from a Google service account key.
  const storage = new Storage({keyFilename: "key.json"});

  /**
   * TODO(developer): Uncomment these variables before running the sample.
   */
  const bucketName = 'bocs-demo123.appspot.com';

  // const bucketName = 'Name of a bucket, e.g. my-bucket';
  const filename = '1.png';

  async function uploadFile() {
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

  uploadFile();