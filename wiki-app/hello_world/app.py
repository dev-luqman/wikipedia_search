import json
import wikipedia

# prints when function loads
print('Loading function')


def lambda_handler(event, context):
    ''' Wikipedia page summarizer.
        :param event: a request with a wikipedia "entity" that has page information
        :return: a response that contains the first sentence of a wikipedia page,
            the response is JSON formatted.'''
    
    ## TO DO: Check that the request has some input body and save it
    if 'body' in event:
        event = json.loads(['body'])

    #save the entity request value
    entity = event['entity']

    # Set Status Code
    BAD_STATUS_CODE = 400
    GOOD_STATUS_CODE = 200 

    # Exception handling
    try:
        res = wikipedia.summary(entity, sentences=1)
        statusCode = GOOD_STATUS_CODE
    except wikipedia.exceptions.PageError:
        res= f'\nThis word -{entity}- does not exist!\n'
        statusCode = BAD_STATUS_CODE
    except wikipedia.exceptions.DisambiguationError: 
        statusCode = BAD_STATUS_CODE
        res = f'\nThere are multiple references to this word {entity}!\n'
    except:
        statusCode = BAD_STATUS_CODE
        res = "\nSorry, Cannot Handle this request!\n"

    # print statements
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    ## TO DO: Format the response as JSON and return the result
    response = {
        "statusCode": statusCode, 
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"message": res})
    }
    
    return response