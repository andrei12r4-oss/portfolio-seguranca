# 🗓️ Cronograma Completo de Estudos

> **Bootcamp Cibersegurança Santander / DIO**  
> Prazo final para conclusão com certificado: **20/12/2026**

---

## 📌 Guia de Uso do Cronograma
1. Ao iniciar cada semana, crie um arquivo em `anotacoes/semana-XX.md` duplicando o template em [`anotacoes/semana-01-template.md`](anotacoes/semana-01-template.md).
2. Marque os itens no checklist conforme for executando.
3. Toda **sexta-feira**, valide o progresso no checkpoint semanal.

---

### Semana 1: 27/10 a 02/11 — IA e Agentes
* **Carga Horária Estimada:** ~7 horas
* **Módulo do Curso:** Fundamentos de Inteligência Artificial e Agentes Inteligentes
* **Metas de Prática & Portfólio:**
  * [ ] Inicializar o repositório principal no GitHub com estrutura organizada de pastas.
  * [ ] Elaborar e documentar `README.md` introdutório sobre **Fundamentos de IA aplicados à Segurança da Informação**.
  * [ ] Levantar casos de uso de IA tanto para defesa cibernética (SIEM, detecção de anomalias) quanto para vetores de ataque.
* **Entregáveis da Semana:**
  - Repositório criado e versionado no Git.
  - Documento base sobre IA & Cibersegurança publicado.

---

### Semana 2: 03/11 a 09/11 — Linux e Máquinas Virtuais
* **Carga Horária Estimada:** ~5 horas
* **Módulo do Curso:** Introdução ao Linux, Virtualização e Ambientes de Laboratório
* **Metas de Prática & Portfólio:**
  * [ ] Configurar ambiente de laboratório isolado local (VirtualBox ou VMware).
  * [ ] Instalar e configurar Kali Linux / Parrot OS como máquina atacante.
  * [ ] Instalar uma máquina vulnerável para testes controlados (ex: Metasploitable 2/3 ou DVWA).
  * [ ] Escrever um guia prático com comandos essenciais de Linux para segurança ofensiva/defensiva.
  * [ ] Desenvolver e versionar um script básico de automação em Bash (ex: checagem de integridade, coleta de informações do sistema).
* **Entregáveis da Semana:**
  - `docs/guia-linux-essencial.md`
  - `scripts/linux-recon-basico.sh`

---

### Semana 3: 10/11 a 16/11 — Fundamentos de Cibersegurança + Pentest (Parte 1)
* **Carga Horária Estimada:** ~5 horas
* **Módulo do Curso:** Pilares de Segurança, Ameaças e Início de Testes de Intrusão
* **Metas de Prática & Portfólio:**
  * [ ] Documentar os conceitos fundamentais: Tríade CIA (Confidencialidade, Integridade, Disponibilidade) e OWASP Top 10.
  * [ ] Iniciar estudos e documentação das fases de Reconhecimento e Varredura (Footprinting & Scanning).
  * [ ] Realizar varreduras laboratoriais com **Nmap** (identificação de portas abertas, versões de serviços e detecção de SO).
  * [ ] Salvar exemplos de saídas (`-sV`, `-sC`, `-O`, `-p-`) comentados didaticamente.
* **Entregáveis da Semana:**
  - `docs/fundamentos-cia-owasp.md`
  - `writeups/recon-nmap-laboratorio.md`

---

### Semana 4: 17/11 a 23/11 — Pentest (Parte 1 - Continuação)
* **Carga Horária Estimada:** ~5 horas
* **Módulo do Curso:** Análise de Redes, Captura de Pacotes e Mapeamento
* **Metas de Prática & Portfólio:**
  * [ ] Executar laboratório prático de captura e inspeção de tráfego de rede utilizando o **Wireshark**.
  * [ ] Analisar fluxos de protocolos comuns (HTTP, DNS, TCP Handshake, ARP).
  * [ ] Realizar exercícios complementares de scan e enumeração de vulnerabilidades.
  * [ ] Elaborar relatórios técnicos devidamente **sanitizados** (atenção: mascarar IPs públicos, nomes de máquinas sensíveis e credenciais).
* **Entregáveis da Semana:**
  - `writeups/analise-trafego-wireshark.md`
  - Relatórios de scans sanitizados.

---

### Semana 5: 24/11 a 30/11 — Pentest (Parte 2) + 1º Desafio de Projeto
* **Carga Horária Estimada:** ~5 horas (bootcamp) + horas excedentes (ShopAI)
* **Módulo do Curso:** Exploração, Pós-Exploração e Entrega do Desafio 1
* **Metas de Prática & Portfólio:**
  * [ ] Concluir integralmente o **1º Desafio de Projeto Oficial** do Bootcamp Santander/DIO.
  * [ ] Escrever relatório técnico da solução, detalhando problema, metodologia adotada, comandos e conclusões.
  * [ ] Publicar no GitHub a documentação do desafio em formato de portfólio.
* **Regra Especial de Transição (ShopAI):**
  * A partir desta semana, o projeto ShopAI pode ser rodado em paralelo exclusivamente nas horas sobressalentes.
* **Entregáveis da Semana:**
  - Pasta do Desafio 1 com documentação completa.

---

### Semana 6: 01/12 a 07/12 — Proteção Contra Ataques & Defesa (Blue Team)
* **Carga Horária Estimada:** ~5 horas
* **Módulo do Curso:** Segurança Defensiva, Hardening e Mitigação de Riscos
* **Metas de Prática & Portfólio:**
  * [ ] Documentar boas práticas de hardening para servidores Linux/Windows.
  * [ ] Praticar e documentar configuração de regras defensivas com Firewall (UFW / iptables) e sistemas de detecção/prevenção (IDS/IPS / Fail2Ban / Snort).
  * [ ] Montar checklist defensivo para mitigação de vulnerabilidades comuns.
* **Entregáveis da Semana:**
  - `docs/hardening-e-regras-defensivas.md`
  - Exemplos de regras de firewall comentadas.

---

### Semana 7: 08/12 a 14/12 — GuardAI (Início)
* **Carga Horária Estimada:** ~5 horas
* **Módulo do Curso / Projeto:** Desenvolvimento do Projeto GuardAI
* **Metas de Prática & Portfólio:**
  * [ ] Iniciar a arquitetura e documentação do **GuardAI**.
  * [ ] Subir estrutura de arquivos iniciais e definir o escopo da aplicação.
  * [ ] Mapear matriz de ameaças específicas para modelos de IA (ex: prompt injection, jailbreaks, data poisoning).
* **Entregáveis da Semana:**
  - Diretório `projetos/guard-ai/` inicializado.
  - Modelagem de ameaças e arquitetura do GuardAI.

---

### Semana 8: 15/12 a 20/12 — GuardAI (Finalização) & Emissão do Certificado
* **Carga Horária Estimada:** ~5 horas
* **Módulo do Curso / Projeto:** Conclusão, Revisão Geral e Certificação
* **Metas de Prática & Portfólio:**
  * [ ] Finalizar o código e a documentação técnica do **GuardAI**.
  * [ ] Concluir todas as etapas pendentes na plataforma DIO e **emitir o certificado oficial**.
  * [ ] Revisão geral do portfólio no GitHub (README principal, tags, badges, licença open-source, links funcionais).
  * [ ] Publicar post de conclusão no LinkedIn conectando os write-ups do repositório.
* **Entregáveis da Semana:**
  - Projeto GuardAI finalizado e testado.
  - Certificado emitido e anexado ao repositório.
  - Repositório polido e pronto para recrutadores.
