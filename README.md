
# P2 A2.2 - Pruebas de caja blanca

## Etapa 1: Statement Coverage
Se ejecuta `test_statement_coverage` para evaluar la cobertura de sentencias.

## Etapa 2: Branch Coverage
Se ejecuta `test_branch_coverage` con pytest-cov y `--cov-branch`.

## Etapa 3: Path Coverage
Se ejecuta `test_path_coverage` para probar diferentes caminos de ejecución.

Nota: pytest-cov mide sentencias y ramas, pero no calcula directamente la cobertura total de caminos.
