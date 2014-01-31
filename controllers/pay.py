import paypalrestsdk
import logging


class Payment(object):

    def __init__(self):
        paypalrestsdk.configure({
            "mode": "sandbox", # sandbox or live
            "client_id": "AQzn8hB4hoxGQ8Wzbk_fWYfMjv6VuSvgoxkMaR17G3RzTnYwzgS8MyKt7nt3",
            "client_secret": "EAkBLhAIJIdOyDknywXMidAaFYGfECDDJKwy21f5AoJ8hdltWzYrM59RgNUl" })
    
    def create(self):
        import logging
        logging.basicConfig(level=logging.INFO)
        
        # ###Payment
        # A Payment Resource; create one using
        # the above types and intent as 'sale'
        payment = paypalrestsdk.Payment({
          "intent": "sale",
        
          # ###Payer
          # A resource representing a Payer that funds a payment
          # Payment Method as 'paypal'
          "payer": {
            "payment_method": "paypal" },
        
          # ###Redirect URLs
          "redirect_urls": {
            "return_url": "http://127.0.0.1:8000/paypal_cpbr7/default/sucesso",
            "cancel_url": "http://127.0.0.1:8000/paypal_cpbr7/default/recusado" },
        
          # ###Transaction
          # A transaction defines the contract of a
          # payment - what is the payment for and who
          # is fulfilling it.
          "transactions": [ {
        
            # ### ItemList
            "item_list": {
              "items": [{
                "name": "item",
                "sku": "item",
                "price": "5.00",
                "currency": "BRL",
                "quantity": 1 }]},
        
            # ###Amount
            # Let's you specify a payment amount.
            "amount": {
              "total": "5.00",
              "currency": "BRL" },
            "description": "This is the payment transaction description." } ] } )
        
        # Create Payment and return status
        if payment.create():
          print("Payment[%s] created successfully"%(payment.id))
          return payment.id ###
          # Redirect the user to given approval url
          for link in payment.links:
            if link.method == "REDIRECT":
              redirect_url = link.href
              print("Redirect for approval: %s"%(redirect_url))
        else:
          print("Error while creating payment:")
          print(payment.error)      
      
    def execute(self, payment_id):
        payment = paypalrestsdk.Payment.find(payment_id)
    
        if payment.execute({"payer_id": "DUFRQ8GWYMJXC"}):
          print("Payment execute successfully")
        else:
          print(payment.error) # Error Hash