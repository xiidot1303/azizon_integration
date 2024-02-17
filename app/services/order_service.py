from app.utils import send_request
from config import API_URL

def get_order_by_id(order_id: str):
    url = API_URL + '/get/order-by-id'
    data = {
        'order_id': order_id
    }
    content, headers = send_request(url, data, type='post')
    return content['orders'][0] if content['orders'] else None

def payme_accept_order(order_id):
    url = API_URL + '/payme/accept-order'
    data = {
        'order_id': order_id
    }
    content, headers = send_request(url, data, type='post')
    return content