# Pixel Paint

Ad-free pixel art color-by-number for kids. No network, no tracking, no accounts.
Everything lives in `www/index.html`. Progress and your own pictures are saved on the phone.

## Get the APK (about 5 minutes, no installs on your computer)

1. On github.com, create a **new private repository** (e.g. `pixel-paint`).
2. Upload everything in this folder to it. Easiest: on the empty repo page choose
   **uploading an existing file**, drag in the *contents* of this folder (including the hidden
   `.github` folder), and commit. If your browser skips `.github`, create the file
   `.github/workflows/build-apk.yml` by hand with **Add file > Create new file** and paste the
   contents of the one in this folder.
3. Open the repo's **Actions** tab. The "Build APK" workflow starts by itself on the commit
   (or choose it and click **Run workflow**).
4. When it turns green, open the run and download **pixel-paint-apk** from *Artifacts*.
   Unzip it to get `app-debug.apk`.
5. Copy `app-debug.apk` to the phone (USB, Drive, email to yourself) and tap it.
   Android will ask to allow installs from that app (Files / Chrome / Drive): allow it.

Samsung phones: if the install is blocked, turn off **Settings > Security and privacy >
Auto Blocker** while installing (you can turn it back on afterward).

## Changing the app

Edit `www/index.html`, commit, and Actions builds a new APK. See the signing note below
before installing it over an older build.

## Notes

- The APK is a debug build signed with a throwaway debug key. That is fine for sideloading to
  your own family's phones. Every build from a fresh runner uses a new debug key, so Android
  may refuse to update over an older build; uninstall first in that case (this erases progress).
- Starter pictures are defined at the top of the script as small character grids, so new ones
  are easy to add.
- "New from a photo" turns any photo or drawing into a puzzle (size and number of colors are
  adjustable before saving).
