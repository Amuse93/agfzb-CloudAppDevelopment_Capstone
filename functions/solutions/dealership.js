/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */
 function main(params) {
    // console.log(params);
    return new Promise(function (resolve, reject) {
    const { CloudantV1 } = require('@ibm-cloud/cloudant');
    const { IamAuthenticator } = require('ibm-cloud-sdk-core');
    const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
        
    });
    cloudant.setServiceUrl(params.COUCH_URL);
        if (params.st) {
            // return dealership with this state 
            cloudant.postFind({db:'dealerships',selector:{st:params.st}})
            .then((result)=>{
              // console.log(result.result.docs);
              let code = 200;
              if (result.result.docs.length == 0) {
                  code = "404: There are no dealerships located in this state.";
              }
              resolve({
                  statusCode: code,
                  headers: { 'Content-Type': 'application/json' },
                  body: result.result.docs
              });
            }).catch((err)=>{
              reject({ 500: "Something went wrong on the server."});
            })
        } else if (params.id) {
            id = parseInt(params.dealerId)
            // return dealership with this state 
            cloudant.postFind({
              db: 'dealerships',
              selector: {
                id: parseInt(params.id)
              }
            })
            .then((result)=>{
              // console.log(result.result.docs);
              let code = 200;
              if (result.result.docs.length == 0) {
                  code = "404: This database is empty.";
              }
              resolve({
                  statusCode: code,
                  headers: { 'Content-Type': 'application/json' },
                  body: result.result.docs
              });
            }).catch((err)=>{
              reject({ 500: "Something went wrong on the server."});
            })
        } else {
            // return all documents 
            cloudant.postAllDocs({ db: 'dealerships', includeDocs: true })            
            .then((result)=>{
              // console.log(result.result.rows);
              let code = 200;
              if (result.result.rows.length == 0) {
                  code = "404: There are no documents to show.";
              }
              resolve({
                  statusCode: code,
                  headers: { 'Content-Type': 'application/json' },
                  body: result.result.rows
              });
            }).catch((err)=>{
              reject({ 500: "Something went wrong on the server."});
            })
      }
    }
    )}