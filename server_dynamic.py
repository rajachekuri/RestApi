import constants
from main3 import Main
from flask import Flask, jsonify, request

main_instance = Main()

def run_rest_api_server():
    try:
        app = Flask(__name__)

        @app.route("/")
        def index():
            return "hello!"

        @app.route("/cycles", methods=['GET'])
        def get_cycles():
            limit = request.args.get('limit')  # Get the 'limit' parameter from the GET request
            if limit is not None:
                limit = int(limit)
            main_instance.configsFromTable(limit)  # Pass the limit to the configsFromTable() method

            return jsonify({'cycles': constants.TABLE_MACHINECONFIGS})

        app.debug = True
        app.run(host=constants.JETSON_IP)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        main_instance.configsFromTable()
        run_rest_api_server()
    except Exception as e:
        print(e)
