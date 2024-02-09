# NLW Expert - Trilha de Python

Esta trilha de Python que durou 3 dias teve como objetivo implementar uma aplicação Flask que gera um `png` com o código de barras a partir de um código de produto.

Neste projeto foram implementados:

- O conceito de API
- Validadores
- Tratamento de erros HTTP
- Testes unitários
- Estruturação de projeto
- Documentação

## Para executar o projeto

Para executar o projeto é necessário ter o gerenciador de bibliotecas [Poetry](https://python-poetry.org) para instalar as bibliotecas que o projeto depende.

Com o poetry disponível, execute os passos:

1. Clone o repositório
```bash
git clone https://github.com/RWallan/nlw-rocketset.git
```

2. Navegue até o diretório
```bash
cd nlw-rocketset
```

3. Instale as dependências

```bash
poetry install # --without dev caso não queira instalar as bibliotecas de desenvolvimento
```

4. Execute o projeto
```
poetry run python run.py
```

Com o servidor no ar, você pode enviar uma requisição `POST` para a rota `http://localhost.com/3000/create_tag`.

A rota trará uma resposta, em caso de sucesso, com o seguinte schema:

```bash
{
    {
	"data": {
		"count": 1,
		"path": "sua_tag.png"
		"type": "Tag Image"
	}
}
}
```
