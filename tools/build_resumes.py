from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from pathlib import Path
W,H=A4
PORT='https://justjao1.vercel.app/'; GH='https://github.com/JustJao1'; EMAIL='silva.joao.232334@gmail.com'
D={
  "PT": {
    "role": "Desenvolvedor de Software Júnior",
    "location": "São Carlos, SP, Brasil",
    "profile": "Desenvolvedor júnior com projetos independentes em aplicações web, SaaS, Android e automação. Utilizo IA no desenvolvimento, com foco em revisão de código, testes e validação de funcionalidades. Matrícula confirmada em Engenharia de Software para 2027.",
    "sections": [
      "Perfil profissional",
      "Experiência prática e projetos",
      "Competências técnicas",
      "Formação e idiomas"
    ],
    "projects": [
      [
        "Meu Ritmo e Meu Ritmo App",
        "SaaS / Android",
        "Plataforma publicada de organização e finanças com React, TypeScript, Cloudflare, Supabase e Pix (Asaas). App Android com notas offline e alarmes nativos. CI: 392 testes Node e 12 Playwright aprovados.",
        "meuritmo.net",
        "https://meuritmo.net"
      ],
      [
        "Imovance e API Studio",
        "Python / QA",
        "Gestão imobiliária demonstrativa e ferramenta de requisições REST com validação JSON. Suítes unitárias e de integração: 15 e 12 testes aprovados, respectivamente; Imovance com 91% de cobertura no escopo medido.",
        "Evidências",
        "https://justjao1.vercel.app/#engineering"
      ],
      [
        "Traincore, Doc Intelligence e FlowEngine",
        "Web / automação",
        "Planejamento de treinos com assistência de IA, extração de dados de documentos e execução de fluxos JSON condicionais.",
        "Portfólio",
        "https://justjao1.vercel.app/#work"
      ],
      [
        "Pulse Monitor e Freight Connect",
        "Ferramentas web",
        "Demonstrações de monitoramento HTTP, incidentes, busca de cargas e estimativa de custos de viagem.",
        "Portfólio",
        "https://justjao1.vercel.app/#work"
      ],
      [
        "LinkPilot e automações independentes",
        "Experimental",
        "Protótipo Windows para pesquisa de ofertas de afiliados; bots, automações de navegador e planilhas, e experimentos com Roblox Studio (Luau).",
        "GitHub",
        "https://github.com/JustJao1/linkpilot"
      ]
    ],
    "skills": [
      [
        "Front-end",
        "TypeScript, JavaScript, React, Next.js, HTML, CSS"
      ],
      [
        "Back-end",
        "Python, Node.js, REST APIs, SQL, SQLite, Supabase, Cloudflare"
      ],
      [
        "QA e DevOps nos projetos",
        "Playwright, unittest, Docker Compose, Git, GitHub Actions, CI/CD, cobertura"
      ],
      [
        "Outras ferramentas",
        "Vercel, Gradle, Android, Luau, documentação técnica e ADRs"
      ]
    ],
    "edu": [
      [
        "PUC-Campinas",
        "Engenharia de Software | matrícula confirmada, ingresso em 2027."
      ],
      [
        "Ensino médio",
        "Conclusão prevista em 2026."
      ],
      [
        "Idiomas",
        "Português nativo; inglês intermediário."
      ]
    ],
    "focus": "Evidências técnicas e resultados de CI: justjao1.vercel.app/#engineering"
  },
  "EN": {
    "role": "Junior Software Developer",
    "location": "São Carlos, SP, Brazil",
    "profile": "Junior developer with independent projects in web applications, SaaS, Android and automation. I use AI-assisted development with an emphasis on code review, testing and feature validation. Enrolled in Software Engineering for 2027 entry.",
    "sections": [
      "Professional profile",
      "Hands-on experience & projects",
      "Technical skills",
      "Education & languages"
    ],
    "projects": [
      [
        "Meu Ritmo & Meu Ritmo App",
        "SaaS / Android",
        "Released personal planning and finance platform using React, TypeScript, Cloudflare, Supabase and Pix (Asaas). Android app with offline notes and native alarms. CI: 392 Node and 12 Playwright tests passed.",
        "meuritmo.net",
        "https://meuritmo.net"
      ],
      [
        "Imovance & API Studio",
        "Python / QA",
        "Property management demo and REST request tool with JSON assertions. Unit and integration suites: 15 and 12 tests passed, respectively; Imovance reached 91% coverage in the measured scope.",
        "Evidence",
        "https://justjao1.vercel.app/#engineering"
      ],
      [
        "Traincore, Doc Intelligence & FlowEngine",
        "Web / automation",
        "Workout planning with AI assistance, document data extraction and conditional JSON workflow execution.",
        "Portfolio",
        "https://justjao1.vercel.app/#work"
      ],
      [
        "Pulse Monitor & Freight Connect",
        "Web tools",
        "Demos for HTTP monitoring, incident handling, freight search and trip cost estimation.",
        "Portfolio",
        "https://justjao1.vercel.app/#work"
      ],
      [
        "LinkPilot & independent automation",
        "Experimental",
        "Windows affiliate offer discovery prototype; bots, browser and spreadsheet automation, and Roblox Studio (Luau) experiments.",
        "GitHub",
        "https://github.com/JustJao1/linkpilot"
      ]
    ],
    "skills": [
      [
        "Frontend",
        "TypeScript, JavaScript, React, Next.js, HTML, CSS"
      ],
      [
        "Backend",
        "Python, Node.js, REST APIs, SQL, SQLite, Supabase, Cloudflare"
      ],
      [
        "Project QA & DevOps",
        "Playwright, unittest, Docker Compose, Git, GitHub Actions, CI/CD, coverage"
      ],
      [
        "Other tools",
        "Vercel, Gradle, Android, Luau, technical documentation and ADRs"
      ]
    ],
    "edu": [
      [
        "PUC-Campinas",
        "Software Engineering | enrolled for 2027 entry."
      ],
      [
        "High school",
        "Expected completion in 2026."
      ],
      [
        "Languages",
        "Native Portuguese; intermediate English."
      ]
    ],
    "focus": "Technical evidence and CI results: justjao1.vercel.app/#engineering"
  }
}
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
        y-=16;para(desc,10.8,14);y-=8
    y-=3;heading(d['sections'][2])
    for k,v in d['skills']:
        txt=k+': ';draw(M,y,txt,10,'Helvetica-Bold')
        left=M+stringWidth(txt,'Helvetica-Bold',10)
        lines=simpleSplit(v,'Helvetica',10,R-left)
        for line in lines:
            draw(left,y,line,10);y-=14
        y-=2
    y-=12;heading(d['sections'][3])
    for k,v in d['edu']:
        txt=k+' | ';draw(M,y,txt,10,'Helvetica-Bold');draw(M+stringWidth(txt,'Helvetica-Bold',10),y,v,10);y-=16
    y-=3;link(M,y,d['focus'],PORT+'#engineering',9.3,color=TEAL)
    assert y>=26
    c.showPage();c.save()
