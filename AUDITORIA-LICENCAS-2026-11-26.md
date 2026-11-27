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


## Complementação da auditoria e verificação remota

Revisão posterior à criação das tags, em 26/11/2026 (São Paulo). A observação anterior sobre commits não assinados continua aplicável aos commits históricos em si, não às tags assinadas. A API GitHub retornou `verified: true`, `reason: valid` para as onze tags anotadas `autoria-2026-11-26`, com os destinos correspondentes às versões documentadas.

| Projeto | Objeto da tag assinada | Verificação | Relatório individual |
|---|---|---|---|
| meu-ritmo | [`0a5e6961385e178c46055625bf0763edfb680a06`](https://api.github.com/repos/JustJao1/meu-ritmo/git/tags/0a5e6961385e178c46055625bf0763edfb680a06) | valid | [auditoria](https://github.com/JustJao1/meu-ritmo/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| meu-ritmo-app | [`f909fe8c2a4dccf1aef1f2a7e16248f0b2f85939`](https://api.github.com/repos/JustJao1/meu-ritmo-app/git/tags/f909fe8c2a4dccf1aef1f2a7e16248f0b2f85939) | valid | [auditoria](https://github.com/JustJao1/meu-ritmo-app/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| traincore | [`f58ef1da4841da56cafb8654b26383dc01cf4ddb`](https://api.github.com/repos/JustJao1/traincore/git/tags/f58ef1da4841da56cafb8654b26383dc01cf4ddb) | valid | [auditoria](https://github.com/JustJao1/traincore/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| imovance | [`7d64816e57d49953787f3acc1cb0f7daa04be17f`](https://api.github.com/repos/JustJao1/imovance/git/tags/7d64816e57d49953787f3acc1cb0f7daa04be17f) | valid | [auditoria](https://github.com/JustJao1/imovance/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| doc-intelligence | [`bbfdbd23fd5df67fd5e1f1fe07688b5dd4f9afd9`](https://api.github.com/repos/JustJao1/doc-intelligence/git/tags/bbfdbd23fd5df67fd5e1f1fe07688b5dd4f9afd9) | valid | [auditoria](https://github.com/JustJao1/doc-intelligence/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| flow-engine | [`d5c6d6e27e718aff8d5c6d843b37349d108f8ed5`](https://api.github.com/repos/JustJao1/flow-engine/git/tags/d5c6d6e27e718aff8d5c6d843b37349d108f8ed5) | valid | [auditoria](https://github.com/JustJao1/flow-engine/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| pulse-monitor | [`c90b18accb41ea5828691eb3448ebcb1c04b18f2`](https://api.github.com/repos/JustJao1/pulse-monitor/git/tags/c90b18accb41ea5828691eb3448ebcb1c04b18f2) | valid | [auditoria](https://github.com/JustJao1/pulse-monitor/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| freight-connect | [`ca32cde0a1f33bc551c4fd8696d260428acc5753`](https://api.github.com/repos/JustJao1/freight-connect/git/tags/ca32cde0a1f33bc551c4fd8696d260428acc5753) | valid | [auditoria](https://github.com/JustJao1/freight-connect/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| api-studio | [`8184376ed1645d16b33a659628c8932a849a7d2f`](https://api.github.com/repos/JustJao1/api-studio/git/tags/8184376ed1645d16b33a659628c8932a849a7d2f) | valid | [auditoria](https://github.com/JustJao1/api-studio/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| linkpilot | [`9034eba8d3ef14c5ccccf82a0319ccc6d8846abb`](https://api.github.com/repos/JustJao1/linkpilot/git/tags/9034eba8d3ef14c5ccccf82a0319ccc6d8846abb) | valid | [auditoria](https://github.com/JustJao1/linkpilot/blob/HEAD/AUDITORIA-LICENCAS-2026-11-26.md) |
| portfolio | [`4cb1caf72ff5b39b2084027649f3cf9a1940ef1a`](https://api.github.com/repos/JustJao1/portfolio/git/tags/4cb1caf72ff5b39b2084027649f3cf9a1940ef1a) | valid | este documento |

### Portfólio — revisão adicional

- index.html carrega DM Sans e Space Grotesk via Google Fonts, cujo uso comercial é permitido (https://developers.google.com/fonts/). Preservar avisos específicos caso incorporar fontes localmente e verificar os direitos de fontes incorporadas em PDFs.
- As oito capturas JPG são referenciadas em uma versão fixa do próprio repositório; isso comprova a origem do arquivo referenciado, não a titularidade de todos os elementos exibidos. Conferir conteúdo de terceiros, dados pessoais e direitos sobre cada captura antes da reutilização comercial.
- forma/index.html contém uma cópia do Traincore com referências de mídia StrengthLog, Free Exercise DB, Workout Free Videos, Free Exercise DB with Videos e YouTube; valem as restrições e pendências documentadas no relatório Traincore. StrengthLog permite uso somente não comercial com crédito; MIT do Free Exercise DB with Videos cobre código e metadados, não comprova licença comercial dos vídeos. Não monetizar a mídia sem autorização nem presumir licença pela disponibilidade da URL.
- LinkPilot continua sendo documentação de software experimental; não há código integral nem executável no repositório.

### Prioridades restantes

1. Traincore e cópia no portfólio: substituir ou obter autorização para mídia de uso comercial antes de monetizar. Não foi feita alteração de funcionalidade ou remoção de mídia nesta auditoria.
2. Meu Ritmo: [inventário de 893 entradas npm por versão](https://github.com/JustJao1/meu-ritmo/blob/HEAD/AUDITORIA-NPM-2026-11-26.md); revisar distribuição efetiva de MPL/LGPL, atribuições e textos originais. Nenhuma entrada sem metadado de licença, o que não garante conformidade.
3. Doc Intelligence: confirmar licença e proveniência dos pesos ONNX e resolver dependências Python por versão.
4. Freight Connect: verificar conformidade operacional dos mapas e rotas; preservar atribuições e política de tiles.
5. Meu Ritmo App: auditar dependências Android resolvidas e APK real. LinkPilot: recuperar fonte e binário antes da auditoria integral.
6. Fazer um novo commit assinado no computador do responsável e verificar o selo GitHub. Os commits desta revisão documental foram realizados por integração, não com a chave privada pessoal. As tags antigas permanecem intactas.

Nenhum gasto ou mudança de licença do código próprio foi autorizado. Esta revisão é documental, não uma certificação legal, não inclui execução dos builds ou exame de todos os artefatos distribuídos.
