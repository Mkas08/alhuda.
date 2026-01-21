# GitHub Migration Guide: Al-Huda

Follow these steps to push the local project to your GitHub account (`Mkas08`).

## 1. Create Repositories on GitHub
Go to [github.com/new](https://github.com/new) and create three **empty** (no README/LICENSE) repositories:
1. `mobile`
2. `backend`
3. `docs` (optional, can also be a folder in a monorepo)

*Recommendation: For MVP simplicity, we can use a **Monorepo** (one repository for everything).*

---

## 2. Push to GitHub (Monorepo Approach)
If you want everything in one repository named `alhuda`:

1. **Initialize Git:**
   ```powershell
   cd "D:\Habit builder"
   git init
   git add .
   git commit -m "chore: initial project scaffolding"
   ```

2. **Add Remote & Push:**
   ```powershell
   git remote add origin https://github.com/Mkas08/alhuda.git
   git branch -M main
   git push -u origin main
   ```

---

## 3. Verify CI/CD
Once pushed, go to the **Actions** tab on GitHub:
- You should see `Backend CI` and `Mobile CI` workflows starting.
- They will automatically run on every push to `main`.

---

## 4. Next Steps
Once the code is on GitHub, I can help you with:
- **Secrets Management:** Adding `SENTRY_DSN`, `SMTP_PASSWORD`, etc. to GitHub Secrets.
- **Branch Protection:** Requiring PR reviews before merging to `main`.
