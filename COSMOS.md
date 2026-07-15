# Guía de Conexión y Gestión de Base de Datos - ImpactX Database Infra

Esta guía contiene la configuración de acceso a **Azure Cosmos DB NoSQL** y pautas para su administración y aprovisionamiento.

## Credenciales de Conexión (Desarrollo / Pruebas)

* **Account Endpoint:** `https://impactx-db-west-final.documents.azure.com:443/`
* **Account Key (Lectura y Escritura):** `<REPLACE_WITH_YOUR_COSMOS_KEY>`
* **Base de Datos Principal:** `ImpactX-Data`
* **Base de Datos Temporal/Test:** `TestDatabase`

---

## 🛠️ Tareas de Infraestructura de Base de Datos

En este repositorio se administra la creación y aprovisionamiento de bases de datos, contenedores, claves de partición e indexación.

### Parámetros Clave para Nuevos Contenedores:
1. **Partition Key (Clave de Partición):** Debe elegirse según los patrones de consulta para evitar consultas "cross-partition" costosas. Ejemplos sugeridos: `/partitionKey`, `/userId`, `/tenantId`.
2. **Throughput (Rendimiento):** Para pruebas y desarrollo local se recomienda usar la base de datos con throughput compartido o modo Serverless para optimizar costos de consumo de Azure (RUs).

---

## Cómo usar Cosmos DB Studio para Validaciones Locales

Como administrador de infraestructura, puedes usar Cosmos DB Studio para auditar el rendimiento, RUs consumidas y la estructura de los datos sin entrar al Azure Portal.

1. Descarga e instala **Cosmos DB Studio**.
2. Crea una nueva conexión ingresando los siguientes datos:
   * **Name:** `ImpactX`
   * **Endpoint:** `https://impactx-db-west-final.documents.azure.com:443/`
   * **Key:** `<REPLACE_WITH_YOUR_COSMOS_KEY>`
   * **Serverless:** Desmarcado
   * **Folder:** En blanco
3. Haz clic en **OK**.
4. Haz doble clic en un contenedor (por ejemplo, `TestContainer` o un contenedor dentro de `ImpactX-Data`).
5. En la ventana central escribe:
   ```sql
   SELECT * FROM c
   ```
6. Haz clic en el botón de **Play (Triángulo Negro)**.
7. La pestaña **Raw** en el panel inferior te mostrará detalles técnicos como el costo exacto de Request Charge (RUs) y el `_etag` para verificar la concurrencia.
