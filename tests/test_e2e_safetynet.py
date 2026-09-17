import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_e2e_landing_page(driver, base_url):
    """E2E Test: Landing page load, search filter, and WhatsApp CTA."""
    driver.get(f"{base_url}/")
    assert "Pusat Belajar Web Development — ITSENJA" in driver.title

    # Verify header & cards
    cards = driver.find_elements(By.CSS_SELECTOR, ".sprint-card")
    assert len(cards) >= 5, f"Expected at least 5 sprint cards, found {len(cards)}"

    # Test Live Search input
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.clear()
    search_input.send_keys("Git")
    time.sleep(0.3)

    visible_cards = [c for c in cards if c.is_displayed()]
    assert len(visible_cards) >= 1, "Expected at least 1 visible card for query 'Git'"
    assert any("Git" in c.text for c in visible_cards)

    # Clear search
    search_input.send_keys(Keys.CONTROL + "a")
    search_input.send_keys(Keys.BACKSPACE)
    time.sleep(0.3)

    # Verify WhatsApp CTA
    wa_btn = driver.find_element(By.CSS_SELECTOR, ".floating-wa-btn")
    assert wa_btn.is_displayed()
    assert "wa.me" in wa_btn.get_attribute("href")


def test_e2e_contact_form_and_honeypot_trap(driver, base_url):
    """E2E Test: Anti-spam honeypot detection and legitimate form validation."""
    driver.get(f"{base_url}/")

    form = driver.find_element(By.ID, "consultForm")
    alert_box = driver.find_element(By.ID, "formAlertBox")

    # 1. Empty submit should fail validation
    submit_btn = form.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()
    time.sleep(0.3)

    name_feedback = driver.find_element(By.ID, "nameFeedback")
    assert name_feedback.is_displayed() or "Nama minimal" in driver.page_source

    # 2. Test Honeypot Bot Trap: Bot fills hidden field
    hp_input = driver.find_element(By.ID, "hp_website")
    # Using JS to set value to simulate malicious bot
    driver.execute_script("arguments[0].value = 'https://spambot-site.xyz';", hp_input)
    submit_btn.click()
    time.sleep(0.3)

    assert "Honeypot Trap" in alert_box.text or "Aktivitas mencurigakan" in alert_box.text

    # Clear honeypot
    driver.execute_script("arguments[0].value = '';", hp_input)


def test_e2e_slide_navigation_sprint01(driver, base_url):
    """E2E Test: Sprint 01 slide deck navigation, keyboard controls, and hub link."""
    driver.get(f"{base_url}/Sprint-01/slide.html")
    assert "Sprint 01" in driver.title

    slides = driver.find_elements(By.CSS_SELECTOR, ".slide")
    assert len(slides) >= 15

    # Initially slide 0 is active
    assert "active" in slides[0].get_attribute("class")

    # Click next button
    next_btn = driver.find_element(By.ID, "next-btn")
    next_btn.click()
    time.sleep(0.3)

    assert "active" not in slides[0].get_attribute("class")
    assert "active" in slides[1].get_attribute("class")

    # Click prev button
    prev_btn = driver.find_element(By.ID, "prev-btn")
    prev_btn.click()
    time.sleep(0.3)

    assert "active" in slides[0].get_attribute("class")

    # Test keyboard navigation (ArrowRight)
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.ARROW_RIGHT)
    time.sleep(0.3)

    assert "active" in slides[1].get_attribute("class")

    # Test Hub link navigation
    hub_link = driver.find_element(By.CSS_SELECTOR, ".nav-hub-link")
    hub_link.click()
    time.sleep(0.5)

    assert "Pusat Belajar" in driver.title


def test_e2e_slide_navigation_and_runner_sprint03(driver, base_url):
    """E2E Test: Sprint 03 slide deck and interactive DOM code runner execution."""
    driver.get(f"{base_url}/Sprint-03/")
    assert "Sprint 03" in driver.title

    slides = driver.find_elements(By.CSS_SELECTOR, ".slide")
    assert len(slides) == 17

    # Navigate to Slide 11 (DOM getElementById text manipulation)
    driver.execute_script("updateSlideDisplay(10);")
    time.sleep(0.3)

    assert "active" in slides[10].get_attribute("class")
    playbox = driver.find_element(By.ID, "playbox")
    original_text = playbox.text

    # Click run button on active slide
    run_btn = slides[10].find_element(By.CSS_SELECTOR, ".btn-run")
    run_btn.click()
    time.sleep(0.3)

    # Text must have updated
    new_text = playbox.text
    assert new_text != original_text
    assert "dinamis" in new_text.lower() or "diubah" in new_text.lower()

    # Navigate to Slide 15 (Click counter)
    driver.execute_script("updateSlideDisplay(14);")
    time.sleep(0.3)

    counter_val = driver.find_element(By.ID, "counterVal")
    assert counter_val.text == "0"

    counter_btn = slides[14].find_element(By.CSS_SELECTOR, ".btn-run")
    counter_btn.click()
    time.sleep(0.2)
    assert counter_val.text == "1"

    counter_btn.click()
    time.sleep(0.2)
    assert counter_val.text == "2"


def test_e2e_slide_navigation_sprint04(driver, base_url):
    """E2E Test: Sprint 04 slide deck and playground runner."""
    driver.get(f"{base_url}/Sprint-04/")
    assert "Sprint 04" in driver.title or "Modern JavaScript" in driver.title

    slides = driver.find_elements(By.CSS_SELECTOR, ".slide")
    assert len(slides) >= 15

    # Navigate to slide with playground (Slide 3)
    driver.execute_script("updateSlideDisplay(2);")
    time.sleep(0.3)

    active_slide = driver.find_element(By.CSS_SELECTOR, ".slide.active")
    run_btn = active_slide.find_elements(By.CSS_SELECTOR, ".btn-run")
    if run_btn:
        run_btn[0].click()
        time.sleep(0.4)
        iframe = active_slide.find_element(By.CSS_SELECTOR, ".preview-iframe")
        assert iframe is not None


def test_e2e_slide_navigation_sprint05(driver, base_url):
    """E2E Test: Sprint 05 theory slide deck and navigation."""
    driver.get(f"{base_url}/Sprint-05/")
    assert "Sprint 05" in driver.title

    slides = driver.find_elements(By.CSS_SELECTOR, ".slide")
    assert len(slides) == 20

    next_btn = driver.find_element(By.ID, "next-btn")
    next_btn.click()
    time.sleep(0.2)
    assert "active" in slides[1].get_attribute("class")


def test_e2e_praktikum_sprint05_interactive_tools(driver, base_url):
    """E2E Test: Sprint 05 practical workshop slide deck and interactive tools."""
    driver.get(f"{base_url}/Sprint-05/praktikum.html")
    assert "Praktikum Interaktif" in driver.title

    slides = driver.find_elements(By.CSS_SELECTOR, ".slide")
    assert len(slides) == 12

    # Slide 4: Test .gitignore tester
    driver.execute_script("updateSlideDisplay(3);")
    time.sleep(0.3)

    git_test_input = driver.find_element(By.ID, "ignTestInput")
    git_test_input.clear()
    git_test_input.send_keys("node_modules/axios/index.js")
    
    test_btn = slides[3].find_element(By.CSS_SELECTOR, ".btn-action.green")
    test_btn.click()
    time.sleep(0.3)

    WebDriverWait(driver, 3).until(
        lambda d: "DIABAIKAN" in d.find_element(By.ID, "ignTestResult").text.upper()
    )
    status_box = driver.find_element(By.ID, "ignTestResult")
    assert "DIABAIKAN" in status_box.text.upper()

    # Slide 5: Test Conventional Commits builder
    driver.execute_script("updateSlideDisplay(4);")
    time.sleep(0.3)

    desc_input = driver.find_element(By.ID, "commitDescInput")
    desc_input.clear()
    desc_input.send_keys("add user authentication module")
    time.sleep(0.3)

    preview_output = driver.find_element(By.ID, "commitCmdOutput")
    assert "feat:" in preview_output.text
    assert "add user authentication module" in preview_output.text

    # Slide 11: Test Interactive Checklist & Progress (Index 11, Slide 12)
    driver.execute_script("updateSlideDisplay(11);")
    time.sleep(0.3)

    progress_text = driver.find_element(By.ID, "labProgressPercent")
    assert "0%" in progress_text.text

    check_cards = driver.find_elements(By.CSS_SELECTOR, ".check-card")
    assert len(check_cards) == 6

    # Click first check card
    driver.execute_script("arguments[0].click();", check_cards[0])
    time.sleep(0.3)

    # Progress should increase to 17%
    assert "17%" in progress_text.text


def test_e2e_custom_404_routing(driver, base_url):
    """E2E Test: Custom 404 page routing and return to Hub."""
    driver.get(f"{base_url}/rute-halaman-random-pasti-tidak-ada-404")
    assert "404" in driver.title or "404" in driver.page_source

    home_btn = driver.find_element(By.CSS_SELECTOR, ".action-buttons .btn-primary")
    assert home_btn.is_displayed()
    home_btn.click()
    time.sleep(0.5)

    assert "Pusat Belajar" in driver.title
