from allstores.user import get_user
from allstores.orders import get_order_user

if __name__ == "__main__":
    print(get_user(1))
    print(get_order_user(1))