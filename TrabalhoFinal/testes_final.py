import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Configuração inicial do teste
@pytest.fixture(scope="module")
def driver():
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    try:
        # Navega até a página inicial
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        yield driver
    finally:
        driver.quit()

# Função auxiliar para preencher campos
def preencher_campo(driver, by, locator, texto):
    campo = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((by, locator)))
    campo.clear()
    campo.send_keys(texto)

#ID: CT-001
# Teste 1: Autenticação bem-sucedida (login/logout)
def test_login_logout(driver):
    try:
        driver.find_element(By.ID, "btn-make-appointment").click()
        preencher_campo(driver, By.ID, "txt-username", "John Doe")
        preencher_campo(driver, By.ID, "txt-password", "ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()

        WebDriverWait(driver, 30).until(EC.url_contains("#appointment"))
        assert "CURA Healthcare Service" in driver.title

        driver.find_element(By.ID, "menu-toggle").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

        WebDriverWait(driver, 30).until(EC.title_contains("CURA Healthcare Service"))
        assert "CURA Healthcare Service" in driver.title

    except Exception as e:
        driver.save_screenshot("screenshot_falha_login.png")
        raise e

#ID: CT-002
# Teste 2: Autenticação falha (credenciais inválidas)
def test_login_falha(driver):
    try:
        driver.find_element(By.ID, "btn-make-appointment").click()
        preencher_campo(driver, By.ID, "txt-username", "UsuarioInvalido")
        preencher_campo(driver, By.ID, "txt-password", "SenhaInvalida")
        driver.find_element(By.ID, "btn-login").click()

        error_message = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "text-danger"))
        )
        assert "Login failed!" in error_message.text

    except Exception as e:
        driver.save_screenshot("screenshot_falha_login_invalido.png")
        raise e
    
#ID: CT-003
# Teste 3: Preenchimento e validação de formulário de agendamento
def test_preenchimento_formulario(driver):
    try:
        # Faz login
        driver.find_element(By.ID, "btn-make-appointment").click()
        preencher_campo(driver, By.ID, "txt-username", "John Doe")
        preencher_campo(driver, By.ID, "txt-password", "ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()

        # Preenche o formulário
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "combo_facility"))
        ).send_keys("Hongkong CURA Healthcare Center")
        driver.find_element(By.ID, "chk_hospotal_readmission").click()
        driver.find_element(By.ID, "radio_program_medicaid").click()
        preencher_campo(driver, By.ID, "txt_visit_date", "10/10/2023")
        preencher_campo(driver, By.ID, "txt_comment", "Agendamento de consulta geral")
        driver.find_element(By.ID, "btn-book-appointment").click()

        # Validação
        confirmation_message = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        assert "Appointment Confirmation" in confirmation_message.text

    except Exception as e:
        driver.save_screenshot("screenshot_falha_formulario.png")
        raise e

#ID: CT-004 
# Teste 4: Validação de campos obrigatórios no formulário de agendamento
def test_validacao_campos_obrigatorios(driver):
    try:
        # Clica no botão "Make Appointment"
        driver.find_element(By.ID, "btn-make-appointment").click()

        # Aguarda até que o formulário de agendamento seja carregado
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "combo_facility"))
        )

        # Tenta submeter o formulário sem preencher o campo obrigatório (data)
        driver.find_element(By.ID, "btn-book-appointment").click()

        # Verifica se o campo da data está marcado como obrigatório
        campo_data = driver.find_element(By.ID, "txt_visit_date")
        assert campo_data.get_attribute("required") is not None, "O campo da data não está marcado como obrigatório."

        # Verifica se a mensagem de validação nativa está sendo exibida
        mensagem_validacao = campo_data.get_attribute("validationMessage")
        assert mensagem_validacao == "Preencha este campo.", f"Mensagem de validação incorreta: {mensagem_validacao}"

    except Exception as e:
        driver.save_screenshot("screenshot_falha_campos_obrigatorios.png")
        raise e

#ID: CT-005
# Teste 5: Navegação para a página de perfil
def test_pagina_perfil(driver):
    try:
        # Navega até a página de perfil
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#profile")

        # Aguarda até que o título da página seja carregado
        WebDriverWait(driver, 30).until(EC.title_is("CURA Healthcare Service"))

        # Verifica se o cabeçalho da seção de perfil está presente
        profile_header = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        assert profile_header.text == "Profile", "O cabeçalho do perfil não está correto."

        # Verifica se a mensagem "Under construction" está presente
        under_construction_message = driver.find_element(By.CLASS_NAME, "lead")
        assert "Under construction" in under_construction_message.text, "A mensagem de construção não está presente."

    except Exception as e:
        driver.save_screenshot("screenshot_falha_perfil.png")
        raise e

#ID: CT-006 
# Teste 6: Navegação para a página de histórico
def test_pagina_history(driver):
    try:
        # Navega até a página de histórico
        driver.get("https://katalon-demo-cura.herokuapp.com/history.php#history")

        # Aguarda até que o título da página seja carregado
        WebDriverWait(driver, 30).until(EC.title_is("CURA Healthcare Service"))

        # Verifica se o cabeçalho da seção de histórico está presente
        history_header = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        assert history_header.text == "History", "O cabeçalho do histórico não está correto."

    except Exception as e:
        driver.save_screenshot("screenshot_falha_history.png")
        raise e
    