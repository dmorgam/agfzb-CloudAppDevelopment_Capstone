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
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


credentials = {
    "COUCH_URL": "",
    "IAM_API_KEY": "",
    "COUCH_USERNAME": ""
}

def main(dict):
    try:
        client = Cloudant.iam(
            account_name=credentials["COUCH_USERNAME"],
            api_key=credentials["IAM_API_KEY"],
            connect=True,
        )
        
    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err }

    if "review" in dict.keys():
        reviews = client['reviews']
        
        my_document = reviews.create_document(dict['review'])

        # Check that the document exists in the database
        if my_document.exists():
            return my_document
        
    else:
        return {"err": 'No params.' }
