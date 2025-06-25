class Automation:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

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

    async def navigate_to_dvr(self):
        await self.page.goto(self.url)

    async def login(self):
        await self.page.get_by_placeholder("Usuário").fill(self.username)
        await self.page.get_by_placeholder("Senha").fill(self.password)
        await self.page.get_by_role("button", name="Entrar").click()

    async def select_buttons(self):
        try:
            for i in range(4):
                await self.page.get_by_role("button", name=f"{i + 1:02}").click(timeout=3000)

        except Exception:
            raise ValueError(
                "Login falhou: Usuário ou senha incorretos.\n\nCertifique-se de que o usuário e a senha estão corretos.")

    async def enter_full_screen(self):
        await self.page.get_by_role("button", name="Tela cheia").click()

    async def close_browser(self):
        await self.browser.close()
        await self.context.close()

    async def run(self):
        import asyncio
        from playwright.async_api import async_playwright

        async with async_playwright() as p:
            await self.launch_browser(p)
            await self.navigate_to_dvr()
            await self.login()
            await self.select_buttons()
            await self.enter_full_screen()
            await asyncio.Future()
