# Traincore — cópia de demonstração

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

Projeto beta. Os dados ficam no navegador; não há contas ou sincronização. Referências ilustradas licenciadas conforme seção abaixo. A IA não substitui profissionais de saúde e as respostas dependem do provedor. Os dados de uma ficha privada não são distribuídos como plano padrão.

## Mídia e direitos de uso — versão atualizada

Todos os 55 exercícios têm ilustrações de referência do RepDB Free Tier; 53 têm posições inicial e final, e 15 têm também vídeos do Workout Free Videos. Algumas variantes ilustradas têm observação de equipamento. As sequências de duas imagens não são vídeos contínuos.

- **Exercise data by [RepDB (repdb.co)](https://repdb.co/)**. [Licença Free Tier v1.0](https://github.com/RepDB/exercise-dataset/blob/main/LICENSE-DATA.md): uso pessoal e comercial dentro de aplicativos, com atribuição visível; proibida redistribuição como dataset ou API e uso de imagens para derivação por IA. Não se usam amostras pagas. O aplicativo referencia apenas os arquivos necessários, sem copiar ou redistribuir o dataset. Versão de referência: `f12da458a90f353a86c953f204304d5a8bd98275`.
- [Workout Free Videos](https://github.com/namnq/workout-free-videos), versão v2.0.0: vídeos declarados CC0 1.0 Universal pelo mantenedor, com uso comercial permitido. Crédito preservado.
- Removidas as imagens e GIFs StrengthLog, fotografias Free Exercise DB de origem não confirmada, mídias do Free Exercise DB with Videos sem licença específica comprovada e prévias de terceiros. A busca externa de vídeos permanece como link, sem cópia nem incorporação automática de resultados.
- Arquivos e links personalizados permanecem locais, via IndexedDB; use somente materiais próprios ou autorizados. Não acompanham os códigos de compartilhamento ou backups JSON. Limites: 80 MB por vídeo e 12 MB por imagem.
- As mídias permanecem de seus titulares. O Traincore é gratuito, sem monetização planejada. As ilustrações são educativas e não substituem orientação profissional. Disponibilidade das fontes externas não é garantida.
