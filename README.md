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

# Fluxo de Desenvolvimento

- [x] TURMA -> G - 2026.1.1.3P - Análise e Des. de Sistemas
- [x] DISCIPLINA -> Ciências do Ambiente
- [x] NOME_PROFESSOR -> Alan Jeferson de Oliveira da Silva 
Aqui está um modelo de **README conceitual** para documentar o fluxo de trabalho da planilha **Analise_base.xlsx**, com explicação passo a passo e sugestões de melhorias para deixar o processo mais robusto e profissional:

---

# Fluxo de Análise — Analise_base.xlsx

### 1. **Filtro**
Aplicar filtros iniciais para selecionar apenas os registros relevantes:
- **POLO** → Nova Iguaçu  
- **MODALIDADE** → G  
- **ENTRADA** → 2  

---

### 2. **Colunas novas**
Adicionar colunas derivadas para enriquecer os dados:
- **CURSO** → Farmácia  
- **PERIODO** → 1  

---

### 3. **Capturar colunas de interesse**
Selecionar apenas os campos relevantes para análise:
- **TURMA**, **DISCIPLINA**, **NOME_PROFESSOR**, **CURSO**, **PERIODO**

---

### 4. **Retirar duplicatas com offset**
Remover registros duplicados considerando:
- **TURMA**, **DISCIPLINA**, **NOME_PROFESSOR**, **CURSO**, **PERIODO**

---

### 5. **Mapper**
Padronizar valores de colunas:
- **CURSO** → "Farmácia" convertido para **"FARM."**

---

### 6. **Tratar coluna PERIODO**
Normalizar o tipo de dado:
- Converter para **INT padrão**

---

### 7. **Resultado final**
Dataset final com colunas organizadas:
- **TURMA**, **CURSO**, **PERIODO**, **DISCIPLINA**, **NOME_PROFESSOR**
