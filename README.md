# Projeto de Automação de Testes com Selenium

Este projeto contém scripts de automação de testes para o site [Katalon Demo CURA](https://katalon-demo-cura.herokuapp.com/), utilizando **Selenium** e **Pytest**. O objetivo é validar as funcionalidades principais do site, como login, agendamento de consultas, validação de campos obrigatórios e navegação entre páginas.

---

## 📋 **Funcionalidades Testadas**

O projeto cobre os seguintes casos de teste:

1. **Autenticação bem-sucedida (login/logout)**  
   - Verifica se o usuário consegue fazer login com credenciais válidas e realizar logout.

2. **Autenticação falha (credenciais inválidas)**  
   - Verifica se o sistema exibe uma mensagem de erro ao tentar fazer login com credenciais inválidas.

3. **Preenchimento e validação de formulário de agendamento**  
   - Verifica se o usuário consegue preencher e submeter o formulário de agendamento com sucesso.

4. **Validação de campos obrigatórios no formulário de agendamento**  
   - Verifica se o sistema exibe mensagens de erro ao tentar submeter o formulário sem preencher o campo obrigatório da data.

5. **Navegação para a página de perfil**  
   - Verifica se o usuário consegue navegar até a página de perfil e visualizar o conteúdo correto.

6. **Navegação para a página de histórico**  
   - Verifica se o usuário consegue navegar até a página de histórico e visualizar o conteúdo correto.

---

## 🛠️ **Tecnologias Utilizadas**

- **Selenium**: Framework de automação de testes para navegadores.
- **Pytest**: Framework de testes para Python.
- **Edge WebDriver**: Driver para o navegador Microsoft Edge.
- **WebDriver Manager**: Gerenciador automático de drivers para Selenium.

---

## ⚙️ **Configuração do Ambiente**

### Pré-requisitos

1. **Python 3.x**: Instale a versão mais recente do Python.
   - [Download Python](https://www.python.org/downloads/)

2. **Pip**: Gerenciador de pacotes do Python (já vem instalado com o Python).

3. **Microsoft Edge**: Certifique-se de ter o navegador Edge instalado.

### Instalação das Dependências

1. Clone este repositório:
   ```bash
   git clone https://github.com/guizitos/Automocao-de-Testes-com-Selenium.git
   cd nome-do-repositorio
   
### Instale as dependências do projeto:

pip install selenium pytest webdriver-manager

## 🚀 *Executando os Testes*

pytest testes_final.py --html=relatorio.html

testes_final.py: Arquivo contendo todos os casos de teste.

--html=relatorio.html: Gera um relatório HTML com os resultados dos testes.


## 📊 *Relatório de Testes*

- Após a execução dos testes, um relatório HTML será gerado (relatorio.html). Abra o arquivo em um navegador para visualizar os resultados detalhados.

## 📝 *Observações*

- Capturas de Tela: Em caso de falha, o teste salva automaticamente uma captura de tela no diretório raiz do projeto.

- Ambiente de Teste: Os testes foram desenvolvidos para o navegador Microsoft Edge. Certifique-se de que o EdgeDriver está configurado corretamente.

- Dados de Teste: Os dados de teste (usuário, senha, etc.) estão embutidos no código. Para testes em outros ambientes, ajuste os dados conforme necessário.

## 🤝 *Contribuição*

- Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas mudanças (git commit -m 'Adicionando nova feature').

Push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

## 📧 *Contato*

- Se tiver dúvidas ou sugestões, entre em contato:

- Nome: [Guilherme Santo Costa]

- E-mail: [gu1cost4@icloud.com]

- GitHub: guizitos

## 📜 *Licença*

- Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
