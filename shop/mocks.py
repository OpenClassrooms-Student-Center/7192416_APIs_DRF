import requests

ECOSCORE_GRADE = 'z'


def mock_openfoodfact_success(self, method, url):

    def monkey_json():
        return {
            'product': {
                'ecoscore_grade': ECOSCORE_GRADE
            }
        }

    response = requests.Response()
    response.status_code = 200
    response.json = monkey_json
    return response
