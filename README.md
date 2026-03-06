# Agencia IA - Automatizaciones 🤖

Plataforma completa de agentes IA con GitHub Actions integrados para automatizaciones end-to-end.

## 🎯 Características

- ✅ Agentes IA modulares y reutilizables
- ✅ Automatización de workflows con GitHub Actions
- ✅ CI/CD integrado
- ✅ Tests automáticos
- ✅ Seguridad y validaciones
- ✅ Monitoreo y alertas
- ✅ Deploy automático

## 🚀 Setup Rápido

### Requisitos
- Python 3.10+
- Git
- GitHub CLI (opcional)

### Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/devmv1979-star/agencia-ia-automatizaciones.git
cd agencia-ia-automatizaciones

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Uso en Codespaces

1. Ve a este repositorio
2. Haz click en `Code` → `Codespaces` → `Create codespace on main`
3. Espera a que se cargue (1-2 minutos)
4. En la terminal: `pip install -r requirements.txt`

## 📁 Estructura del Proyecto

```
agencia-ia-automatizaciones/
├── src/
│   ├── agents/           # Código de agentes IA
│   │   ├── agent_base.py # Clase base de agentes
│   │   └── __init__.py
│   ├── workflows/        # Orquestación de workflows
│   └── scripts/          # Scripts auxiliares
├── tests/                # Tests unitarios
├── .github/
│   └── workflows/        # GitHub Actions workflows
│       ├── 01-test-agents.yml
│       ├── 02-lint-security.yml
│       └── 03-build-deploy.yml
├── models/               # Modelos entrenados
├── data/                 # Datos
│   └── processed/        # Datos procesados
├── prompts/              # Prompts de IA
├── logs/                 # Logs de ejecución
├── requirements.txt      # Dependencias Python
├── setup.py              # Configuración del paquete
└── README.md             # Este archivo

```

## 🔧 Configuración de Variables de Entorno

Crea un archivo `.env.local` (no se sube a Git):

```env
OPENAI_API_KEY=tu_clave_aqui
CLAUDE_API_KEY=tu_clave_aqui
DATABASE_URL=postgresql://user:password@localhost/db
SLACK_WEBHOOK=https://hooks.slack.com/...
```

## 🧪 Ejecutar Tests

```bash
# Tests básicos
pytest tests/ -v

# Con cobertura
pytest tests/ -v --cov=src/agents/ --cov-report=html

# Test específico
pytest tests/test_agent.py::test_agent_creation -v
```

## 📊 GitHub Actions Workflows

### 1. Tests Automáticos (01-test-agents.yml)
- Se ejecuta en cada push y PR
- Corre tests en Python 3.10 y 3.11
- Genera reporte de cobertura

### 2. Lint & Seguridad (02-lint-security.yml)
- Validación de código con Black, Flake8
- Análisis de seguridad con Bandit
- Se ejecuta en cada push

### 3. Build & Deploy (03-build-deploy.yml)
- Construye paquete Python
- Se ejecuta en pushes a main
- Genera artefactos

## 🚀 Primeros Pasos

1. **Crear un agente simple:**
```python
from src.agents import Agent, AgentConfig

config = AgentConfig(
    name="MiAgente",
    description="Mi primer agente IA",
    model="gpt-4",
    temperature=0.7
)

agent = Agent(config)
respuesta = agent.process("Hola, ¿cómo estás?")
print(respuesta)
```

2. **Ejecutar tests:**
```bash
pytest tests/ -v
```

3. **Hacer un commit:**
```bash
git add .
git commit -m "🚀 Primer agente implementado"
git push
```

## 📚 Documentación Adicional

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Python Agents](./docs/agents.md)
- [Workflows](./docs/workflows.md)

## 🤝 Contribuir

1. Crea una rama: `git checkout -b feature/tu-feature`
2. Haz cambios y tests
3. Push: `git push origin feature/tu-feature`
4. Abre un Pull Request

## 📝 Licencia

MIT License - Ver LICENSE para detalles

## ✨ Autor

Creado con ❤️ por devmv1979-star

---

**¿Necesitas ayuda?** Abre un issue o contactame.

**Última actualización:** 2026-03-06