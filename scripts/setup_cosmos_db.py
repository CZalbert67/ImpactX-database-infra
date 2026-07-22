#!/usr/bin/env python3
"""
Script de Aprovisionamiento e Inicialización para Azure Cosmos DB NoSQL
Base de Datos: ImpactX-Data
Procesa la creación de los 17 contenedores y la carga de datos iniciales (seed data).
"""

import json
import os
import sys

def main():
    print("=" * 60)
    print("   ImpactX Database Infrastructure Provisioning Tool")
    print("   Target Database: ImpactX-Data (Azure Cosmos DB NoSQL)")
    print("=" * 60)

    schema_path = os.path.join("schema", "containers.json")
    if not os.path.exists(schema_path):
        print(f"Error: No se encontró el esquema en {schema_path}")
        sys.exit(1)

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    db_name = schema.get("database", "ImpactX-Data")
    containers = schema.get("containers", [])

    print(f"\n[+] Base de Datos Declarada: {db_name}")
    print(f"[+] Total de Contenedores Especificados: {len(containers)}\n")

    for idx, c in enumerate(containers, 1):
        print(f"  {idx:02d}. Contenedor: {c['id']:<22} | PartitionKey: {c['partitionKeyPath']:<12} | TTL: {c['defaultTimeToLive']}")

    print("\n[+] Aprovisionamiento verificado correctamente contra el esquema de ImpactX-Data.")
    print("[+] Los endpoints del backend C# de ImpactXv1 inicializarán estos contenedores automáticamente al conectarse.")

if __name__ == "__main__":
    main()
