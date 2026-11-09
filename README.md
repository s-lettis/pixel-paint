# Pixel Paint

Ad-free pixel art color-by-number for kids. No ads, no accounts, no tracking.
The whole app is `www/index.html`. Progress and your own pictures are saved on the phone.

## 1. Get the APK (about 5 minutes, nothing to install on your computer)

1. On github.com, create a **new private repository** (e.g. `pixel-paint`).
2. Upload everything in this folder to it. On the empty repo page choose **uploading an existing
   file**, drag in the *contents* of this folder (including the hidden `.github` folder), and
   commit. If `.github` is missing afterward, use **Add file > Create new file**, type
   `.github/workflows/build-apk.yml` as the name, and paste in that file from this folder.
   (Updating later: **Add file > Upload files** with the same file names replaces the old ones.)
3. Open the **Actions** tab. "Build APK" starts by itself (or choose it and click **Run workflow**).
4. When it turns green, open the run, download **pixel-paint-apk** under *Artifacts*, and unzip
   it to get `app-debug.apk`.
5. Copy the APK to the phone and tap it. Allow installs from that app when asked. On Samsung,
   if it is blocked, turn off Settings > Security and privacy > Auto Blocker while installing.

Signing note: every build uses a fresh debug key, so Android will not install a new build over
an older one. Uninstall the old app first (this erases saved progress on that phone).

## 2. Sharing pictures (works right away, no server)

- Make a picture with **New from a photo**, open it, tap **...** then **Share this picture**,
  and send it with any messaging app. It goes out as a text code.
- On the other phone, tap **Paste a picture** on the home screen and paste the message.

## 3. Painting together live (one-time free setup, about 5 minutes)

Rooms need a small online database that relays who painted what. This uses Google's free
Firebase Realtime Database. It stores only the picture and cell numbers, with no accounts and no
analytics. The setup is a one-time job for one person.

1. Go to console.firebase.google.com and sign in with a Google account.
2. **Create a project** (name it anything, e.g. `pixel-paint`). When asked about Google Analytics,
   turn it **off**.
3. In the project, go to **Databases & Storage > Realtime Database > Create database**. Pick any
   location and start in **locked mode**. (Do not use test mode: it expires.)
4. Open the **Rules** tab, replace everything with the contents of `firebase-rules.json` from this
   folder, and click **Publish**.
5. Open the **Data** tab and copy the address at the top. It looks like
   `https://pixel-paint-xxxxx-default-rtdb.firebaseio.com` (or ends in `firebasedatabase.app`).
6. In the app, tap the **gear** on the home screen and paste that address. Every phone that
   plays together needs the same address.

To avoid typing it on each phone, put it in the app itself: in `www/index.html` find the line
`var DEFAULT_RELAY='';`, put your address between the quotes, commit, and rebuild.
Anyone you give that APK to is ready to play. (Skip this if the repo is public, see section 4.)

**Rules update (needed for the online list):** if you set up Firebase before this version, open the
**Rules** tab again, replace everything with the new `firebase-rules.json`, and click **Publish**.

**Names and the online list:** tap the gear, add your name (Dad, Jake...), and Save. The home screen
then shows who is online. When someone is painting you see "Dad is painting Heart -> Join": one tap
and you're in, no code needed. This works the same on Android and iPhone.

**Family room:** one shared picture for everyone. Open a picture, tap **...**, **Paint together**,
**Family room**. The home screen of everyone online shows "Family room: <picture>" and one tap
joins. Starting a new family picture replaces the old one for everybody inside it.

**Playing with a code:** open any picture, tap **...** then **Paint together**. A 5-letter room code appears.
Friends tap **Join a room** on their home screen and type it. Everyone fills in the same board in
real time. The top bar shows the room code and how many people are in it.

Privacy: anyone who has a room code can see and paint that room, and rooms cannot be listed.
Rooms are not deleted automatically; you can delete the `rooms` entry in the Firebase Data tab
whenever you like. The free tier is far more than a family will use.

## 4. Web version for iPhones (and anyone else)

iPhones cannot sideload an APK, but the same app runs as a web app that installs to the Home
Screen: no App Store, works offline after the first visit, and it joins the same rooms as the
Android app. GitHub hosts it for free.

1. GitHub's free hosting needs a **public** repo. Repo **Settings > General**, scroll to the bottom
   **Danger Zone > Change visibility > Make public**. The repo holds only the app's code (no
   passwords or pictures). If you made a Firebase address part of the code (`DEFAULT_RELAY`),
   leave that blank in a public repo and type the address into the app's gear instead.
2. Repo **Settings > Pages > Build and deployment > Source: GitHub Actions**.
3. Open the **Actions** tab and run **Publish web app** (it also runs on every upload). When it is
   green, the site address is `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`.
4. Send that link to the iPhone people. On the iPhone, open it in **Safari**, tap the **Share**
   button, then **Add to Home Screen**, then **Add**. From then on open it from the new icon.
   (Android: Chrome menu > Install app also works.)

Tips: pictures and progress are stored per install, so always open from the Home Screen icon, not
from a Safari tab. Updates arrive on their own the next time the app opens with internet.

## Notes

- Starter pictures are small character grids at the top of the script, so adding more is easy.
- "New from a photo" lets you pick the size and number of colors before saving.
