# Localiza Bodega Operativa para Odoo 19

Módulo para Odoo.sh v19 integrado con Inventario.

## Incluye

- App independiente: **Bodega Operativa**.
- Extensión de ficha de producto con campos operativos Localiza.
- Puestos con creación automática de ubicaciones internas.
- GPS / equipos seriados con IMEI, cliente, placa, proveedor y lote Odoo.
- Entregas operativas con transferencia interna de inventario.
- Importador Excel para:
  - Uniformes / botas.
  - Insumos operativos.
  - Inventario GPS.
- Seguridad por grupos:
  - Usuario.
  - Responsable.

## Instalación en Odoo.sh

1. Copia la carpeta `localiza_bodega_operativa` dentro de tu repositorio de addons.
2. Sube cambios a GitHub.
3. En Odoo.sh actualiza Apps.
4. Busca **Localiza Bodega Operativa**.
5. Instala.
6. Asigna el grupo **Bodega Operativa / Responsable** al usuario administrador.

## Nota de seguridad

Este módulo está diseñado para bodega operativa general: uniformes, insumos, GPS, puestos y entregas. No incluye flujos específicos para armas ni objetos peligrosos.

## Corrección Odoo 19

Este paquete usa `res.groups.privilege` y `privilege_id` en seguridad, ya que en Odoo 19 `res.groups.category_id` fue removido.
