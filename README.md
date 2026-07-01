# Honeypot Dashboard

Projeto acadêmico desenvolvido para as disciplinas de Programação para Redes e Laboratório de Programação.

O projeto demonstra como automatizar a implantação de uma honeypot SSH utilizando o Cowrie, processar os logs gerados com Python e apresentar as informações em um painel web desenvolvido com Flask.

---

## Objetivo

Automatizar todo o ambiente utilizando Ansible para que qualquer pessoa consiga reproduzir o projeto executando apenas um comando.

O sistema realiza:

- Implantação automática do Cowrie Honeypot
- Processamento dos logs em Python
- Visualização das informações em um painel web
- Monitoramento básico de tentativas de acesso SSH

---

## Tecnologias utilizadas

- Python 3
- Flask
- Ansible
- Cowrie Honeypot
- Git
- GitHub
- Linux (WSL)

---

## Estrutura do projeto

```
honeypot-dashboard/
│
├── ansible/
│   └── site.yml
│
├── config/
│
├── docs/
│
├── logs/
│
├── monitor/
│   ├── app.py
│   └── venv/
│
├── reports/
│
├── services/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Arquitetura

```
Atacante
     │
     ▼
Cowrie Honeypot
     │
     ▼
cowrie.json
     │
     ▼
Python
     │
     ▼
Flask
     │
     ▼
Dashboard Web
```

---

## Funcionalidades

O painel apresenta em tempo real:

- Status do Cowrie
- Total de eventos registrados
- IPs identificados
- Usuários utilizados
- Senhas utilizadas
- Comandos executados
- Última atividade registrada

A página é atualizada automaticamente a cada 3 segundos.

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/ftyamauchi/Honeypot-Dashboard.git
```

Entre na pasta do projeto:

```bash
cd Honeypot-Dashboard
```

Execute o playbook:

```bash
ansible-playbook ansible/site.yml --ask-become-pass
```

Ao finalizar, abra no navegador:

```
http://localhost:5000
```

---

## Como testar

Em outro terminal execute:

```bash
ssh root@localhost -p 2222
```

Caso seja o primeiro acesso, confirme a chave digitando:

```
yes
```

Em seguida, tente autenticar utilizando qualquer senha.

Exemplo:

```
123456
password
admin
```

Após o login, execute alguns comandos:

```bash
ls
pwd
whoami
uname -a
cat /etc/passwd
exit
```

O painel será atualizado automaticamente com as novas informações.

---

## Caso apareça erro de chave SSH

Se o SSH informar que a chave do servidor mudou, execute:

```bash
ssh-keygen -R "[localhost]:2222"
```

Depois tente novamente:

```bash
ssh root@localhost -p 2222
```

---

## Fluxo de funcionamento

1. O Ansible prepara o ambiente.
2. O Cowrie é instalado e iniciado.
3. O Cowrie registra os eventos em `cowrie.json`.
4. O Python lê os logs continuamente.
5. O Flask apresenta as informações em um painel web.

---

## Objetivo acadêmico

Este projeto foi desenvolvido para demonstrar a integração entre:

- Infraestrutura como Código (IaC)
- Automação com Ansible
- Honeypots
- Processamento de logs com Python
- Desenvolvimento Web com Flask

---

## Autor

Fabio Yamauchi

Curso: Redes de Computadores

Instituição: IFMT
