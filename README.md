# ImpactX Database Infrastructure (`ImpactX-database-infra`)

Este repositorio contiene la arquitectura de infraestructura, especificación de contenedores NoSQL, claves de partición y datos semillas para la base de datos **`ImpactX-Data`** en **Azure Cosmos DB NoSQL**.

---

## 📌 Base de Datos Objetivo: `ImpactX-Data`

* **Tipo:** Azure Cosmos DB (Core NoSQL API)
* **Nombre de Base de Datos:** `ImpactX-Data` (Configurada en nivel gratuito / cuota de promoción para optimización de costos).
* **Endpoint:** `https://impactx-db-west-final.documents.azure.com:443/`

---

## 🗄️ Esquema de Contenedores NoSQL (17 Contenedores)

Todos los datos generados por los 94 endpoints del backend `ImpactXv1` se almacenan exclusivamente en los siguientes contenedores dentro de `ImpactX-Data`:

| Contenedor | Partition Key | TTL Predeterminado | Propósito |
| :--- | :--- | :--- | :--- |
| **`Usuarios`** | `/id` | Sin expiración (-1) | Perfiles de usuarios, preferencias, datos de conductor y perfil médico. |
| **`RefreshTokens`** | `/usuarioId` | 7 días (604800 s) | Tokens JWT de sesión activa. |
| **`PasswordResetTokens`**| `/usuarioId` | 1 hora (3600 s) | Tokens de recuperación de contraseña. |
| **`Planes`** | `/id` | Sin expiración (-1) | Catálogo de planes de suscripción (Básico, Pro, Familiar). |
| **`Suscripciones`** | `/usuarioId` | Sin expiración (-1) | Estado de suscripciones activas por usuario. |
| **`Pagos`** | `/usuarioId` | Sin expiración (-1) | Registro transaccional de cobros y facturación. |
| **`Monitores`** | `/usuarioId` | Sin expiración (-1) | Red de monitores y supervisores vinculados. |
| **`ContactosEmergencia`**| `/usuarioId` | Sin expiración (-1) | Contactos de emergencia para alertas SOS. |
| **`Rutas`** | `/usuarioId` | Sin expiración (-1) | Rutas y trayectos habituales. |
| **`Viajes`** | `/usuarioId` | 90 días (7776000 s) | Histórico de viajes ejecutados. |
| **`TelemetriaViaje`** | `/viajeId` | 90 días (7776000 s) | Lecturas físicas de sensores kinéticos y acelerómetro. |
| **`Alertas`** | `/usuarioId` | 365 días (31536000 s)| Registro de alertas de impacto y eventos SOS. |
| **`Notificaciones`** | `/usuarioId` | 30 días (2592000 s) | Bandeja de entrada de notificaciones del usuario. |
| **`Wearables`** | `/usuarioId` | Sin expiración (-1) | Dispositivos Smartwatch y sensores BLE enlazados. |
| **`AppInvites`** | `/usuarioId` | 30 días (2592000 s) | Invitaciones enviadas a familiares/monitores. |
| **`ChatThreads`** | `/usuarioId` | Sin expiración (-1) | Canales de mensajería interna. |
| **`Incidentes`** | `/usuarioId` | Sin expiración (-1) | Expediente técnico de colisiones e incidentes. |

---

## 📁 Archivos de Configuración y Semillas

* **`schema/containers.json`**: Especificación técnica completa de los 17 contenedores en JSON.
* **`seed_data/`**: Documentos semilla en formato JSON (`planes.json`, `usuarios_sample.json`, `wearables_sample.json`).
* **`scripts/setup_cosmos_db.py`**: Script de verificación de esquema y estructura.