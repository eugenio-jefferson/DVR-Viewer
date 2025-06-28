class Automation:
    def __init__(self, url, username, password, channel_numbers):
        self.url = url
        self.username = username
        self.password = password
        self.channel_numbers = channel_numbers

    async def launch_browser(self, p):
        self.browser = await p.chromium.launch(
            headless=False,
            channel="chrome",
            args=['--start-maximized']
        )
        self.context = await self.browser.new_context(
            ignore_https_errors=True,
            no_viewport=True
        )
        self.page = await self.context.new_page()
        self.page.on("close", self.on_page_close)

    async def navigate_to_dvr(self):
        await self.page.goto(self.url)

    async def login(self):
        import asyncio
        await self.page.get_by_placeholder("Usuário").fill(self.username)
        await self.page.get_by_placeholder("Senha").fill(self.password)

        button_login = self.page.get_by_role("button", name="Entrar")
        await button_login.click()

        del self.password

        await self.page.wait_for_timeout(2000)

        if await button_login.is_visible():
            raise ValueError(
                "Login falhou: Usuário ou senha incorretos.\n\nCertifique-se de que o usuário e a senha estão corretos.")

    async def select_channels(self):
        for i in range(self.channel_numbers):
            await self.page.get_by_role("button", name=f"{i + 1:02}").click()

    async def enter_full_screen(self):
        await self.page.get_by_role("button", name="Tela cheia").click()

    async def close_browser(self):
        await self.browser.close()
        await self.context.close()

    async def run(self):
        import asyncio
        from playwright.async_api import async_playwright

        self.close_event = asyncio.Event()

        async with async_playwright() as p:
            await self.launch_browser(p)
            await self.navigate_to_dvr()
            await self.login()
            await self.select_channels()
            await self.enter_full_screen()

            await self.close_event.wait()

    def on_page_close(self):
        self.close_event.set()
