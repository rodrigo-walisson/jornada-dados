# Trilha de estudos: de Administração para Ciência de Dados

> Montada em 01/11/2026 a partir do teste de nivelamento (7/20).
> Ritmo: até 5h por semana, sem pressa. Duração estimada: cerca de 20 meses.

---

## Diagnóstico

| Área | Nota | O que o teste mostrou |
|---|---|---|
| Python | 1/4 | Base de sintaxe ainda não consolidada (listas, dicionários) |
| Estatística | 2/4 | Intuição boa (mediana, outliers); faltam inferência (p-valor) e probabilidade condicional (Bayes) |
| Matemática | 0/4 | Ponto de partida do zero: funções, derivadas, matrizes |
| SQL | 2/4 | Sabe filtrar e agregar; faltam JOINs e funções de janela |
| Machine learning | 2/4 | Conceitos gerais certos; faltam métricas (precisão/recall) e boas práticas de validação |

**Seu maior trunfo:** Excel avançado com Power Query e Power BI. Você já pensa em tabelas, mesclagens e agregações, e a lógica de SQL e pandas é a mesma. Além disso, você conhece processos de negócio por causa da Administração, coisa que muitos programadores não conhecem.

**Estratégia:** primeiro chegar a **Analista de Dados** (Fases 1 e 2), que é a vaga mais próxima do seu perfil e a porta de entrada mais comum. Depois, aprofundar em estatística, matemática e ML para **Ciência de Dados** (Fases 3 a 6). Você não precisa decidir o cargo agora: o Marco da Fase 2 é o momento de decidir.

---

## Rotina semanal (5h)

| Sessão | Duração | O que fazer |
|---|---|---|
| 1 | 1h30 | Leitura do livro da fase + digitar e rodar os exemplos |
| 2 | 1h30 | Exercícios do capítulo (não pule: é onde o aprendizado acontece) |
| 3 | 2h | Projeto da fase |

Regras de ouro:
- Todo código vai para o **GitHub**, mesmo o que estiver feio. O histórico de commits mostra constância.
- Ficou travado mais de 30 minutos? Anote a dúvida e siga. Volte depois ou pergunte.
- Ao fim de cada capítulo, escreva 3 linhas com o que aprendeu em um arquivo de notas.

---

## Fase 0: Preparação do ambiente (2 semanas)

- [ ] Instalar Python (via Anaconda ou Miniconda) e VS Code com a extensão Jupyter
- [ ] Criar conta no GitHub e aprender o básico: `clone`, `add`, `commit`, `push`
- [ ] Criar um repositório `jornada-dados` para guardar tudo desta trilha

---

## Fase 1: Python do zero (≈ 3 meses)

**Objetivo:** escrever scripts simples com segurança: variáveis, listas, dicionários, laços, funções e leitura de arquivos.

**Livro principal**
- 📘 *Automatize tarefas maçantes com Python*, de Al Sweigart (Novatec). A versão em inglês, *Automate the Boring Stuff with Python*, é gratuita em automatetheboringstuff.com.
  - Parte I inteira (caps. 1 a 9)
  - Da Parte II, os capítulos de arquivos, Excel e CSV

**Projeto 1: Automação de relatório**
Pegue uma tarefa repetitiva de planilha do seu dia a dia (ou de um estágio, ou um caso inventado) e automatize com Python: ler várias planilhas, consolidar, calcular totais e gerar um arquivo final.
- [ ] Script funcionando
- [ ] README explicando o problema, a solução e quanto tempo isso economiza

> ✅ Teste de saída: refaça as questões 1 e 2 do nivelamento e explique cada linha.

---

## Fase 2: SQL e análise de dados (≈ 4 meses)

**Objetivo:** consultar bancos com SQL (JOINs, GROUP BY, HAVING, funções de janela) e analisar dados com pandas.

**Livros**
- 📘 *SQL para Análise de Dados*, de Cathy Tanimura (Novatec). Caps. 1 a 4 primeiro; o restante como consulta.
- 📘 *Python para Análise de Dados*, de Wes McKinney (Novatec). A 3ª edição em inglês é gratuita em wesmckinney.com/book. Caps. 4 a 10.
- 📗 Leitura de apoio: *Storytelling com Dados*, de Cole Nussbaumer Knaflic (Alta Books). Vai deixar seus dashboards de Power BI muito melhores.

**Dica:** o **LEFT JOIN** que você errou é exatamente a "Mesclar consultas → Externa esquerda" do Power Query. Faça a mesma mesclagem nos dois e compare os resultados.

**Projeto 2: Análise do e-commerce brasileiro (Olist)**
Dataset público do Kaggle: *Brazilian E-Commerce Public Dataset by Olist* (cerca de 100 mil pedidos reais).
- [ ] Carregar os CSVs em um banco SQLite e responder 10 perguntas de negócio em SQL (ex.: faturamento por estado, categorias com mais atraso, último pedido de cada cliente usando `ROW_NUMBER`)
- [ ] Repetir parte da análise em pandas
- [ ] Construir um dashboard no Power BI com os resultados
- [ ] README em formato de relatório: pergunta → análise → recomendação

> 🚩 **Marco:** com este projeto mais seu Power BI, você já tem perfil para vagas de **Analista de Dados Júnior**. Momento de decidir: seguir estudando enquanto busca a vaga de analista, ou focar direto em Ciência de Dados. As duas opções são válidas, e a experiência como analista acelera muito o resto.

---

## Fase 3: Estatística (≈ 3 meses)

**Objetivo:** entender distribuições, amostragem, intervalos de confiança, testes de hipótese (p-valor) e probabilidade condicional.

**Livros**
- 📘 *Use a Cabeça! Estatística*, de Dawn Griffiths (Alta Books). Para construir intuição: é leve e visual.
- 📘 *Estatística Prática para Cientistas de Dados*, de Peter Bruce, Andrew Bruce e Peter Gedeck (Alta Books). Caps. 1 a 3, com o código em Python.
- 📗 Leitura de lazer: *Como Mentir com Estatística*, de Darrell Huff.

**Pontos que o teste mostrou para reforçar**
- p-valor: o que ele **não** diz (não é a probabilidade da hipótese ser verdadeira)
- Teorema de Bayes: refaça a questão 8 com uma tabela de 1.000 pessoas. Fica intuitivo.

**Projeto 3: O atraso na entrega derruba a nota?**
Usando o dataset da Olist: compare as notas de avaliação de pedidos entregues no prazo e com atraso.
- [ ] Análise descritiva e gráficos
- [ ] Teste de hipótese e intervalo de confiança
- [ ] Conclusão escrita para um gestor, sem jargão

---

## Fase 4: Matemática para dados (≈ 3 meses, sem pressa)

**Objetivo:** perder o medo da matemática. Funções, derivadas (a ideia de "taxa de variação"), vetores e matrizes.

**Materiais** (aqui vídeos funcionam melhor que livros para começar)
- 🎥 Khan Academy em português: funções, álgebra e introdução a derivadas
- 🎥 3Blue1Brown: séries *Essência da Álgebra Linear* e *Essência do Cálculo* (com legendas em português)
- 📘 *Essential Math for Data Science*, de Thomas Nield (O'Reilly, em inglês). É a ponte entre a matemática e o código.

**Projeto 4: Regressão linear do zero**
- [ ] Implementar regressão linear com **gradiente descendente** usando só NumPy
- [ ] Plotar a reta sendo ajustada a cada iteração
- [ ] Comparar com o resultado do scikit-learn

> ✅ Teste de saída: refaça as questões 9 a 12 do nivelamento.

---

## Fase 5: Machine learning (≈ 4 meses)

**Objetivo:** treinar, validar e avaliar modelos supervisionados corretamente.

**Livros**
- 📘 *Mãos à Obra: Aprendizado de Máquina com Scikit-Learn, Keras & TensorFlow*, de Aurélien Géron (Alta Books). Parte I (caps. 1 a 9). Pule a parte de redes neurais por enquanto.
- 📗 Consulta: *An Introduction to Statistical Learning with Python* (ISLP), gratuito em statlearning.com. Para entender a teoria por trás.

**Pontos que o teste mostrou para reforçar**
- Dados desbalanceados: precisão, recall, F1, matriz de confusão (questão 19)
- Data leakage: sempre separe treino e teste **antes** de qualquer transformação e use `Pipeline` (questão 20)

**Projeto 5: Previsão de cancelamento de clientes (churn)**
Dataset do Kaggle: *Telco Customer Churn*.
- [ ] EDA, tratamento de dados e engenharia de variáveis
- [ ] Comparar pelo menos 3 modelos com validação cruzada, dentro de um `Pipeline`
- [ ] Escolher a métrica certa para o negócio e justificar
- [ ] Traduzir o resultado em decisão: "quais clientes a equipe de retenção deve ligar primeiro, e quanto isso economiza"

---

## Fase 6: Projeto final e portfólio (≈ 3 meses)

**Projeto 6: Ponta a ponta com um problema de negócio**
Escolha um problema da área de Administração que você conheça (previsão de demanda, inadimplência, rotatividade de funcionários, precificação…).
- [ ] Definir o problema e a métrica de sucesso
- [ ] Coletar e tratar os dados
- [ ] Modelar e avaliar
- [ ] Publicar um app simples com **Streamlit** onde dê para testar o modelo
- [ ] Escrever um artigo (LinkedIn ou Medium) contando o projeto

**Portfólio final**
- [ ] GitHub organizado com os 6 projetos e READMEs claros
- [ ] Perfil do LinkedIn reposicionado: "Administração + Dados"
- [ ] Refazer o teste de nivelamento completo

---

## Linha do tempo resumida

| Fase | Tema | Duração | Acumulado |
|---|---|---|---|
| 0 | Ambiente | 2 sem | 0,5 mês |
| 1 | Python | 3 meses | 3,5 meses |
| 2 | SQL + pandas → **pronto para Analista Jr.** | 4 meses | 7,5 meses |
| 3 | Estatística | 3 meses | 10,5 meses |
| 4 | Matemática | 3 meses | 13,5 meses |
| 5 | Machine learning | 4 meses | 17,5 meses |
| 6 | Projeto final | 3 meses | ≈ 20 meses |

Se em algum momento você conseguir mais horas por semana, as fases encurtam proporcionalmente. Os projetos não devem ser cortados: eles são o que te contrata.
