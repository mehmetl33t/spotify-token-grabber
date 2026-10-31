import os
import re
from playwright.sync_api import sync_playwright


def get_spotify_token_from_existing_chrome_profile(user_data_dir=None, profile_name="Default"):
    """Extract Spotify Bearer token from an existing Chrome session using Playwright."""
    if user_data_dir is None:
        username = os.environ.get("USERNAME") or os.environ.get("USER") or "Default"
        user_data_dir = rf"C:\Users\{username}\AppData\Local\Google\Chrome\User Data"

    print(f"Chrome Profil Dizini: {user_data_dir}")
    print(f"Profil: {profile_name}")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            args=[f"--profile-directory={profile_name}"],
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

        print("Spotify sayfası açıldı. Otomatik token taranıyor...")
        page.wait_for_timeout(10000)
        context.close()

        if token:
            print("\n[+] Token başarıyla alındı!")
            return token
        else:
            print("\n[-] Token bulunamadı. Lütfen Spotify'da oturum açtığınızdan emin olun.")
            return None


if __name__ == "__main__":
    token = get_spotify_token_from_existing_chrome_profile()
    if token:
        print("\nTOKEN:", token)
