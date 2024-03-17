import data
import sender_stand_request

def test_create_order_and_get_order_by_track():
    order = data.create_order_request.copy()
    create_order_response = sender_stand_request.create_new_order(order)

    trackId = create_order_response.json()["track"]

    get_order_params = data.get_order_request.copy()
    get_order_params["t"] = trackId

    response = sender_stand_request.get_order(get_order_params)

    assert response.status_code == 200