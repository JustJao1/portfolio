from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from pathlib import Path
W,H=A4
PORT='https://justjao1.vercel.app/'; GH='https://github.com/JustJao1'; EMAIL='silva.joao.232334@gmail.com'
D={
'PT':dict(role='Desenvolvedor Júnior de Software',location='São Carlos, SP, Brasil',profile='Desenvolvedor júnior e estudante de Engenharia de Software. Desenvolvo aplicações web, aplicativos Android e ferramentas de automação, incluindo um SaaS próprio publicado. Utilizo IA como apoio à pesquisa, à prototipagem e à depuração de código.',sections=['Perfil','Experiência prática e projetos','Competências técnicas','Formação e idiomas'],projects=[('Meu Ritmo e Meu Ritmo App','SaaS / Android','Desenvolvi e publiquei uma plataforma de organização pessoal com agenda, finanças, autenticação e pagamentos Pix. Aplicativo Android complementar com APK, notas offline e alarmes nativos.','meuritmo.net','https://meuritmo.net'),('Imovance','Demonstração web','Sistema demonstrativo de gestão imobiliária com inventário, manutenção e registros financeiros, usando Python, SQLite e JavaScript.','GitHub',GH+'/imovance'),('Doc Intelligence e FlowEngine','Documentos / automação','Pesquisa e extração de dados em documentos, comparação de versões e editor visual de fluxos com condições, transformações JSON e histórico de execução.','Portfólio',PORT+'#work'),('Pulse Monitor, Freight Connect e API Studio','Ferramentas web','Demonstrações de monitoramento HTTP e incidentes, busca de cargas e estimativa de custos, além de requisições HTTP e validação de respostas JSON.','Portfólio',PORT+'#work'),('LinkPilot','Desktop experimental','Protótipo Windows v0.7.1 para pesquisa de ofertas de afiliados e seleção de produtos com IA; integrações e automação em fase de testes.','GitHub',GH+'/linkpilot'),('Automação e scripts','Projetos independentes','Bots e fluxos de navegador para empresa privada, automações de planilhas e experimentos com interfaces e mecânicas no Roblox Studio (Luau).',None,None)],skills=[('Web','JavaScript, TypeScript, React, Next.js, HTML, CSS'),('Backend e integrações','Python, Node.js, REST APIs, SQL, SQLite, Supabase, Cloudflare'),('Ferramentas','Git, GitHub Actions, Vercel, Gradle, Luau, testes e depuração')],edu=[('PUC-Campinas','Engenharia de Software | matrícula confirmada, ingresso em 2027.'),('Ensino médio','Último ano; conclusão prevista para 2026.'),('Idiomas','Português nativo; inglês intermediário.')],focus='Foco atual: aprofundar testes, documentação e confiabilidade das integrações.'),
'EN':dict(role='Junior Software Developer',location='São Carlos, SP, Brazil',profile='Junior developer and Software Engineering student. I build web applications, Android apps and automation tools, including my own released SaaS product. I use AI to support research, prototyping and debugging.',sections=['Profile','Hands-on experience & projects','Technical skills','Education & languages'],projects=[('Meu Ritmo & Meu Ritmo App','SaaS / Android','Built and released a personal organization platform with planning, finance, authentication and Pix payments. Android companion app with APK releases, offline notes and native alarms.','meuritmo.net','https://meuritmo.net'),('Imovance','Web demo','Property management demo for inventory, maintenance and financial records using Python, SQLite and JavaScript.','GitHub',GH+'/imovance'),('Doc Intelligence & FlowEngine','Documents / automation','Document search, field extraction and version comparison, plus a visual workflow editor with conditional branches, JSON transformations and execution history.','Portfolio',PORT+'#work'),('Pulse Monitor, Freight Connect & API Studio','Web tools','Demos for HTTP monitoring and incidents, freight search and cost estimation, and HTTP requests with JSON response assertions.','Portfolio',PORT+'#work'),('LinkPilot','Experimental desktop','Windows v0.7.1 prototype for affiliate offer discovery and AI-assisted product selection; integrations and automation are still under testing.','GitHub',GH+'/linkpilot'),('Automation & scripting','Independent projects','Bots and browser workflows for a private business, spreadsheet automations and experiments with interfaces and game mechanics in Roblox Studio (Luau).',None,None)],skills=[('Web','JavaScript, TypeScript, React, Next.js, HTML, CSS'),('Backend & integrations','Python, Node.js, REST APIs, SQL, SQLite, Supabase, Cloudflare'),('Tools','Git, GitHub Actions, Vercel, Gradle, Luau, testing and debugging')],edu=[('PUC-Campinas','Software Engineering | enrolled for 2027 entry.'),('High school','Final year; expected completion in 2026.'),('Languages','Native Portuguese; intermediate English.')],focus='Current focus: deepen testing, documentation and integration reliability.')}
NAVY=HexColor('#163348'); TEAL=HexColor('#087e89'); TEXT=HexColor('#263440'); SUB=HexColor('#536575'); LINE=HexColor('#c7d6dc')
for lang,d in D.items():
    path=Path('Joao_Victor_Curriculo_PT.pdf' if lang=='PT' else 'Joao_Victor_Resume_EN.pdf')
    c=canvas.Canvas(str(path),pagesize=A4,pageCompression=1,invariant=1); c.setTitle('João Victor da Silva | '+d['role']);c.setAuthor('João Victor da Silva')
    M=42; R=W-M
    c.setFillColor(NAVY);c.rect(0,H-121,W,121,fill=1,stroke=0);c.setFillColor(TEAL);c.rect(0,H-121,W,4,fill=1,stroke=0)
    def draw(x,y,s,size=10.5,font='Helvetica',color=TEXT):
        c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,s)
    def link(x,y,s,url,size=9.2,color=TEAL):
        draw(x,y,s,size,color=color);c.linkURL(url,(x,y-2,x+stringWidth(s,'Helvetica',size),y+size+2),relative=0,thickness=0)
    WHITE=HexColor('#ffffff'); PALE=HexColor('#e1e9ee')
    draw(M,H-43,'João Victor da Silva',27,'Helvetica-Bold',WHITE);draw(M,H-65,d['role'],14.3,color=WHITE)
    draw(M,H-84,d['location'],9.5,color=PALE);link(M+165,H-84,EMAIL,'mailto:'+EMAIL,9.5,PALE)
    link(M,H-101,'justjao1.vercel.app',PORT,9.5,PALE);link(M+165,H-101,'github.com/JustJao1',GH,9.5,PALE)
    y=H-143
    def heading(s):
        global y
        draw(M,y,s,12.4,'Helvetica-Bold',TEAL);y-=7;c.setStrokeColor(LINE);c.setLineWidth(.6);c.line(M,y,R,y);y-=13
    def para(s,size=11,lead=15):
        global y
        for line in simpleSplit(s,'Helvetica',size,R-M):draw(M,y,line,size);y-=lead
    heading(d['sections'][0]);para(d['profile']);y-=14
    heading(d['sections'][1])
    for name,tag,desc,label,url in d['projects']:
        draw(M,y,name,11.2,'Helvetica-Bold',NAVY);width=stringWidth(name,'Helvetica-Bold',11.2)
        tag_x=M+width+9;tw=stringWidth(tag,'Helvetica',9.1)
        lx=R-stringWidth(label or '','Helvetica',9.2)
        if tag_x+tw+8<lx:draw(tag_x,y,tag,9.1,color=SUB)
        if label:link(lx,y,label,url)
        y-=16;para(desc,10.9,14.5);y-=9
    y-=3;heading(d['sections'][2])
    for k,v in d['skills']:
        txt=k+': ';draw(M,y,txt,10,'Helvetica-Bold');draw(M+stringWidth(txt,'Helvetica-Bold',10),y,v,10);y-=16
    y-=12;heading(d['sections'][3])
    for k,v in d['edu']:
        txt=k+' | ';draw(M,y,txt,10,'Helvetica-Bold');draw(M+stringWidth(txt,'Helvetica-Bold',10),y,v,10);y-=16
    y-=3;draw(M,y,d['focus'],9.3,color=SUB)
    assert y>=26
    c.showPage();c.save()
