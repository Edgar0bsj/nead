# Estrutura de Análise de Dados com Pandas e API

## Objetivo
Este projeto tem como finalidade realizar análises de dados utilizando **Pandas** em planilhas, estruturando as principais **features** e disponibilizando os resultados por meio de uma **API** simples e escalável.  
A ideia é manter uma arquitetura clara, modular e profissional, que facilite manutenção e evolução futura.

---

## Conceito da Arquitetura

1. **Camada de Ingestão**  
   - Responsável por carregar dados de planilhas (CSV, Excel, etc.).  
   - Centraliza a lógica de leitura e pré-processamento inicial.

2. **Camada de Processamento**  
   - Utiliza **Pandas** para limpeza, transformação e criação de features.  
   - Mantém funções organizadas e reutilizáveis para diferentes análises.

3. **Camada de Features**  
   - Estrutura os indicadores e métricas que serão expostos.  
   - Garante consistência e padronização dos resultados.

4. **Camada de API**  
   - Disponibiliza os resultados das análises em endpoints REST.  
   - Permite integração com sistemas externos e aplicações front-end.

---

## Princípios da Estrutura

- **Simplicidade**: código modular e fácil de entender.  
- **Escalabilidade**: preparado para crescer conforme novas features forem adicionadas.  
- **Profissionalismo**: documentação clara, organização de pastas e padronização de nomenclaturas.  
- **Reutilização**: funções genéricas que podem ser aplicadas em diferentes análises.  
- **Separação de responsabilidades**: cada camada cuida de uma parte específica do fluxo.

---

## Estrutura de Pastas (conceitual)

```
project/
│── data/              # Planilhas e arquivos brutos
│── notebooks/         # Exploração inicial e protótipos
│── src/
│   ├── ingestion/     # Funções de leitura e carregamento
│   ├── processing/    # Transformações e cálculos com Pandas
│   ├── features/      # Definição das métricas e indicadores
│   └── api/           # Endpoints para disponibilizar resultados
│── README.md          # Documentação do projeto
```

---

## Fluxo de Trabalho

1. **Carregar dados** → ingestão de planilhas.  
2. **Processar dados** → limpeza, normalização e cálculos.  
3. **Gerar features** → métricas e indicadores prontos para uso.  
4. **Expor via API** → endpoints REST para consumo externo.  
