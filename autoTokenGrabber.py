from playwright.sync_api import sync_playwright
import re
import os

def get_spotify_token_from_existing_chrome_profile():
    with sync_playwright() as p:
        #LEETleri kendi kullanıcıı adınıza göre değiştirin
        user_data_dir = r"C:\Users\LEET\AppData\Local\Google\Chrome\User Data"
        profile_name = "LEET"

        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            args=[f"--profile-directory={profile_name}"]
        )

        page = context.new_page()
        page.goto("https://open.spotify.com")

        token = None

        def handle_request(request):
            nonlocal token
            auth = request.headers.get("authorization")
            if auth and auth.startswith("Bearer ") and token is None:
                token = auth.split(" ")[1]

        page.on("request", handle_request)

        print("Spotify sayfası açıldı. Otomatik token arıyoruz...")
        page.wait_for_timeout(15000) 
        context.close()

        if token:
            print("\nToken alındı!")
            return token
        else:
            print("\nToken bulunamadı.")
            return None
        
if __name__ == "__main__":
    token = get_spotify_token_from_existing_chrome_profile()
    if token:
        print("TOKEN:", token[:60] + "...")
