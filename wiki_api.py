from flask import Flask, request, abort, jsonify
import wikipedia
from flask_cors import CORS

app = Flask(__name__)

res = ''

"""
@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
"""
CORS(app)

"""
@TODO: Use the after_request decorator to set Access-Control-Allow
"""
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

"""
@TODO:
Create an endpoint to handle GET requests
Doc: welcome page
"""
@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "success": True,
            "categories": "welcome back to wiki search",
        }
    )


"""
@TODO:
Create an endpoint to POST a new question,
"""
@app.route("/search", methods=["POST"])
def wiki_search():
    body = request.get_json()
    entity = body.get("entity", None)

    # Set Status Code
    BAD_STATUS_CODE = 400
    GOOD_STATUS_CODE = 200

    # Exception handling
    try:
        res = wikipedia.summary(entity, sentences=1)
        statusCode = GOOD_STATUS_CODE 
            ## TO DO: Format the response as JSON and return the result
        return ({
            "statusCode": statusCode, 
            "success": True,
            "headers": { "Content-type": "application/json" },
            "message": f"\n${entity} ->  ${res}\n"
        })
    except wikipedia.exceptions.PageError:
        res= f'\nThis word -{entity}- does not exist!\n'
        abort(404)
    except wikipedia.exceptions.DisambiguationError:
        res = f'\nThere are multiple references to this word {entity}!\n'
        abort(422)
    except:
        res = "\nSorry, Cannot Handle this request!\n"
        abort(404)


"""
@TODO:
Error Handling
"""
@app.errorhandler(422)
def unprocessable():
    return jsonify({
    "success": False, 
    "headers": { "Content-type": "application/json" },
    "error": 422,
    "message": res
    }), 422

@app.errorhandler(404)
def not_found():
    return jsonify({
    "success": False, 
    "headers": { "Content-type": "application/json" },
    "error": 404,
    "message": res
    }), 404

# @app.errorhandler(400)
# def unprocessable(error):
#     return jsonify({
#     "success": False, 
#     "error": 400,
#     "message": res
#     }), 400

@app.errorhandler(405)
def not_allowed_method():
    return jsonify({
    "success": False, 
    "error": 405,
    "message": "method not allowed"
    }), 405


if __name__ == "__main__":
    app.run(debug=True)