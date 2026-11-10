from src.service.acessibilidade_svc.acess_created import AcessCreated
from src.service.acessibilidade_svc.acess_load import AcessLoad


class AcessibilidadeController(AcessLoad, AcessCreated):
    def __init__(self):
        AcessLoad.__init__(self)
        AcessCreated.__init__(self)
