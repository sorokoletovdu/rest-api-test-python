ENDPOINT = "/ihrebank"


def has_nested_key(data, keys):
    """
    Check if a nested dictionary has a specific path of keys.

    :param data: The dictionary to check.
    :param keys: A list of keys representing the path.
    :return: True if all keys are found in the specified path, False otherwise.
    """
    if not isinstance(data, dict) or not keys:
        return False
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return False
    return True


def get_browsers_with_missed_or_incorrect_min_field(data):
    """
    Checks all browsers in the given data
    and return non-empty list if the 'min' key is missed or is None for any browsers.
    """
    failed_browsers = []
    if isinstance(data, dict):
        for platform, operationSystems in data.items():
            if isinstance(operationSystems, dict):
                for operationSys, browsers in operationSystems.items():
                    if isinstance(browsers, dict):
                        for browserName, browserParams in browsers.items():
                            if isinstance(browserParams, dict):
                                if 'min' in browserParams:
                                    if browserParams['min'] is None:
                                        failed_browsers.append(
                                            f"'min' key is None for {platform}->{operationSys}->{browserName}")
                                else:
                                    failed_browsers.append(
                                        f"'min' key is missing for {platform}->{operationSys}->{browserName}")
    return failed_browsers


def test_get_response_fields(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200

    data = response.json()

    # Check if required fields are in the response
    assert has_nested_key(data, ['settings', 'idnow', 'autoident', 'web', 'browserSupportMatrix'])
    matrix = data['settings']['idnow']['autoident']['web']['browserSupportMatrix']

    assert get_browsers_with_missed_or_incorrect_min_field(matrix) == []
