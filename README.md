# Conversao_Decimal

Este é um projeto de conversão de números decimais para binário, octal ou hexadecimal desenvolvido em Flask.

## Estrutura do Projeto

O projeto consiste em três arquivos principais:

1. `app.py`: Este arquivo Python contém o código do aplicativo Flask, incluindo a lógica de conversão e as rotas para renderizar as páginas HTML.

2. `templates/index.html`: Este arquivo HTML contém a estrutura da página inicial do aplicativo, incluindo o formulário para entrada do número decimal e a exibição do resultado.

3. `static/style.css`: Este arquivo CSS contém as regras de estilo que definem a aparência da página HTML.

## Funcionalidades

- Os usuários podem inserir um número decimal e escolher o tipo de conversão (binário, octal ou hexadecimal).
- Ao clicar no botão "Calcular", o aplicativo realiza a conversão e exibe o resultado na mesma página.
- Os usuários também têm a opção de limpar o resultado clicando no botão "Limpar".

## Como Utilizar

Para utilizar este projeto, siga estas etapas:

1. Clone este repositório:

```bash
git clone https://github.com/seu_usuario/conversao-decimal-flask.git
```

2. Navegue até o diretório:

```bash
cd conversao-decimal-flask
```

3. Execute o aplicativo:

```bash
python app.py
```

4. Abra um navegador da web e acesse o seguinte endereço:

```bash
http://localhost:5000
```