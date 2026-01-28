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

## Licencia

MIT License - Uso libre para cualquier propósito.
