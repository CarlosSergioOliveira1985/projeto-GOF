from abc import ABC, abstractmethod

class Order:
    """ Context"""
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self)-> None:
        print("Tentando executar pending()")
        self.state.pending()
        print("Estado atual: ", self.state)
        print()

    def approve(self)-> None:
        print("Tentando executar approve()")
        self.state.approve()
        print("Estado atual: ", self.state)
        print()

    def reject(self)-> None:
        print("Tentando executar reject()")
        self.state.reject()        
        print("Estado atual: ", self.state)
        print()

class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self):
        return self.__class__.__name__

class PaymentPending(OrderState):
    # def __init__(self, order: Order) -> None:
    #     self.order = order

    def pending(self) -> None:
        print('Pagamento ja pendente, não posso fazer nada')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print("Pagamento aprovado")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")

class PaymentApproved(OrderState):
    # def __init__(self, order: Order) -> None:
    #     self.order = order

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("Pagamento pendente")

    def approve(self) -> None:
        print('Pagamento já aprovado, não posso fazer nada')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")
    
class PaymentRejected(OrderState):
    # def __init__(self, order: Order) -> None:
    #     self.order = order

    def pending(self) -> None:
        print('Pagamento não pode mais ir para pendente, pagamento recusado')


    def approve(self) -> None:
        print('Pagamento não pode mais ir para aprovado, pagamento recusado')

    def reject(self) -> None:
        print('Pagamento já recusado, não posso fazer nada')

if __name__ == "__main__":

    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.approve()
    order.pending()
    order.reject()
