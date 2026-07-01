# Manual de Instalação e Execução

## Honeypot Dashboard

## 1. Contexto

O Honeypot Dashboard é um projeto desenvolvido para a disciplina de Programação para Redes com foco em Infraestrutura como Código (IaC).

O ambiente é implantado automaticamente utilizando Ansible, permitindo instalar e configurar todos os componentes com um único comando.

---

## 2. Pré-requisitos

* Windows 10 ou Windows 11
* Conexão com a Internet
* Permissão de administrador no Windows

---

## 3. Instalação do WSL

Abra o PowerShell como Administrador.

Execute:

```powershell
wsl --install
```

Reinicie o computador.

Verifique a instalação:

```powershell
wsl --status
```

---

## 4. Instalação do Ubuntu 24.04 LTS

Caso o Ubuntu não tenha sido instalado automaticamente, liste as distribuições disponíveis:

```powershell
wsl --list --online
```

Instale o Ubuntu 24.04 LTS:

```powershell
wsl --install Ubuntu-24.04
```

Abra o Ubuntu pelo Menu Iniciar.

Na primeira execução será solicitado:

* Nome de usuário
* Senha

Essa senha será utilizada nos comandos `sudo`.

---

## 5. Atualizar o Ubuntu

Dentro do Ubuntu execute:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 6. Instalar o sudo (caso necessário)

Normalmente o Ubuntu já possui o `sudo` instalado.

Caso não exista, entre como usuário root e execute:

```bash
apt update
apt install sudo -y
```

Adicione seu usuário ao grupo sudo:

```bash
usermod -aG sudo NOME_DO_USUARIO
```

Reinicie o Ubuntu.

---

## 7. Instalar as Dependências

Execute:

```bash
sudo apt install git ansible python3 python3-pip python3-venv -y
```

Serão instalados:

* Git
* Ansible
* Python 3
* pip
* Ambiente virtual Python

---

## 8. Clonar o Projeto

```bash
git clone https://github.com/ftyamauchi/Honeypot-Dashboard.git
```

Entre na pasta:

```bash
cd Honeypot-Dashboard
```

---

## 9. Configuração

Não é necessária configuração manual.

Toda a instalação é realizada automaticamente pelo playbook do Ansible.

---

## 10. Executar o Projeto

Na pasta do projeto execute:

```bash
ansible-playbook ansible/site.yml --ask-become-pass
```

Informe a senha do usuário quando solicitada.

Aguarde a conclusão da instalação.

---

## 11. Testar o Honeypot

Abra outro terminal e execute:

```bash
ssh root@localhost -p 2222
```

Digite qualquer senha.

A tentativa de acesso será registrada pelo honeypot.

---

## 12. Visualização

Após executar o projeto, acesse o Dashboard pelo navegador conforme configurado na aplicação.

Os eventos capturados pelo honeypot serão exibidos automaticamente.

---

## 13. Estrutura do Projeto

```text
Honeypot-Dashboard/
├── ansible/
├── app/
├── logs/
├── static/
├── templates/
├── README.md
└── MANUAL.md
```

---

## 14. Considerações Finais

Este projeto demonstra a utilização de Infraestrutura como Código para automatizar a implantação de um honeypot SSH e de um dashboard web, permitindo reproduzir o ambiente de forma rápida e padronizada.
