# Analisador de Sentimento de Tweets

Este projeto realiza a análise de sentimento de tweets utilizando um modelo de aprendizado de máquina treinado com dados do Twitter. O objetivo é classificar os tweets em três categorias: Negativo, Neutro e Positivo.

## Estrutura do Projeto

- `notebooks/jup.ipynb`: Jupyter Notebook contendo o código de treinamento e avaliação dos modelos de aprendizado de máquina.
- `data/Twitter_Data.csv`: Dataset utilizado para treinar e testar os modelos.
- `projeto-web/templates/index.html`: Template HTML para a interface web.
- `projeto-web/static/styles.css`: Arquivo de estilo CSS para a interface web.
- `projeto-web/main.py`: Código principal da aplicação web utilizando Flask.
- `modelo.pkl`: Modelo treinado salvo.
- `vectorizer.pkl`: Vetorizador TF-IDF salvo.

## Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- Flask
- Jupyter Notebook
- Matplotlib e Seaborn para visualização de dados
- Plotly para gráficos interativos

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação web:
    ```bash
    python projeto-web/main.py
    ```

4. Acesse a aplicação em seu navegador:
    ```
    http://127.0.0.1:5000/
    ```

## Dataset

O dataset utilizado neste projeto foi obtido do Kaggle e contém tweets rotulados com sentimentos. As colunas principais são:

- `clean_text`: Texto do tweet.
- `category`: Sentimento associado ao tweet (-1: Negativo, 0: Neutro, 1: Positivo).

## Treinamento do Modelo

O modelo foi treinado utilizando Regressão Logística e Naive Bayes. A vetorização dos textos foi feita utilizando TF-IDF. O código de treinamento e avaliação dos modelos está disponível no notebook `notebooks/jup.ipynb`.

## Interface Web

A interface web permite que o usuário insira um texto em inglês e obtenha a análise de sentimento correspondente. A aplicação utiliza Flask para renderizar o template HTML e exibir o resultado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
