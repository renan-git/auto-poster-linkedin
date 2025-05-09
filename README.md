## Auto Poster LinkedIn

Script em Python que automatiza a publicação de mensagens no LinkedIn utilizando Selenium.

#### Funcionalidades

- Login automático no LinkedIn
- Publicação de mensagens de texto no feed
- Interface simples via linha de comando


#### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/renan-git/auto-poster-linkedin.git
```

2. Acesse o diretório do projeto:
```bash
cd auto-poster-linkedin
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com suas credenciais:
```env
email_linkedin=seu_email@exemplo.com
password_linkedin=sua_senha
```

#### Como usar

Execute o script:
```bash
python main.py
```

O script irá:
1. Pedir a mensagem que deseja publicar
2. Fazer login automaticamente no LinkedIn
3. Publicar a mensagem no seu feed

#### Observações

- O script utiliza pausas (`time.sleep()`) para aguardar o carregamento dos elementos
- Certifique-se de ter o Google Chrome instalado
- Mantenha suas credenciais seguras no arquivo `.env` 
