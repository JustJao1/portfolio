# Auditoria documental de licenças — 26/11/2026

Responsável: João Victor da Silva (JustJao1). Escopo: versões indicadas nos arquivos EVIDENCIA-2026-11-26.md dos onze repositórios. Inventário preliminar baseado no código, nos READMEs, nos arquivos de licença e nas dependências declaradas. Não é certificação jurídica, SBOM completo nem auditoria de todas as dependências transitivas.

| Projeto | Evidência de terceiros | Verificação/pendência |
| --- | --- | --- |
| Meu Ritmo | THIRD_PARTY_NOTICES.md; public/fonts/LICENSE.txt (Open Sans); public/licenses/lucide.txt; package.json (React, Next, Zod, Drizzle, etc.) | Preservar avisos; conferir licenças de todas as versões travadas e transitivas antes de redistribuir. Termos de Cloudflare, Supabase, Asaas e outros provedores são distintos de licenças de código. |
| Meu Ritmo App | app-web/fonts/LICENSE.txt identifica Open Sans Apache-2.0; Android Gradle e SDK | Preservar créditos e licença da fonte, verificar dependências e certificado da versão APK efetivamente distribuída. Configuração de assinatura no Gradle não demonstra assinatura de um APK específico. |
| Traincore | README.md informa Free Exercise DB, Workout Free Videos (CC0 conforme fonte), Free Exercise DB with Videos, StrengthLog, YouTube; Vercel AI Gateway | Direitos de mídia não são do projeto. Licença de metadados/código não implica licença de vídeo; verificar permissões de incorporação/hotlink, uso comercial e disponibilidade. Até confirmar, preferir links para páginas oficiais e materiais CC0/licenciados. |
| Imovance | README informa Python stdlib; static/index.html usa Google Fonts | Conferir fontes, ativos e eventuais integrações opcionais de Asaas/IA; não certificar todos os ativos. |
| Doc Intelligence | THIRD_PARTY_NOTICES.md; requirements.txt: pypdf, openpyxl; fontes Google, Transformers.js e modelo Hugging Face opcional | pypdf BSD-3-Clause, openpyxl MIT conforme aviso existente; conferir dependências transitivas, versão e licença do modelo antes de redistribuir. |
| FlowEngine | requirements.txt: biblioteca padrão; THIRD_PARTY_NOTICES.md: Google Fonts | Preservar licenças de fontes; conferir scripts e ativos externos. |
| Pulse Monitor | requirements.txt: biblioteca padrão; THIRD_PARTY_NOTICES.md: Google Fonts | Preservar licenças de fontes; conferir scripts e ativos externos. |
| Freight Connect | THIRD_PARTY_NOTICES.md: Leaflet BSD-2-Clause, OSM ODbL; OSRM serviço externo; public/municipios-LICENSE.txt: MIT de Kelvin S. do Prado | Manter atribuição no mapa, dados e avisos; observar política de tiles/rotas e ODbL para redistribuição. |
| API Studio | requirements.txt: biblioteca padrão; THIRD_PARTY_NOTICES.md: Google Fonts | Preservar licenças de fontes e conferir ativos externos. |
| LinkPilot | README indica Go, API de marketplaces e Gemini; código-fonte completo indisponível no repositório | Auditoria de dependências e executável impossível sem recuperar fonte e binário. Nenhum registro de assinatura do binário foi confirmado. |
| Portfólio | DM Sans, Space Grotesk via Google Fonts; screenshots de projetos; ilustrações e PDFs | Conferir direitos sobre cada ativo; manter créditos das fontes e não publicar documentos pessoais assinados no repositório público. |

Os arquivos OWNERSHIP.md identificam responsabilidade e titularidade declarada; não transferem direitos de terceiros, não garantem exclusividade de marcas e não são registros no INPI. Não foi concedida nova licença de distribuição. Os commits auditados não tinham assinatura criptográfica verificada. Nenhum gasto autorizado ou serviço contratado.
