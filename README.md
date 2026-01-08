# CI/CD QA Starter (Python + Pytest + GitHub Actions)

Este repositório demonstra um pipeline de CI rodando testes automaticamente a cada push/PR.

## Como rodar localmente
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
