# Forma

Aplicação web de planejamento de treino, academia e calistenia, com acompanhamento local e assistentes de IA de treino e nutrição.

- Demonstração independente: https://forma-training-three.vercel.app/
- Autor: João Victor da Silva (JustJao1)

## Estrutura para um repositório independente

- Copie `forma/index.html` para `index.html` na raiz.
- Copie `api/forma-chat.js` para `api/forma-chat.js` na raiz do novo repositório.
- Publique na Vercel como projeto sem framework. O endpoint usa AI Gateway com OIDC da Vercel ou uma variável de servidor AI_GATEWAY_API_KEY. Nunca inclua chaves no código.

## Funcionalidades

Editor de planos, 55 exercícios, marcações, cronômetro, histórico, exportação/importação de backup, compartilhamento por código e assistentes conversacionais.

## Limitações

Projeto beta. Os dados ficam no navegador; não há contas ou sincronização. Referências fotográficas externas: Free Exercise DB (https://github.com/yuhonas/free-exercise-db). Algumas fichas usam diagramas indicativos. Vídeos são links de busca, não vídeos integrados. A IA não substitui profissionais de saúde e as respostas dependem do provedor. Os dados de uma ficha privada não são distribuídos como plano padrão.
