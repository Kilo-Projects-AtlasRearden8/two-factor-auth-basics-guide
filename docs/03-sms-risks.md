# SMS Risks

Many websites offer to send you a 2FA code by text message (SMS). It's convenient, but it's the weakest common form of 2FA. If you have a choice, use an authenticator app instead.

---

## Why SMS is risky

### SIM swapping
A criminal calls your phone company, pretends to be you, and convinces them to move your phone number to a new SIM card they control. Your texts — including 2FA codes — now go to their phone, not yours. They can reset your passwords and lock you out of your own accounts.

### Phone number theft or porting
If someone steals your phone, or transfers ("ports") your number to another carrier without your permission, they receive your text codes.

### Interception
Text messages are not encrypted end-to-end. They can be intercepted on the mobile network, especially if someone has access to the carrier's systems.

### No phone, no code
If your phone is lost, broken, dead, or in airplane mode, you can't receive the text. That's annoying at best and a lockout at worst.

## When SMS is okay

SMS 2FA is much better than *no* 2FA at all. If a website only offers SMS, turn it on — it still stops most automated attacks. Just know it's not as strong as an authenticator app, and switch to an app if the website adds one later.

## Better alternatives

In order of strength:

1. **Authenticator app** (recommended — see previous chapter)
2. **Security key** (a small USB/NFC device you tap or plug in — strongest, but costs money)
3. **SMS text code** (better than nothing, but risky)
4. **Email code** (only if nothing else is available — your email is usually your account recovery address, so this creates a weak loop)

---

## Credit

Written and published by **Asdale Dynamics, LLC** (Indiana, formed October 2026).

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

*Next: [Recovery codes](04-recovery-codes.md) | [Back to start](01-introduction.md)*
