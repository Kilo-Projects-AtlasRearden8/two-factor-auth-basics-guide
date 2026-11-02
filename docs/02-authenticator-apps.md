# Authenticator Apps

The most recommended way to do two-factor authentication is with an authenticator app on your phone.

---

## What an authenticator app does

When you turn on 2FA for an account, the app shows you a six-digit code that changes every 30 seconds. When you log in, you enter your password *and* the current code from the app.

Because the code changes constantly and only lives on your phone, someone who steals your password still can't log in — they don't have your phone.

## Why authenticator apps are the best everyday choice

- They work without cell service or Wi-Fi (the codes are generated on your phone)
- They're faster than waiting for a text message
- They're not tied to your phone number, so SIM-swap attacks don't work against them (more on that next)
- Most are free

## Popular free authenticator apps

| App | Platform | Notes |
|-----|----------|-------|
| Google Authenticator | iPhone, Android | Simple, widely supported |
| Microsoft Authenticator | iPhone, Android | Can back up to your cloud account |
| Authy | iPhone, Android | Can back up and sync across devices |
| Aegis | Android | Open source, encrypted backups |
| Raivo OTP | iPhone | Open source, simple |

You only need one. Pick whichever is easiest for you to install and use.

## How to set up an authenticator app (general steps)

The exact screens vary by app and website, but the steps are almost always the same:

1. **Install the app** from your phone's app store (Apple App Store or Google Play Store).
2. **Go to the account's security settings.** Look for "Two-factor authentication," "2FA," "Two-step verification," or "Login security."
3. **Turn on 2FA** and choose "Authenticator app" (sometimes called an "app-based code" or "TOTP").
4. **Scan the QR code** the website shows you with your authenticator app. Or, if scanning doesn't work, copy the long "setup key" the website gives you and type it into the app manually.
5. **The app will show a six-digit code.** Type that code into the website to prove it works.
6. **Save your recovery codes** (see the recovery codes chapter) before you finish.

After this, logging in means: password + current code from your app.

## Tips for using your authenticator app

- **Don't delete the app** until you've saved recovery codes and moved your accounts elsewhere. If you delete the app, you could be locked out.
- **Don't share your codes** with anyone. A real company will never call or message you asking for your authenticator code.
- **If you get a new phone,** move your accounts to the new phone *before* you wipe or give away the old one. Some apps let you transfer accounts; others require you to re-scan each QR code.

---

## Credit

Written and published by **Asdale Dynamics, LLC** (Indiana, formed October 2026).

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

*Next: [SMS risks](03-sms-risks.md) | [Back to start](01-introduction.md)*
