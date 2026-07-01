# Honeypot Dashboard

Projeto desenvolvido como trabalho interdisciplinar para as disciplinas de Programação para Redes (Infraestrutura como Código - IaC) e Laboratório de Programação (Python), sob orientação do Prof. João Preti.

O projeto demonstra como automatizar a implantação de um ambiente de monitoramento utilizando Ansible, Python e Cowrie Honeypot. Toda a infraestrutura pode ser provisionada por meio de um único comando, seguindo os princípios de Infraestrutura como Código (IaC).

## Objetivos

- Automatizar a instalação de todas as dependências do ambiente.
- Implantar o Honeypot Cowrie para simulação de um servidor SSH.
- Criar automaticamente os ambientes virtuais Python.
- Executar o dashboard desenvolvido em Flask.
- Exibir em tempo real os eventos registrados pelo honeypot.
- Demonstrar a integração entre automação (Ansible) e desenvolvimento Python.

---

# Tecnologias Utilizadas

- Ubuntu 24.04 LTS
- WSL2 (Windows)
- Ansible
- Python 3
- Flask
- Cowrie Honeypot
- Git

---

# Estrutura do Projeto

```
Honeypot-Dashboard/
│
├── ansible/
│   ├── site.yml
│   ├── stop.yml
│   └── roles/
│
├── cowrie/
│
├── monitor/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── README.md
└── requirements.txt
```

---

# Preparação do Ambiente

## Sistema Operacional

O projeto foi desenvolvido utilizando:

- Ubuntu 24.04 LTS

Caso utilize Windows, recomenda-se instalar o Ubuntu através do WSL2.

---

# Instalação do WSL

Abra o PowerShell como Administrador.

Verifique se já existe alguma instalação do Ubuntu:

```powershell
wsl --list --verbose
```

Caso queira começar completamente do zero:

```powershell
wsl --unregister Ubuntu
```

Instale o Ubuntu 24.04 LTS:

```powershell
wsl --install -d Ubuntu-24.04
```

Após a instalação:

Reinicie o computador.

Verifique o status:

```powershell
wsl --status
```

Abra o Ubuntu pelo Menu Iniciar.

Na primeira execução será solicitado:

- Nome do usuário
- Senha

Essa senha será utilizada posteriormente pelo comando sudo e pelo Ansible.

---

# Atualização do Ubuntu

Dentro do terminal do Ubuntu execute:

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Instalação das Dependências

Instale todas as ferramentas necessárias:

```bash
sudo apt install git ansible python3 python3-pip python3-venv -y
```

Verifique as versões instaladas:

```bash
git --version

ansible --version

python3 --version

pip3 --version
```

---

# Clonando o Projeto

Clone o repositório:

```bash
git clone https://github.com/ftyamauchi/Honeypot-Dashboard.git
```

Entre na pasta:

```bash
cd Honeypot-Dashboard
```

---

# Provisionamento da Infraestrutura

Todo o ambiente é criado utilizando um único comando:

```bash
ansible-playbook ansible/site.yml --ask-become-pass
```

ou

```bash
ansible-playbook ansible/site.yml -K
```

Será solicitada a senha do usuário Ubuntu.

Essa senha é necessária para que o Ansible possa utilizar privilégios administrativos (sudo) durante a instalação.

Durante a execução do playbook são realizadas automaticamente as seguintes tarefas:

- Atualização dos pacotes do sistema.
- Instalação das dependências.
- Criação dos ambientes virtuais Python.
- Instalação do Cowrie.
- Instalação das bibliotecas Python.
- Configuração do Honeypot.
- Inicialização do Cowrie.
- Inicialização do Dashboard Flask.

Toda a infraestrutura é provisionada automaticamente.

---

# Acessando o Dashboard

Após o término do playbook, abra um navegador e acesse:

```
http://localhost:5000
```

ou

```
http://127.0.0.1:5000
```

---

# Funcionamento do Dashboard

O painel foi desenvolvido em Python utilizando Flask.

Sempre que uma requisição é realizada:

- o arquivo de logs do Cowrie é lido;
- cada evento é processado;
- as informações são organizadas;
- as estatísticas são atualizadas;
- os dados são enviados para a interface web.

O painel apresenta informações como:

- Quantidade de eventos registrados;
- IPs de origem;
- Usuários utilizados nas tentativas de login;
- Senhas testadas;
- Comandos executados pelos atacantes.

---

# Atualização em Tempo Real

A interface é atualizada automaticamente a cada três segundos através da seguinte instrução presente no HTML:

```html
<meta http-equiv="refresh" content="3">
```

Dessa forma não é necessário atualizar a página manualmente.

---

# Funcionamento do Python

O arquivo principal da aplicação é:

```
monitor/app.py
```

Ele é responsável por:

- iniciar o servidor Flask;
- localizar o arquivo de logs do Cowrie;
- ler cada linha do arquivo JSON;
- interpretar os eventos registrados;
- gerar as estatísticas utilizadas pelo dashboard;
- disponibilizar as informações para a interface web.

---

# Ambientes Virtuais

Durante o provisionamento, o Ansible cria ambientes virtuais separados para evitar conflitos entre dependências.

São utilizados ambientes distintos para:

- Cowrie
- Dashboard Flask

Essa separação facilita futuras atualizações e manutenção do projeto.

---

# Gerando Eventos

Após iniciar o projeto, basta realizar uma tentativa de conexão SSH para gerar registros.

Exemplo:

```bash
ssh teste@localhost
```

ou

```bash
ssh root@localhost
```

Cada tentativa será registrada pelo Cowrie e aparecerá automaticamente no dashboard.

---

# Encerrando os Serviços

Para interromper o ambiente execute:

```bash
ansible-playbook ansible/stop.yml
```

---

# Conceitos Demonstrados

Este projeto demonstra na prática os seguintes conceitos:

- Infraestrutura como Código (IaC)
- Automação com Ansible
- Provisionamento automatizado
- Ambientes virtuais Python
- Honeypots
- Monitoramento de eventos
- Leitura e processamento de arquivos JSON
- Desenvolvimento Web com Flask
- Integração entre automação e programação

---

# Autores

Fabio Yamauchi

Kaique Pinheiro

---

# Orientação

Prof. João Preti

---

# Licença

Este projeto foi desenvolvido para fins acadêmicos nas disciplinas de Programação para Redes e Laboratório de Programação.
