from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import Base, Order
engine = create_engine('sqlite:///orders.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def process_order(order_d):
    #Your code here
    order = Order( sender_pk=order_d['sender_pk'],receiver_pk=order_d['receiver_pk'], buy_currency=order_d['buy_currency'], sell_currency=order_d['sell_currency'], buy_amount=order_d['buy_amount'], sell_amount=order_d['sell_amount'] )
    session.add(order)
    session.commit();
    buy_curr = order.buy_currency
    sell_curr = order.sell_currency
    buy_am = order.buy_amount
    sell_am = order.sell_amount
    send_pk = order.sender_pk
    receive_pk = order.receiver_pk
    exchange_rate = buy_am/sell_am
    existing = session.query(Order).filter(Order.filled == None, Order.buy_currency == order.sell_currency,Order.sell_currency == order.buy_currency, Order.sell_amount/Order.buy_amount >= exchange_rate).first()
    #filled
    existing.filled = datetime.now()
    order.filled = datetime.now()
    #counterparty id
    order.counterparty_id = existing.id
    existing.counterparty_id = order.id
    session.commit()
    #order can buy more
    if(existing.sell_amount < buy_am):
      new_buy = buy_am - existing.sell_amount
      new_sell = new_buy / exchange_rate
      #Insert the order
      order_obj = Order( sender_pk=order.sender_pk,receiver_pk=order.receiver_pk, buy_currency=order.buy_currency, sell_currency=order.sell_currency, buy_amount=new_buy, sell_amount=new_sell, creator_id = order.id)
      session.add(order_obj)
      session.commit()
    elif(existing.sell_amount>buy_am):
      new_sell = existing.sell_amount - buy_am
      new_buy = new_sell * existing.buy_amount/existing.sell_amount
      #Insert the order
      order_obj = Order( sender_pk=existing.sender_pk,receiver_pk=existing.receiver_pk, buy_currency=existing.buy_currency, sell_currency=existing.sell_currency, buy_amount=new_buy, sell_amount=new_sell, creator_id = existing.id)
      session.add(order_obj)
      session.commit()
