import asyncio
from playwright.async_api import async_playwright


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            channel="chrome",
            args=[
                '--start-maximized'
            ]
        )
        context = await browser.new_context(
            ignore_https_errors=True,
            no_viewport=True
        )
        page = await context.new_page()

        url = ""

        try:
            await page.goto(url)

            await page.get_by_placeholder("Usuário").fill("")
            await page.get_by_placeholder("Senha").fill("")
            await page.get_by_role("button", name="Entrar").click()

            for i in range(4):
                await page.get_by_role("button", name=f"{i + 1:02}").click()

            await page.get_by_role("button", name="Tela cheia").click()

            await asyncio.Future()

        except Exception as e:
            print(f"Erro: {e}")

        finally:
            await browser.close()
            await context.close()


async def main():
    await run()

if __name__ == "__main__":
    asyncio.run(main())
