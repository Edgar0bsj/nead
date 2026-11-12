from src.modules.acessibilidade.acess_created import AcessCreated
from src.modules.acessibilidade.acess_deleted import AcessDeleted
from src.modules.acessibilidade.acess_export import AcessExport
from src.modules.acessibilidade.acess_finds import AcessFinds
from src.modules.acessibilidade.acess_init import AcessInit
from src.modules.acessibilidade.acess_read_csv import AcessReadCsv
from src.modules.acessibilidade.acess_updated import AcessUpdated


class AcessibilidadeLoad(
    AcessInit,
    AcessCreated,
    AcessReadCsv,
    AcessUpdated,
    AcessFinds,
    AcessDeleted,
    AcessExport,
):
    def __init__(self):
        AcessInit.__init__(self)
        AcessReadCsv.__init__(self)
        AcessCreated.__init__(self)
        AcessUpdated.__init__(self)
        AcessFinds.__init__(self)
        AcessDeleted.__init__(self)
        AcessExport.__init__(self)
