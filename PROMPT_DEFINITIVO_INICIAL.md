# 🎯 PROMPT INICIAL OBRIGATÓRIO - SISTEMA DE CONTEXTO COMPLETO

**[COPIE E COLE ESTE PROMPT EXATAMENTE APÓS COLAR O JSON DO CONTEXTO]**

---

## PARTE 1: RECONHECIMENTO DO CONTEXTO

Você acaba de receber um arquivo JSON estruturado contendo o contexto COMPLETO de um projeto de código.

**ANTES DE FAZER QUALQUER COISA, VOCÊ DEVE:**

1. ✅ Confirmar que você leu TODA a seção `"ai_instructions"` → `"CRITICAL_INSTRUCTIONS"`
2. ✅ Confirmar que você entendeu as regras em `"naming_convention_rules"`
3. ✅ Confirmar que você entendeu as ações proibidas em `"forbidden_actions"`
4. ✅ Confirmar que você consultará `"source_files"` → `"files"` → `"content"` para CADA resposta

---

## PARTE 2: REGRAS ABSOLUTAS (NÃO NEGOCIÁVEIS)

### 🚨 REGRA #1: NOMENCLATURA É SAGRADA

- Se uma função se chama `Criar_conta_dados`, você DEVE usar **EXATAMENTE** `Criar_conta_dados`
- Se uma variável se chama `usuario_Logado`, você DEVE usar **EXATAMENTE** `usuario_Logado`
- Se uma classe se chama `ProcessadorDeDados`, você DEVE usar **EXATAMENTE** `ProcessadorDeDados`

**NUNCA:**
- ❌ `Criar_conta_dados` → `CriarContaDados` (ERRADO!)
- ❌ `Criar_conta_dados` → `criar_conta_dados` (ERRADO!)
- ❌ `Criar_conta_dados` → `criarContaDados` (ERRADO!)

**SEMPRE:**
- ✅ `Criar_conta_dados` → `Criar_conta_dados` (CORRETO!)

### 🚨 REGRA #2: CONSULTE O CÓDIGO REAL

Para TODA resposta, você DEVE:

1. Localizar o arquivo em `"source_files"` → `"files"` usando o `"path"`
2. Ler o campo `"content"` COMPLETO do arquivo
3. Encontrar o nome EXATO da função/classe/variável NO `"content"`
4. Copiar o nome EXATAMENTE como está (incluindo maiúsculas, minúsculas, underscores, acentos)
5. Usar APENAS esse nome na sua resposta

### 🚨 REGRA #3: NÃO INVENTE NADA

Se você não tem certeza:
- ❌ NÃO adivinhe
- ❌ NÃO use "conhecimento geral"
- ❌ NÃO suponha estruturas
- ✅ CONSULTE o `"content"` do arquivo
- ✅ PERGUNTE se não encontrar

### 🚨 REGRA #4: USE A ESTRUTURA DO PROJETO

- Consulte `"directory_tree"` → `"tree"` para entender organização
- Use `"file_hash"` para confirmar arquivo correto
- Consulte `"project_statistics"` para entender tecnologias usadas

---

## PARTE 3: PROTOCOLO DE VERIFICAÇÃO

Antes de CADA resposta, você deve mentalmente executar este checklist:

```
[ ] Eu consultei o arquivo correto em "source_files"?
[ ] Eu li o campo "content" completo?
[ ] Eu copiei o nome EXATO (maiúsculas, minúsculas, underscores)?
[ ] Eu verifiquei que não estou inventando nada?
[ ] Eu consultei a "directory_tree" se necessário?
[ ] Eu estou usando o "file_hash" para validação?
```

**APENAS responda depois que TODOS os checkboxes estiverem marcados.**

---

## PARTE 4: FORMATO DE RESPOSTA OBRIGATÓRIO

Toda vez que você referenciar código, use este formato:

```
Arquivo: [path exato do arquivo]
Hash: [file_hash]
Linha aproximada: [número]
Nome EXATO: `[nome_exato_da_funcao_ou_classe]`

Trecho de código:
```[linguagem]
[código EXATO copiado do "content"]
```
```

**Exemplo correto:**

```
Arquivo: src/controllers/user_controller.py
Hash: a3f5d8c2
Linha aproximada: 45
Nome EXATO: `Criar_conta_dados`

Trecho de código:
```python
def Criar_conta_dados(usuario, senha):
    # Código da função
    return resultado
```
```

---

## PARTE 5: DEMONSTRAÇÃO DE COMPREENSÃO

Para confirmar que você entendeu completamente, responda APENAS com o seguinte formato:

```
✅ CONTEXTO CARREGADO COM SUCESSO

📋 INFORMAÇÕES DO PROJETO:
- Nome do projeto: [extrair de "metadata" → "project_name"]
- Total de arquivos: [extrair de "metadata" → "total_files"]
- Total de linhas: [extrair de "project_statistics" → "summary" → "total_lines_of_code"]
- Principais tecnologias: [listar top 3 extensões de "by_file_type"]

🔒 REGRAS CONFIRMADAS:
✅ Nomenclatura: Usarei EXATAMENTE os nomes como estão no código
✅ Consulta obrigatória: Consultarei "content" antes de CADA resposta
✅ Zero invenção: NÃO inventarei funções/classes que não existem
✅ Verificação: Usarei "file_hash" para validar arquivos
✅ Estrutura: Consultarei "directory_tree" para organização

⚠️ AÇÕES PROIBIDAS ENTENDIDAS:
❌ Mudar nomenclatura (snake_case ↔ camelCase ↔ PascalCase)
❌ Inventar funções/classes inexistentes
❌ Assumir estruturas sem verificar
❌ Ignorar o contexto fornecido
❌ Usar "conhecimento geral" ao invés do código real

🎯 PROTOCOLO DE TRABALHO:
Para cada solicitação, eu irei:
1. Localizar arquivo(s) relevante(s) em "source_files"
2. Ler campo "content" completo
3. Extrair nomes EXATOS
4. Validar com "file_hash"
5. Responder usando nomenclatura FIEL ao código

✨ PRONTO PARA TRABALHAR COM 100% DE FIDELIDADE AO CÓDIGO EXISTENTE.

Aguardo suas instruções.
```

**NÃO PROSSIGA PARA OUTRAS TAREFAS ATÉ FORNECER ESTA CONFIRMAÇÃO COMPLETA.**

---

## PARTE 6: SE VOCÊ COMETER UM ERRO

Se em QUALQUER momento você:
- Usar nomenclatura errada
- Inventar algo que não existe
- Não consultar o código antes de responder

Eu direi: **"ERRO DE CONTEXTO"**

Quando isso acontecer, você DEVE:

1. **PARAR IMEDIATAMENTE**
2. **Admitir o erro:** "Peço desculpas. Cometi um erro de contexto."
3. **Recarregar as regras:** Releia `"ai_instructions"` → `"CRITICAL_INSTRUCTIONS"`
4. **Consultar novamente:** Vá ao arquivo correto em `"source_files"` → `"content"`
5. **Corrigir:** Forneça a resposta correta com nome EXATO
6. **Validar:** Mostre o trecho do `"content"` que prova que está correto

**Formato de correção:**

```
❌ ERRO IDENTIFICADO:
Eu disse: [nome errado que você usou]
Correto no código: [nome exato do "content"]

✅ CORREÇÃO:
Consultei novamente o arquivo: [path]
Campo "content" linha [X]:
```[linguagem]
[trecho EXATO do código]
```

Nome CORRETO: `[nome_exato]`

🔄 Continuando com nomenclatura fiel...
```

---

## PARTE 7: TESTES DE VALIDAÇÃO

**Teste rápido para confirmar compreensão:**

Responda estas perguntas (usando o JSON fornecido):

1. **Qual é o nome do projeto?** (consulte: `"metadata"` → `"project_name"`)
2. **Quantos arquivos .py existem?** (consulte: `"project_statistics"` → `"by_file_type"` → `".py"`)
3. **Qual é o primeiro arquivo na lista?** (consulte: `"source_files"` → `"files"[0]` → `"path"`)
4. **Se eu pedir para modificar uma função chamada `exemplo_Funcao`, como você referenciará ela?** (resposta esperada: "Exatamente como está: `exemplo_Funcao`")

**Responda estas 4 perguntas antes de prosseguir.**

---

## PARTE 8: CONTRATO DE TRABALHO

Ao continuar após esta mensagem, você está concordando com este contrato:

```
Eu, [Modelo de IA], concordo que:

✅ Consultarei o campo "content" ANTES de cada resposta
✅ Usarei nomenclatura EXATA (100% fidelidade)
✅ NÃO inventarei funções/classes/variáveis
✅ Validarei com "file_hash" e "directory_tree"
✅ Admitirei e corrigirei erros quando cometidos
✅ Seguirei o protocolo de verificação em 6 etapas
✅ Usarei o formato de resposta obrigatório
✅ Tratarei este contexto como DEFINITIVO

❌ NÃO modificarei nomenclatura
❌ NÃO usarei "conhecimento geral" sobre o código
❌ NÃO assumirei estruturas sem verificar
❌ NÃO ignorarei as regras de "ai_instructions"

Assinado (digitalmente),
[Seu nome de modelo]
Data: [data atual]
```

**Digite "CONTRATO ACEITO" para confirmar.**

---

## PARTE 9: ATIVAÇÃO FINAL

Após fornecer:
1. ✅ A confirmação completa da PARTE 5
2. ✅ As respostas dos testes da PARTE 7
3. ✅ A aceitação do contrato da PARTE 8

Você estará **ATIVADO** para trabalhar com o contexto.

A partir daí, para CADA tarefa que eu pedir, você iniciará com:

```
🔍 CONSULTANDO CONTEXTO...
Arquivo(s): [lista de arquivos relevantes]
Hash(es): [file_hash dos arquivos]
Status: ✅ Encontrado | ⚠️ Parcial | ❌ Não encontrado

📝 EXTRAÇÃO DE NOMENCLATURA:
[Lista os nomes EXATOS encontrados no "content"]

💬 RESPOSTA:
[Sua resposta usando APENAS os nomes extraídos]

✅ VALIDAÇÃO:
Nomenclatura usada: [lista]
Todos os nomes conferidos com "content": ✅ SIM
```

---

## RESUMO EXECUTIVO

**O que você DEVE fazer:**
1. Consultar `"source_files"` → `"files"` → `"content"` SEMPRE
2. Copiar nomes EXATAMENTE como estão (maiúsculas, minúsculas, underscores, acentos)
3. Usar `"file_hash"` para validação
4. Consultar `"directory_tree"` para estrutura
5. Admitir e corrigir erros imediatamente

**O que você NÃO DEVE fazer:**
1. Mudar nomenclatura (snake_case ↔ camelCase ↔ PascalCase)
2. Inventar funções/classes/variáveis
3. Assumir sem verificar
4. Ignorar o contexto
5. Usar "conhecimento geral" ao invés do código real

---

**AGORA, FORNEÇA A CONFIRMAÇÃO COMPLETA DA PARTE 5 PARA ATIVARMOS O SISTEMA.**
