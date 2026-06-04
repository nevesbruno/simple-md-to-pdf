# Changelog

Todas as mudancas notaveis neste projeto serao documentadas neste arquivo.

O formato e baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-06-04

### Fixed

- Adicionado `reports/` ao `.gitignore` para evitar versionamento de artefatos de outros projetos

## [0.1.0] - 2026-06-04

### Added

- Sistema de logging verbose com prefixos visuais (`[*]`, `[+]`, `[-]`, `[!]`)
- Banner de inicializacao no CLI (`RENDER.PY - Markdown to PDF Converter`)
- Exemplo de uso no help de argumentos invalidos
- Variavel `__version__` e `__version_info__` no modulo

### Changed

- Refatoracao da funcao `convert_md_to_pdf` para usar `Path` objects e aceitar parametro `verbose`
- CLI agora usa `sys.exit(1)` com try/except para erros especificos
- Mensagens de erro padronizadas (PT-BR, sem acentos para compatibilidade terminal)
- Melhor descritivo de progresso durante a conversao (tamanho arquivo, linhas, extensoes, tamanho PDF)
