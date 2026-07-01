# Honeypot Dashboard

Projeto acadêmico desenvolvido para as disciplinas de Programação para Redes e Laboratório de Programação.

O objetivo do projeto é automatizar a implantação de uma honeypot SSH utilizando o Cowrie, processar os logs gerados utilizando Python e apresentar as informações em um painel web desenvolvido com Flask.

Todo o ambiente é provisionado automaticamente utilizando Ansible, permitindo que qualquer pessoa reproduza o projeto com apenas um comando.

---

# Autores

- Fabio Yamauchi
- Kaique Pinheiro

Curso: Redes de Computadores

Instituição: IFMT

---

# Objetivos do projeto

- Automatizar a instalação do ambiente utilizando Ansible.
- Implantar automaticamente a honeypot Cowrie.
- Coletar eventos de ataques SSH.
- Processar os logs utilizando Python.
- Exibir as informações em um Dashboard Web desenvolvido com Flask.

---

# Arquitetura do projeto

```
                Atacante
                    │
                    ▼
              Cowrie Honeypot
                    │
                    ▼
             cowrie.json (logs)
                    │
                    ▼
              Python (parser)
                    │
                    ▼
             Dashboard Flask
                    │
                    ▼
          http://localhost:5000
```

---

# Ambiente utilizado

| Componente | Versão |
|------------|---------|
| Sistema Operacional | Ubuntu 24.04.4 LTS (WSL2) |
| Python | 3.12.3 |
| Ansible | Core 2.16.3 |
| Git | 2.43.0 |
| Flask | 3.1.3 |
| Cowrie | Commit 7e0fd081 |

---

# Estrutura do projeto

```
honeypot-dashboard/

├── ansible/
│   └── site.yml
│
├── monitor/
│   └── app.py
│
├── logs/
│
├── reports/
│
├── services/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Instalação do ambiente

## 1. Instalar o WSL (Windows)

Abra o PowerShell como Administrador.

```powershell
wsl --install
```

Reinicie o computador quando solicitado.

Verifique a instalação:

```powershell
wsl --status
```

---

## 2. Atualizar o Ubuntu

Abra o Ubuntu e execute:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 3. Instalar as dependências iniciais

O projeto utiliza Ansible para automatizar toda a instalação, porém algumas ferramentas precisam existir previamente.

```bash
sudo apt install git ansible python3 python3-pip python3-venv -y
```

---

## 4. Clonar o projeto

```bash
git clone https://github.com/ftyamauchi/Honeypot-Dashboard.git
```

Entre na pasta do projeto:

```bash
cd Honeypot-Dashboard
```

---

## 5. Executar o projeto

Execute apenas um comando:

```bash
ansible-playbook ansible/site.yml --ask-become-pass
```

O Ansible será responsável por:

- instalar dependências adicionais;
- baixar automaticamente o Cowrie;
- criar os ambientes virtuais;
- instalar o Flask;
- iniciar o Cowrie;
- iniciar o Dashboard.

---

# Acessando o Dashboard

Após a execução do playbook, abra:

```
http://localhost:5000
```

A página é atualizada automaticamente a cada 3 segundos.

---

# Funcionalidades

O Dashboard apresenta:

- Status do Cowrie
- Quantidade total de eventos registrados
- IPs identificados
- Usuários utilizados
- Senhas testadas
- Comandos executados
- Última atividade registrada

---

# Como testar

Abra outro terminal e execute:

```bash
ssh root@localhost -p 2222
```

No primeiro acesso confirme a chave:

```
yes
```

Utilize qualquer senha.

Exemplos:

```
123456
password
admin
```

Após autenticar, execute alguns comandos:

```bash
ls
pwd
whoami
uname -a
cat /etc/passwd
exit
```

Retorne ao Dashboard.

Após alguns segundos os novos eventos aparecerão automaticamente.

---

# Problemas comuns

## Erro de chave SSH

Caso apareça uma mensagem informando que a chave do servidor mudou:

```bash
ssh-keygen -R "[localhost]:2222"
```

Depois conecte novamente:

```bash
ssh root@localhost -p 2222
```

---

# Tecnologias utilizadas

- Python
- Flask
- Ansible
- Cowrie Honeypot
- Git
- GitHub
- WSL2
- Ubuntu Linux

---

# Objetivo acadêmico

Este projeto demonstra a utilização de Infraestrutura como Código (IaC) aplicada à Segurança da Informação.

Durante o desenvolvimento foram utilizados conceitos de:

- Automação de infraestrutura
- Honeypots
- Monitoramento de eventos
- Processamento de logs
- Desenvolvimento Web
- Ambientes virtuais Python
- Controle de versão com Git

---

# Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
