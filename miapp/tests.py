from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['testdb.json']  # carga usuario isard

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = ChromeOptions()
        opts.add_argument("--headless")  # ejecuta sin abrir navegador
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        cls.selenium = Chrome(options=opts)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        self.assertEqual(self.selenium.title, "Log in | Django site admin")

        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('isard')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()

        self.assertEqual(self.selenium.title, "Site administration | Django site admin")

    def test_login_error(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        self.assertEqual(self.selenium.title, "Log in | Django site admin")

        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('usuario_no_existe')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('contrasena_incorrecta')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()

        self.assertNotEqual(self.selenium.title, "Site administration | Django site admin")
