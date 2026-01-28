# LogiTrack - Sistema de Gestión de Almacén

Sistema diseñado para **optimizar la salida de pedidos** y mejorar la **comunicación interna** en operaciones de almacén.

## ¿Qué hace LogiTrack?

LogiTrack es una herramienta sencilla pero potente que te ayuda a:

- **Controlar el flujo de pedidos** desde que entran hasta que salen del almacén
- **Priorizar envíos urgentes** para que nunca se quede atrás un pedido importante
- **Detectar incidencias** como falta de stock antes de que se conviertan en problemas
- **Comunicar el estado** de cada pedido a todo el equipo en tiempo real

## Estructura del Proyecto

```
LogiTrack/
├── docs/
│   └── MANUAL_OPERATIVO.md    # Reglas de oro y procedimientos
├── prompts/
│   └── setup_log.md           # Log de configuración
└── README.md                  # Este archivo
```

## Flujo de Trabajo

El sistema organiza los pedidos en **7 etapas** visuales:

| Etapa | Descripción |
|-------|-------------|
| 📥 Pedidos por Entrar | Nuevos pedidos recibidos |
| 🔥 PRIORIDAD | Envíos que deben salir HOY |
| 🛠️ En Preparación | Pedidos siendo recogidos |
| 📦 Embalaje y Packing | Empaquetado en proceso |
| 🏷️ Etiquetado y Listo | Preparado para envío |
| 🚚 Enviados / Salida | Pedidos despachados |
| ⚠️ Incidencias | Pedidos con problemas |

## Documentación

Consulta el [Manual Operativo](docs/MANUAL_OPERATIVO.md) para conocer las reglas de oro del almacén y los procedimientos estándar.

---

## Caso de Estudio: Simulación de Pico de Trabajo

### Contexto

Durante 4 días de operación intensiva, LogiTrack gestionó **28 pedidos simultáneos** de forma organizada y sin pérdida de información.

### Distribución del Flujo

| Etapa | Pedidos | Estado |
|-------|---------|--------|
| 📥 Recepción | 5 | Nuevos (día actual) |
| 🔥 PRIORIDAD | 6 | Urgentes con vencimiento HOY |
| 🛠️ Preparación | 5 | En proceso (~50% completados) |
| 📦 Embalaje | 3 | Listos para packing |
| 🏷️ Listo | 2 | Esperando recogida |
| 🚚 Enviados | 8 | Completados (últimos 2 días) |
| ⚠️ Incidencias | 6 | Problemas documentados |

### Resultados Clave

- **0 pedidos perdidos**: Cada pedido tiene seguimiento visual desde entrada hasta salida
- **Incidencias documentadas**: Falta de stock, direcciones incorrectas y duplicados identificados antes de afectar al cliente
- **Priorización efectiva**: Pedidos VIP con fechas de vencimiento siempre visibles en la columna de prioridad
- **Transportistas identificados**: Etiquetas de color (🔵 DHL, 🟠 SEUR, 🟣 Local) permiten agrupar envíos

### Lecciones Aprendidas

1. **El sistema de 7 columnas** permite ver de un vistazo el cuello de botella del almacén
2. **Los checklists al 50%** muestran pedidos que necesitan atención prioritaria
3. **Las incidencias separadas** evitan que bloqueen el flujo normal de trabajo
4. **Las portadas de color** destacan visualmente los pedidos críticos

---

## Licencia

MIT License - Uso libre para cualquier propósito.
