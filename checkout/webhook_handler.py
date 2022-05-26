from django.http import HttpResponse



class StripeWH_Handler:
    
    def __init__(self, request):
        self.requestm = request
        

    def handle_event(self, event):
        
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status = 200)
        
        
    def handle_payment_intent_succeeded(self, event):
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status = 200)
        
        
    def handle_payment_intent_failed(self, event):
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status = 200)
        