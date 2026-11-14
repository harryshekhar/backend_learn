from allstores.user import get_user
from allstores.orders import get_order_user
from allstores.notification import send_mail

def get_user_profile(user_id :int) -> dict:
    return{"user" : get_user(user_id), "order" : get_order_user(user_id)}

def create_order(user_id: int, iteam:str) -> None:
    user = get_user(user_id)
    send_mail(user["email"], f"order is confirm{iteam}")
