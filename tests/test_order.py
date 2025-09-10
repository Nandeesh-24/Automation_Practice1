import pytest


@pytest.mark.api
def test_create_order(client):
    payload = {'orders': [{'country': "India", 'productOrderedId': "68a961459320a140fe1ca57a"}]}

    order_response = client.post('/api/ecom/order/create-order', json=payload)
    assert order_response.status_code == 201

    assert order_response.json()['message'] == "Order Placed Successfully"

    order_id = order_response.json()['orders'][0]

    order_details = client.get('/api/ecom/order/get-orders-details', params={'id': order_id})

    assert order_details.status_code == 200

    assert order_details.json()['data']['_id'] == order_id
