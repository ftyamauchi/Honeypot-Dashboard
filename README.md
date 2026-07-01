# Honeypot Dashboard

Projeto acadêmico desenvolvido para as disciplinas de Programação para Redes e Laboratório de Programação.

O projeto utiliza Ansible para automatizar a implantação de uma honeypot SSH com Cowrie. Os logs gerados pelo Cowrie são lidos por um programa em Python e exibidos em um painel web simples feito com Flask.

---

# Autores

- Fabio Yamauchi
- Kaique Pinheiro

Curso: Redes de Computadores  
Instituição: Instituto Federal de Mato Grosso (IFMT)

---

# Objetivo do projeto

Demonstrar a integração entre:

- Infraestrutura como Código com Ansible
- Honeypot SSH com Cowrie
- Processamento de logs com Python
- Visualização dos dados em um painel Flask

---

# Arquitetura

```text
Atacante
   |
   v
Cowrie Honeypot
   |
   v
cowrie.json
   |
   v
Python
   |
   v
Flask Dashboard
   |
   v
http://localhost:5000
```

---

# Ambiente utilizado

Projeto desenvolvido e testado em:

| Componente | Versão |
|---|---|
| Sistema Operacional | Ubuntu 24.04.4 LTS |
| Ambiente | WSL2 |
| Python | 3.12.3 |
| Ansible | Core 2.16.3 |
| Git | 2.43.0 |
| Flask | 3.1.3 |
| Cowrie | Commit 7e0fd081 |

---

# Estrutura do projeto

```text
Honeypot-Dashboard/

├── ansible/
│   ├── site.yml
│   └── stop.yml
│
├── config/
├── docs/
├── logs/
├── monitor/
│   └── app.py
│
├── reports/
├── services/
├── README.md
└── .gitignore
```

Observação: a pasta `services/cowrie` não é enviada ao GitHub. Ela é criada automaticamente pelo Ansible durante a execução do projeto.

---

# Pré-requisitos

Para executar o projeto do zero, recomenda-se utilizar:

- Windows com WSL2 instalado
- Ubuntu 24.04 LTS no WSL
- Conexão com a internet
- Permissão de sudo no Ubuntu

---

# Instalação do WSL

No Windows, abra o PowerShell como administrador e execute:

```powershell
wsl --install
```

Após a instalação, reinicie o computador.

Verifique o WSL:

```powershell
wsl --status
```

Abra o Ubuntu pelo menu iniciar.

---

# Atualizar o Ubuntu

Dentro do Ubuntu/WSL, execute:

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Instalar dependências iniciais

Antes de rodar o projeto, instale Git, Ansible e Python:

```bash
sudo apt install git ansible python3 python3-pip python3-venv -y
```

---

# Clonar o projeto

```bash
git clone https://github.com/ftyamauchi/Honeypot-Dashboard.git
```

Entre na pasta:

```bash
cd Honeypot-Dashboard
```

---

# Iniciar o projeto

Execute:

```bash
ansible-playbook ansible/site.yml --ask-become-pass
```

Esse comando irá:

- instalar dependências do sistema;
- baixar o Cowrie automaticamente;
- criar o ambiente virtual do Cowrie;
- instalar o Cowrie;
- iniciar a honeypot;
- criar o ambiente virtual do painel;
- instalar Flask;
- iniciar o painel web.

Após a execução, acesse:

```text
http://localhost:5000
```

---

# Testar a honeypot

Em outro terminal, execute:

```bash
ssh root@localhost -p 2222
```

No primeiro acesso, o SSH pode perguntar se você confia na chave do servidor.

Digite:

```text
yes
```

Depois tente algumas senhas, por exemplo:

```text
123456
password
admin
```

Se o login for aceito, execute comandos como:

```bash
ls
pwd
whoami
uname -a
cat /etc/passwd
exit
```

O painel será atualizado automaticamente a cada 3 segundos.

---

# Erro de chave SSH

Se aparecer um erro dizendo que a chave SSH mudou, execute:

```bash
ssh-keygen -R "[localhost]:2222"
```

Depois tente conectar novamente:

```bash
ssh root@localhost -p 2222
```

Esse erro acontece quando o cliente SSH já tinha uma chave antiga salva para `localhost:2222`.

---

# Encerrar o projeto

Para parar o Cowrie e o painel Flask, execute:

```bash
ansible-playbook ansible/stop.yml
```

---

# O que aparece no painel

O painel mostra:

- status do Cowrie;
- total de eventos registrados;
- IPs encontrados;
- usuários utilizados;
- senhas testadas;
- comandos executados;
- última atividade registrada.

---

# Observação sobre o IP 127.0.0.1

Durante os testes locais, o IP exibido normalmente será:

```text
127.0.0.1
```

Esse IP representa o próprio computador local. Em um ambiente com outros dispositivos acessando a honeypot pela rede, o painel exibiria os IPs desses dispositivos.

---

# Finalidade

Projeto desenvolvido exclusivamente para fins acadêmicos.
