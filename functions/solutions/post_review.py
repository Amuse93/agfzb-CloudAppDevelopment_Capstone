#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

couch_url="https://211aa84b-7857-450e-af82-2787c051a6d6-bluemix.cloudantnosqldb.appdomain.cloud"
iam_api_key='XN_veGIw251yhJtaBLID2FmTIJgqlmvEthLCZmFeBxpM'
couch_username="211aa84b-7857-450e-af82-2787c051a6d6-bluemix"

def main(dict):
    authenticator = IAMAuthenticator(iam_api_key)
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(couch_url)
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
        # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
            'statusCode': 404,
            'message': 'Something went wrong on the server'
        }
