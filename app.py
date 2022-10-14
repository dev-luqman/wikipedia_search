import json
import click
import wikipedia

# prints when function loads
print('Loading function')

@click.command()
@click.argument('entity')
def main(entity):
    ''' Wikipedia page summarizer.
        :param entity: a request with a wikipedia "entity" that has page information
        :return: a response that contains the first sentence of a wikipedia page,
            the response is JSON formatted.'''

    click.secho(f"Your Argument `{entity}`", bg="white", fg="black")

    # Set Status Code
    BAD_STATUS_CODE = 400
    GOOD_STATUS_CODE = 200 
    COLOR_CODE = 'green'

    # Exception handling
    try:
        res = wikipedia.summary(entity, sentences=1)
        statusCode = GOOD_STATUS_CODE
    except wikipedia.exceptions.PageError:
        res= f'\nThis word -{entity}- does not exist!\n'
        COLOR_CODE = 'red'
        statusCode = BAD_STATUS_CODE
    except wikipedia.exceptions.DisambiguationError: 
        statusCode = BAD_STATUS_CODE
        COLOR_CODE = 'red'
        res = f'\nThere are multiple references to this word {entity}!\n'
    except:
        statusCode = BAD_STATUS_CODE
        COLOR_CODE = 'red'
        res = "\nSorry, Cannot Handle this request!\n"

    # print statements
    click.secho("WIkI Response is", fg=COLOR_CODE)
    click.secho(res, blink=True, bold=True)
    
    ## TO DO: Format the response as JSON and return the result
    response = {
        "statusCode": statusCode, 
        # "headers": { "Content-type": "application/json" },
        "body": json.dumps({"message": res})
    }
    
    return response

if __name__=="__main__":
    main()