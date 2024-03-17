import configuration
import requests
import data


def create_new_order(order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order,
                         headers=data.headers)


def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                         params=track,
                         headers=data.headers)

