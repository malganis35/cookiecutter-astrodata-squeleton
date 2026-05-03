# Troubleshooting & FAQ

Found a bug or getting an error? Check here first.

---

## ❓ Frequently Asked Questions

### Q: `uv` is not found after installation
**A**: Ensure your shell path includes `~/.local/bin`. On Linux/macOS, add this to your `.bashrc` or `.zshrc`:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then restart your terminal.

### Q: Import error in Jupyter Notebooks
**A**: Make sure you have:
1. Ran `make dev-install`.
2. Selected the correct Python kernel in your IDE (the one located in `.venv/bin/python`).

### Q: API returns 500 errors
**A**: Check the terminal output where you ran `make run_api`. Ensure your `.env` variables are correctly set and you have data in `data/raw/`.

---

## 🐞 Reporting Issues

If your problem is not listed here:
1. Check the existing **GitLab/GitHub Issues**.
2. Create a new issue using the **Bug Template**. 
3. Include your OS version, Python version, and a copy of the error log.
