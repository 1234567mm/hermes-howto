<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/hermes-howto-logo-dark.svg">
  <img alt="Hermes How To" src="resources/logos/hermes-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%23%201%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/wchao-hermes/hermes-howto?style=flat&color=gold)](https://github.com/wchao-hermes/hermes-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wchao-hermes/hermes-howto?style=flat)](https://github.com/wchao-hermes/hermes-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)](CHANGELOG.md)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-Compatible-purple)](https://hermes-agent.dev)

🌐 **Idioma / Ngôn ngữ / 语言 / Мова:** [English](README.md) | [Tiếng Việt](vi/README.md) | [中文](zh/README.md) | [Українська](uk/README.md)

# Domina Hermes Agent en un Fin de Semana

Pasa de un chat básico a la orquestación de agentes, habilidades, servidores MCP, voz e integraciones de mensajería — con tutoriales visuales, plantillas para copiar y pegar, y una ruta de aprendizaje guiada.

**[Comenzar en 15 Minutos](#get-started-in-15-minutes)** | **[Encuentra tu Nivel](#not-sure-where-to-start)** | **[Explorar el Catálogo de Funciones](INDEX.md)**

---

## Tabla de Contenidos

- [El Problema](#the-problem)
- [Cómo lo Soluciona Hermes How To](#how-hermes-how-to-fixes-this)
- [Cómo Funciona](#how-it-works)
- [¿No Sabes por Dónde Empezar?](#not-sure-where-to-start)
- [Comenzar en 15 Minutos](#get-started-in-15-minutes)
- [¿Qué Puedes Construir Con Esto?](#what-can-you-build-with-this)
- [Preguntas Frecuentes (FAQ)](#faq)
- [Contribución](#contributing)
- [Licencia](#license)

---

## El Problema

Instalaste Hermes Agent. Ejecutaste algunos prompts. ¿Y ahora qué?

- **La documentación oficial describe las funciones, pero no muestra cómo combinarlas.** Sabes que existen las habilidades (skills), pero no cómo encadenarlas con delegación, voz y MCP en un flujo de trabajo que realmente ahorre horas.
- **No hay una ruta de aprendizaje clara.** ¿Deberías aprender MCP antes que la delegación? ¿Memoria antes que personalidad? Terminas leyendo todo superficialmente y sin dominar nada.
- **Los ejemplos son demasiado básicos.** Una habilidad de "hello world" no te ayuda a construir un pipeline de servicio al cliente de producción que utilice pasarelas de mensajería, voz y tareas programadas.

Estás desperdiciando el 90% del poder de Hermes Agent — y no sabes lo que no sabes.

---

## Cómo lo Soluciona Hermes How To

Esta no es otra referencia de funciones. Es una **guía estructurada, visual y basada en ejemplos** que te enseña a usar cada función de Hermes Agent con plantillas del mundo real que puedes copiar en tu proyecto hoy mismo.

| | Docs Oficiales | Esta Guía |
|--|---------------|------------|
| **Formato** | Documentación de referencia | Tutoriales visuales con diagramas Mermaid |
| **Profundidad** | Descripciones de funciones | Cómo funciona internamente |
| **Ejemplos** | Fragmentos básicos | Plantillas listas para producción para uso inmediato |
| **Estructura** | Organizada por funciones | Ruta de aprendizaje progresiva (principiante a avanzado) |
| **Onboarding** | Autodirigido | Roadmap guiado con estimaciones de tiempo |
| **Autoevaluación** | Ninguna | Quizzes interactivos para encontrar vacíos y crear una ruta personalizada |

### Lo que obtienes:

- **14 módulos de tutoriales** que cubren cada función de Hermes Agent — desde el inicio rápido hasta las referencias de contexto.
- **Configuraciones para copiar y pegar** — habilidades, plantillas de delegación, configuraciones de MCP, ajustes de voz, integraciones de pasarela de mensajería y paquetes completos de plugins.
- **Diagramas Mermaid** que muestran cómo funciona cada función internamente, para que entiendas el *porqué* y no solo el *cómo*.
- **Una ruta de aprendizaje guiada** que te lleva de principiante a usuario avanzado en 11-13 horas.
- **Autoevaluación integrada** — ejecuta quizzes después de cada módulo para identificar lagunas de conocimiento.

**[Iniciar la Ruta de Aprendizaje](LEARNING-ROADMAP.md)**

---

## Cómo Funciona

### 1. Encuentra tu nivel

Ejecuta `/self-assessment` en Hermes Agent. Obtén un roadmap personalizado basado en lo que ya sabes.

> Disponible tanto en **Modo Rápido** (2 min, 8 preguntas) como en **Modo Profundo** (5 min, 10 dominios con puntuación individual).

### 2. Sigue la ruta guiada

Completa los 14 módulos en orden — cada uno construye sobre el anterior. Copia las plantillas directamente en tu proyecto a medida que aprendes.

### 3. Combina funciones en flujos de trabajo

El verdadero poder reside en la combinación. Aprende a conectar habilidades + delegación + MCP + voz + pasarela de mensajería + cron en pipelines automatizados que gestionen el servicio al cliente, el monitoreo y las integraciones.

### 4. Pon a prueba tu comprensión

Ejecuta `/lesson-quiz [tema]` después de cada módulo. El quiz señala exactamente qué te faltó para que puedas llenar los vacíos rápidamente.

Disponible para los 14 módulos:

| Comando | Módulo |
|---------|--------|
| `/lesson-quiz quickstart` | 01 Inicio Rápido |
| `/lesson-quiz memory` | 02 Memoria |
| `/lesson-quiz skills` | 03 Habilidades |
| `/lesson-quiz delegation` | 04 Delegación |
| `/lesson-quiz mcp` | 05 MCP |
| `/lesson-quiz voice` | 06 Voz |
| `/lesson-quiz messaging` | 07 Pasarela de Mensajería |
| `/lesson-quiz cron` | 08 Cron |
| `/lesson-quiz soul-personality` | 09 Alma y Personalidad |
| `/lesson-quiz toolsets` | 10 Conjuntos de Herramientas |
| `/lesson-quiz plugins` | 11 Plugins |
| `/lesson-quiz checkpoints` | 12 Checkpoints |
| `/lesson-quiz providers` | 13 Proveedores |
| `/lesson-quiz context-refs` | 14 Refs de Contexto |

También puedes usar el número del módulo: `/lesson-quiz 07` = `/lesson-quiz messaging`.

---

## ¿No Sabes por Dónde Empezar?

Realiza la autoevaluación o elige tu nivel:

| Nivel | Puedes... | Empieza aquí | Tiempo |
|-------|-----------|------------|------|
| **Principiante** | Iniciar Hermes Agent y chatear | [Inicio Rápido](01-quickstart/) | ~2.5 horas |
| **Intermedio** | Usar Memoria y Habilidades | [Habilidades](03-skills/) | ~3.5 horas |
| **Avanzado** | Configurar MCP y Delegación | [Delegación](04-delegation/) | ~5 horas |

**Ruta de aprendizaje completa con los 14 módulos:**

| Orden | Módulo | Nivel | Tiempo |
|-------|--------|-------|------|
| 1 | [Inicio Rápido](01-quickstart/) | Principiante | 30 min |
| 2 | [Memoria](02-memory/) | Principiante+ | 45 min |
| 3 | [Habilidades](03-skills/) | Intermedio | 1 hora |
| 4 | [Delegación](04-delegation/) | Intermedio+ | 1.5 horas |
| 5 | [MCP](05-mcp/) | Intermedio+ | 1 hora |
| 6 | [Voz](06-voice/) | Intermedio | 1 hora |
| 7 | [Pasarela de Mensajería](07-messaging-gateway/) | Avanzado | 1.5 horas |
| 8 | [Cron](08-cron/) | Intermedio | 45 min |
| 9 | [ALMA/Personalidad](09-soul-personality/) | Intermedio | 1 hora |
| 10 | [Conjuntos de Herramientas](10-toolsets/) | Avanzado | 1.5 horas |
| 11 | [Plugins](11-plugins/) | Avanzado | 2 horas |
| 12 | [Checkpoints](12-checkpoints/) | Intermedio | 45 min |
| 13 | [Proveedores](13-providers/) | Intermedio | 1 hora |
| 14 | [Refs de Contexto](14-context-refs/) | Avanzado | 1 hora |

**[Roadmap de Aprendizaje Completo](LEARNING-ROADMAP.md)**

---

## Comenzar en 15 Minutos

```bash
# 1. Clonar la guía
git clone https://github.com/wchao-hermes/hermes-howto.git
cd hermes-howto

# 2. Copiar tu primera habilidad
mkdir -p ~/.hermes/skills
cp -r 03-skills/example-skill ~/.hermes/skills/

# 3. Pruébalo — interactúa con la habilidad en Hermes Agent

# 4. ¿Listo para más? Configura la memoria del proyecto:
cp 02-memory/project-HERMES.md /ruta/a/tu-proyecto/HERMES.md

# 5. Configura un proveedor:
cp 13-providers/provider-examples/standard-providers.yaml ~/.hermes/providers/
```

¿Quieres la configuración completa? Aquí tienes la **configuración esencial de 1 hora**:

```bash
# Habilidades (15 min)
cp -r 03-skills/* ~/.hermes/skills/

# Memoria del proyecto (15 min)
cp 02-memory/project-HERMES.md ./HERMES.md

# Plantillas de delegación (15 min)
cp -r 04-delegation/* ~/.hermes/delegation/

# Servidores MCP (15 min)
export GITHUB_TOKEN="***"
hermes mcp add github -- npx -y @modelcontextprotocol/server-github

# Meta del fin de semana: añadir voz, pasarela de mensajería, cron, plugins
# Sigue la ruta de aprendizaje para una configuración guiada
```

---

## ¿Qué Puedes Construir Con Esto?

| Caso de Uso | Funciones que Combinarás |
|----------|------------------------|
| **Bot de Atención al Cliente** | Pasarela de Mensajería + Voz + Habilidades + MCP |
| **Monitoreo Programado** | Cron + Delegación + Checkpoints + Proveedores |
| **Pipeline Multi-agente** | Delegación + ALMA/Personalidad + Conjuntos de Herramientas + Plugins |
| **Asistente de Voz** | Voz + Memoria + Habilidades + MCP |
| **Onboarding de Equipo** | Memoria + Plugins + Refs de Contexto |
| **Automatización DevOps** | Cron + MCP + Checkpoints + Proveedores |
| **Refactorización Compleja** | Checkpoints + Planificación + Delegación |

---

## Preguntas Frecuentes (FAQ)

**¿Es gratuito?**
Sí. Licencia MIT, gratis para siempre. Úsalo en proyectos personales, en el trabajo, en tu equipo — sin restricciones más allá de incluir el aviso de licencia.

**¿Está mantenido?**
Activamente. La guía se sincroniza con cada lanzamiento de Hermes Agent.

**¿En qué se diferencia de la documentación oficial?**
La documentación oficial es una referencia de funciones. Esta guía es un tutorial con diagramas, plantillas listas para producción y una ruta de aprendizaje progresiva. Se complementan entre sí: comienza aquí para aprender, consulta la documentación cuando necesites detalles específicos.

**¿Cuánto tiempo toma completar todo?**
Entre 11 y 13 horas para la ruta completa. Pero obtendrás valor inmediato en 15 minutos: basta con copiar una plantilla de habilidad y probarla.

**¿Puedo contribuir?**
Absolutamente. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para ver las directrices. Agradecemos nuevos ejemplos, corrección de errores, mejoras en la documentación y plantillas de la comunidad.

**¿Puedo leer esto sin conexión?**
Sí. Clona el repositorio y léelo localmente, o genera una versión offline utilizando los scripts.

---

## Comienza a Dominar Hermes Agent Hoy

Ya tienes Hermes Agent instalado. Lo único que te separa de una productividad 10x es saber cómo usarlo. Esta guía te ofrece la ruta estructurada, las explicaciones visuales y las plantillas para lograrlo.

Licencia MIT. Gratis para siempre. Clónalo, haz un fork, hazlo tuyo.

**[Iniciar la Ruta de Aprendizaje](LEARNING-ROADMAP.md)** | **[Explorar el Catálogo de Funciones](INDEX.md)** | **[Comenzar en 15 Minutos](#get-started-in-15-minutes)**

---

<details>
<summary>Navegación Rápida — Todas las Funciones</summary>

| Función | Descripción | Carpeta |
|---------|-------------|--------|
| **Catálogo de Funciones** | Referencia completa con comandos de instalación | [INDEX.md](INDEX.md) |
| **Inicio Rápido** | Guía para comenzar | [01-quickstart/](01-quickstart/) |
| **Memoria** | Contexto persistente | [02-memory/](02-memory/) |
| **Habilidades** | Capacidades reutilizables | [03-skills/](03-skills/) |
| **Delegación** | Delegación de tareas | [04-delegation/](04-delegation/) |
| **Protocolo MCP** | Acceso a herramientas externas | [05-mcp/](05-mcp/) |
| **Voz** | Interacción por voz | [06-voice/](06-voice/) |
| **Pasarela de Mensajería** | Integraciones con plataformas de mensajería | [07-messaging-gateway/](07-messaging-gateway/) |
| **Cron** | Tareas programadas | [08-cron/](08-cron/) |
| **ALMA/Personalidad** | Configuración de la personalidad del agente | [09-soul-personality/](09-soul-personality/) |
| **Conjuntos de Herramientas** | Colecciones de herramientas | [10-toolsets/](10-toolsets/) |
| **Plugins** | Funciones empaquetadas | [11-plugins/](11-plugins/) |
| **Checkpoints** | Instantáneas de sesión y retroceso | [12-checkpoints/](12-checkpoints/) |
| **Proveedores** | Configuración de proveedores de IA | [13-providers/](13-providers/) |
| **Refs de Contexto** | Referencias de contexto | [14-context-refs/](14-context-refs/) |

</details>

<details>
<summary>Comparativa de Funciones</summary>

| Función | Invocación | Persistencia | Ideal Para |
|---------|-----------|------------|----------|
| **Habilidades** | Auto-invocadas | Sistema de archivos | Flujos de trabajo automatizados |
| **Delegación** | Auto-delegada | Contexto aislado | Distribución de tareas |
| **Memoria** | Auto-cargada | Entre sesiones | Aprendizaje a largo plazo |
| **Protocolo MCP** | Auto-consultado | Tiempo real | Acceso a datos en vivo |
| **Voz** | Iniciada por usuario | Sesión | Interacción manos libres |
| **Pasarela de Mensajería** | Activada por evento | Tiempo real | Integraciones de plataforma |
| **Cron** | Programada | Persistente | Tareas recurrentes |
| **ALMA/Personalidad** | Configurada | Persistente | Comportamiento personalizado |
| **Conjuntos de Herramientas** | Auto-disponibles | Sesión | Capacidades extendidas |
| **Plugins** | Un comando | Todas las funciones | Soluciones completas |
| **Checkpoints** | Manual/Auto | Basado en sesión | Experimentación segura |
| **Proveedores** | Configurados | Persistente | Selección de backend de IA |
| **Refs de Contexto** | Auto-inyectadas | Por solicitud | Contexto dinámico |

</details>

<details>
<summary>Referencia Rápida de Instalación</summary>

```bash
# Habilidades
cp -r 03-skills/* ~/.hermes/skills/

# Memoria
cp 02-memory/project-HERMES.md ./HERMES.md

# Delegación
cp -r 04-delegation/* ~/.hermes/delegation/

# MCP
export GITHUB_TOKEN="***"
hermes mcp add github -- npx -y @modelcontextprotocol/server-github

# Voz (configurar en ajustes)
# Ver 06-voice/README.md

# Pasarela de Mensajería
# Ver 07-messaging-gateway/README.md

# Cron
# Ver 08-cron/README.md

# Plugins
/hermes plugin install pr-review

# Checkpoints (activados por defecto, configurar en ajustes)
# Ver 12-checkpoints/README.md

# Proveedores
cp 13-providers/provider-examples/*.yaml ~/.hermes/providers/

# Refs de Contexto
# Ver 14-context-refs/README.md
```

</details>
