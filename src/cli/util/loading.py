from time import sleep
from tqdm import tqdm


def loading(temp:float=0.09):
    for _ in tqdm(
        iterable=range(100),
        desc= "CARREGANDO DADOS...",
        unit= "MB",colour="blue"
        ):

        sleep(temp)