#!/usr/bin/env python3
"""
Script Definitivo de Extração de Contexto para IA
Versão 3.0 - MÁXIMA PROTEÇÃO CONTRA ALUCINAÇÕES

Características:
- Instruções ultra-detalhadas para a IA
- Sistema de validação de nomenclatura
- Exemplos de uso correto e incorreto
- Protocolo de verificação em múltiplas etapas
- Formatação otimizada para GPT-4, Claude, Gemini, etc
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog

# ==================== CONFIGURAÇÕES ====================

EXTENSOES_PERMITIDAS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.vue', '.svelte',
    '.rb', '.java', '.go', '.rs', '.php', '.cs', '.kt', '.swift',
    '.c', '.cpp', '.h', '.hpp', '.css', '.scss', '.sass', '.less',
    '.html', '.xml', '.json', '.yaml', '.yml', '.toml', '.ini',
    '.sql', '.prisma', '.sh', '.bash', '.md', '.txt', '.dockerfile'
}

DIRETORIOS_IGNORADOS = {
    'node_modules', '.git', '__pycache__', 'venv', 'env', '.venv',
    'dist', 'build', 'target', '.next', '.nuxt', 'vendor',
    'coverage', '.pytest_cache', '.idea', '.vscode', 'tmp', 'temp'
}

ARQUIVOS_SEM_EXTENSAO = {
    'Dockerfile', 'Makefile', 'Rakefile', 'Gemfile', 'Procfile'
}

TAMANHO_MAXIMO_ARQUIVO = 2_000_000

# ==================== FUNÇÕES AUXILIARES ====================

def calcular_hash_arquivo(caminho):
    try:
        sha256 = hashlib.sha256()
        with open(caminho, 'rb') as f:
            for bloco in iter(lambda: f.read(4096), b''):
                sha256.update(bloco)
        return sha256.hexdigest()[:16]
    except:
        return "unknown"

def deve_processar_arquivo(caminho):
    try:
        tamanho = os.path.getsize(caminho)
        if tamanho > TAMANHO_MAXIMO_ARQUIVO:
            return False
        extensao = Path(caminho).suffix.lower()
        if extensao in EXTENSOES_PERMITIDAS:
            return True
        nome = Path(caminho).name
        if nome in ARQUIVOS_SEM_EXTENSAO:
            return True
        return False
    except:
        return False

def construir_arvore_diretorios(caminho_raiz, arquivos_processados):
    arvore = {}
    for _, caminho_rel in arquivos_processados:
        partes = caminho_rel.parts
        nivel_atual = arvore
        for parte in partes[:-1]:
            if parte not in nivel_atual:
                nivel_atual[parte] = {}
            nivel_atual = nivel_atual[parte]
        if '__files__' not in nivel_atual:
            nivel_atual['__files__'] = []
        nivel_atual['__files__'].append(partes[-1])
    return arvore

def arvore_para_texto(arvore, prefixo="", eh_ultimo=True):
    linhas = []
    items = sorted([(k, v) for k, v in arvore.items() if k != '__files__'])
    arquivos = arvore.get('__files__', [])

    for idx, (nome, sub_arvore) in enumerate(items):
        eh_ultimo_dir = (idx == len(items) - 1 and not arquivos)
        conector = "└── " if eh_ultimo_dir else "├── "
        linhas.append(f"{prefixo}{conector}{nome}/")
        extensao = "    " if eh_ultimo_dir else "│   "
        linhas.extend(arvore_para_texto(sub_arvore, prefixo + extensao, eh_ultimo_dir))

    for idx, arquivo in enumerate(sorted(arquivos)):
        eh_ultimo_arq = (idx == len(arquivos) - 1)
        conector = "└── " if eh_ultimo_arq else "├── "
        linhas.append(f"{prefixo}{conector}{arquivo}")

    return linhas

def coletar_estatisticas(arquivos_processados):
    stats = {
        'total_arquivos': len(arquivos_processados),
        'total_linhas': 0,
        'total_caracteres': 0,
        'por_extensao': defaultdict(lambda: {'count': 0, 'lines': 0}),
        'arquivos_maiores': []
    }

    tamanhos = []

    for caminho_completo, caminho_rel in arquivos_processados:
        try:
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                linhas = conteudo.count('\n') + 1
                caracteres = len(conteudo)
                stats['total_linhas'] += linhas
                stats['total_caracteres'] += caracteres
                extensao = Path(caminho_completo).suffix or 'sem_extensao'
                stats['por_extensao'][extensao]['count'] += 1
                stats['por_extensao'][extensao]['lines'] += linhas
                tamanhos.append((str(caminho_rel), linhas, caracteres))
        except:
            pass

    tamanhos.sort(key=lambda x: x[2], reverse=True)
    stats['arquivos_maiores'] = [
        {'path': path, 'lines': lines, 'chars': chars}
        for path, lines, chars in tamanhos[:10]
    ]

    return stats

def gerar_instrucoes_ia_ultra_detalhadas():
    """Gera instruções EXTREMAMENTE detalhadas para a IA"""
    return {
        "CRITICAL_INSTRUCTIONS": {
            "_readme_first": "LEIA ESTA SEÇÃO COMPLETA ANTES DE PROCESSAR QUALQUER CÓDIGO",

            "purpose": {
                "description": "Este arquivo contém o contexto COMPLETO e DEFINITIVO do projeto",
                "your_role": "Você é um assistente de código que deve manter 100% de fidelidade ao código fornecido",
                "success_criteria": "Sucesso = usar nomenclatura EXATA + consultar 'content' antes de cada resposta"
            },

            "naming_convention_rules": {
                "_importance": "REGRA #1 - MAIS IMPORTANTE - NUNCA VIOLE ISTO",

                "absolute_rules": [
                    "NUNCA, EM HIPÓTESE ALGUMA, modifique nomes de funções, classes ou variáveis",
                    "Se o código tem 'Criar_conta_dados', use EXATAMENTE 'Criar_conta_dados'",
                    "Se o código tem 'usuarioLogado', use EXATAMENTE 'usuarioLogado'",
                    "Se o código tem 'ProcessadorDeDados', use EXATAMENTE 'ProcessadorDeDados'",
                    "Mantenha TODOS os caracteres: maiúsculas, minúsculas, underscores, acentos, números",
                    "NÃO converta entre snake_case ↔ camelCase ↔ PascalCase ↔ kebab-case"
                ],

                "examples_of_correct_behavior": {
                    "example_1": {
                        "code_has": "Criar_conta_dados",
                        "you_must_use": "Criar_conta_dados",
                        "forbidden": ["CriarContaDados", "criar_conta_dados", "criarContaDados", "criar-conta-dados"]
                    },
                    "example_2": {
                        "code_has": "usuario_Logado",
                        "you_must_use": "usuario_Logado",
                        "forbidden": ["usuarioLogado", "usuario_logado", "UsuarioLogado", "USUARIO_LOGADO"]
                    },
                    "example_3": {
                        "code_has": "ProcessaDados123",
                        "you_must_use": "ProcessaDados123",
                        "forbidden": ["processaDados123", "processa_dados_123", "PROCESSA_DADOS_123"]
                    }
                },

                "verification_protocol": {
                    "step_1": "Localizar arquivo em 'source_files' pelo 'path'",
                    "step_2": "Ler campo 'content' COMPLETO",
                    "step_3": "Procurar o identificador (função/classe/variável)",
                    "step_4": "Copiar nome EXATO (Ctrl+C, Ctrl+V mental)",
                    "step_5": "Usar APENAS esse nome na resposta",
                    "step_6": "Validar com 'file_hash' se necessário"
                }
            },

            "context_usage_rules": {
                "_importance": "REGRA #2 - SEMPRE CONSULTE O CONTEXTO",

                "mandatory_actions": [
                    "SEMPRE consulte 'source_files' → 'files' → 'content' antes de responder",
                    "NUNCA confie em 'conhecimento geral' sobre o projeto",
                    "SEMPRE use 'directory_tree' para entender estrutura de pastas",
                    "SEMPRE use 'file_hash' para confirmar que está no arquivo correto",
                    "SEMPRE use 'project_statistics' para entender escala e tecnologias"
                ],

                "how_to_find_information": {
                    "to_find_function_name": "source_files → files → [localizar por path] → content → [procurar função]",
                    "to_find_class_name": "source_files → files → [localizar por path] → content → [procurar classe]",
                    "to_find_variable_name": "source_files → files → [localizar por path] → content → [procurar variável]",
                    "to_find_file_location": "directory_tree → tree → [visualizar estrutura]",
                    "to_confirm_correct_file": "source_files → files → [arquivo] → file_hash → [comparar]"
                },

                "response_template": {
                    "always_start_with": "Consultando 'source_files' → 'files' → 'content'...",
                    "then_state": "Arquivo: [path exato] (hash: [file_hash])",
                    "then_extract": "Nomes EXATOS encontrados: [`nome1`], [`nome2`]",
                    "then_respond": "[Sua resposta usando APENAS os nomes extraídos]",
                    "finally_validate": "✅ Nomenclatura fiel ao 'content' confirmada"
                }
            },

            "forbidden_actions": {
                "_importance": "REGRA #3 - NUNCA FAÇA ISTO",

                "never_do_this": [
                    "❌ NÃO invente nomes de funções/classes/variáveis que não existem no 'content'",
                    "❌ NÃO mude snake_case para camelCase ou vice-versa",
                    "❌ NÃO mude PascalCase para snake_case ou vice-versa",
                    "❌ NÃO adicione ou remova underscores dos nomes",
                    "❌ NÃO mude maiúsculas para minúsculas ou vice-versa",
                    "❌ NÃO assuma estruturas de código sem verificar no 'content'",
                    "❌ NÃO use 'conhecimento geral' ao invés do código real",
                    "❌ NÃO ignore o 'content' em favor de 'boas práticas'",
                    "❌ NÃO sugira refatorações de nomenclatura sem permissão explícita",
                    "❌ NÃO crie variações dos nomes ('user' se o código usa 'usuario')"
                ],

                "consequences_of_violation": {
                    "what_happens": "Se você violar estas regras, o código não funcionará",
                    "example": "Se você usar 'criarConta' mas o código tem 'Criar_conta', Python dará NameError",
                    "severity": "CRÍTICO - Pode quebrar toda a aplicação",
                    "recovery": "Se violar, ADMITA o erro e CORRIJA consultando 'content' novamente"
                }
            },

            "verification_checklist": {
                "_importance": "REGRA #4 - EXECUTE ANTES DE CADA RESPOSTA",

                "before_every_response": {
                    "check_1": "☐ Localizei o arquivo correto em 'source_files' usando 'path'?",
                    "check_2": "☐ Li o campo 'content' COMPLETO (não apenas parte)?",
                    "check_3": "☐ Encontrei o identificador EXATO no 'content'?",
                    "check_4": "☐ Copiei o nome EXATAMENTE como está (maiúsculas, underscores, etc)?",
                    "check_5": "☐ Confirmei o 'file_hash' se necessário?",
                    "check_6": "☐ NÃO estou inventando ou modificando nada?",
                    "check_7": "☐ Minha resposta usa APENAS nomes do 'content'?",
                    "check_8": "☐ Posso provar tudo citando trechos do 'content'?"
                },

                "only_respond_when": "TODOS os checkboxes acima estiverem marcados (☑)",

                "if_unsure": {
                    "dont": "NÃO adivinhe ou assuma",
                    "do": "PERGUNTE ao usuário ou DIGA que não encontrou no 'content'"
                }
            },

            "response_format": {
                "_importance": "REGRA #5 - SEMPRE USE ESTE FORMATO",

                "structure": {
                    "section_1_consultation": {
                        "label": "🔍 CONSULTA AO CONTEXTO",
                        "content": [
                            "Arquivo(s) consultado(s): [path(s)]",
                            "Hash(es): [file_hash(es)]",
                            "Campo 'content' lido: ✅",
                            "Total de linhas lidas: [número]"
                        ]
                    },
                    "section_2_extraction": {
                        "label": "📝 EXTRAÇÃO DE NOMENCLATURA",
                        "content": [
                            "Nomes EXATOS encontrados:",
                            "- Função: `[nome_exato_1]`",
                            "- Classe: `[NomeExato_2]`",
                            "- Variável: `[variavel_exata_3]`"
                        ]
                    },
                    "section_3_response": {
                        "label": "💬 RESPOSTA",
                        "content": "[Sua resposta usando APENAS os nomes extraídos acima]"
                    },
                    "section_4_validation": {
                        "label": "✅ VALIDAÇÃO",
                        "content": [
                            "Evidência do 'content':",
                            "```[linguagem]",
                            "[trecho EXATO do código]",
                            "```",
                            "Fidelidade de nomenclatura: 100% ✅"
                        ]
                    }
                },

                "minimal_format_if_simple_question": {
                    "acceptable": "Consultar 'content' → Extrair nome EXATO → Responder brevemente",
                    "but_always": "SEMPRE mencione de onde extraiu a informação (path + hash)"
                }
            },

            "error_recovery_protocol": {
                "_when_to_use": "Se você cometer erro de nomenclatura, execute IMEDIATAMENTE",

                "steps": {
                    "step_1_admit": "Diga: 'Cometi um erro. Vou corrigir consultando o código original.'",
                    "step_2_identify": "Liste: 'Eu disse: [nome_errado] | Deveria ser: [procurando...]'",
                    "step_3_consult": "Vá para: 'source_files' → 'files' → [path] → 'content'",
                    "step_4_extract": "Procure e copie: nome EXATO do 'content'",
                    "step_5_prove": "Cole trecho do 'content' mostrando o nome correto",
                    "step_6_correct": "Diga: 'Nome CORRETO: `[nome_exato]`'",
                    "step_7_redo": "Refaça a resposta usando o nome correto",
                    "step_8_commit": "Diga: 'Consultarei o content antes de cada menção daqui em diante'"
                },

                "example_of_correction": {
                    "wrong_response": "A função criarConta faz...",
                    "correction": {
                        "admit": "Cometi um erro. Vou corrigir.",
                        "identify": "Eu disse: criarConta | Consultando 'content'...",
                        "extract": "Encontrado em 'content' linha 42: def Criar_conta_dados(",
                        "prove": "```python\ndef Criar_conta_dados(usuario, senha):\n    ...\n```",
                        "correct": "Nome CORRETO: `Criar_conta_dados`",
                        "redo": "A função `Criar_conta_dados` faz...",
                        "commit": "Consultarei o 'content' antes de cada menção."
                    }
                }
            },

            "special_situations": {
                "if_function_not_found": {
                    "do_not": "NÃO invente que ela existe",
                    "instead": "Diga: 'Não encontrei [nome] no content do arquivo [path]. Pode verificar se o nome está correto ou se está em outro arquivo?'"
                },
                "if_multiple_files_have_same_name": {
                    "do": "Liste TODOS os arquivos onde aparece, com paths e hashes diferentes"
                },
                "if_name_is_ambiguous": {
                    "do": "Peça clarificação: 'Encontrei `[nome]` em [N] lugares. Qual você quer: [lista com paths]?'"
                },
                "if_user_wants_to_rename": {
                    "warn": "⚠️ Renomear afetará [N] arquivos. Listar todos antes de prosseguir?",
                    "require_confirmation": True
                }
            }
        }
    }

def extrair_conteudo_diretorio(caminho_raiz, arquivo_saida='contexto_ia_completo.json'):
    caminho_raiz = Path(caminho_raiz).resolve()

    if not caminho_raiz.exists():
        print(f"❌ Erro: O diretório '{caminho_raiz}' não existe!")
        return

    print(f"\n{'='*60}")
    print(f"🚀 EXTRATOR DE CONTEXTO PARA IA v3.0")
    print(f"{'='*60}\n")

    arquivos_processados = []
    arquivos_ignorados = 0

    print(f"📂 Escaneando: {caminho_raiz.name}")

    for root, dirs, files in os.walk(caminho_raiz):
        dirs[:] = [d for d in dirs if d not in DIRETORIOS_IGNORADOS]
        for file in files:
            caminho_completo = Path(root) / file
            if deve_processar_arquivo(caminho_completo):
                caminho_relativo = caminho_completo.relative_to(caminho_raiz)
                arquivos_processados.append((caminho_completo, caminho_relativo))
            else:
                arquivos_ignorados += 1

    arquivos_processados.sort(key=lambda x: str(x[1]))

    print(f"✅ {len(arquivos_processados)} arquivos para processar")
    print(f"⏭️  {arquivos_ignorados} arquivos ignorados\n")
    print("📊 Coletando estatísticas...")

    stats = coletar_estatisticas(arquivos_processados)
    arvore = construir_arvore_diretorios(caminho_raiz, arquivos_processados)
    arvore_texto = arvore_para_texto(arvore)

    print("📝 Processando arquivos...\n")

    lista_arquivos = []
    erros = []

    for idx, (caminho_completo, caminho_rel) in enumerate(arquivos_processados, 1):
        caminho_rel_str = str(caminho_rel).replace('\\', '/')
        progresso = (idx / len(arquivos_processados)) * 100
        print(f"\r[{progresso:5.1f}%] {caminho_rel_str[:50]:<50}", end='', flush=True)

        conteudo_arquivo = ""
        encoding_usado = "utf-8"

        try:
            with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
                conteudo_arquivo = arquivo.read()
        except UnicodeDecodeError:
            try:
                with open(caminho_completo, 'r', encoding='latin-1') as arquivo:
                    conteudo_arquivo = arquivo.read()
                    encoding_usado = "latin-1"
            except Exception as e:
                conteudo_arquivo = f"[ERRO: {str(e)}]"
                erros.append({'file': caminho_rel_str, 'error': str(e)})
                encoding_usado = "error"
        except Exception as e:
            conteudo_arquivo = f"[ERRO: {str(e)}]"
            erros.append({'file': caminho_rel_str, 'error': str(e)})
            encoding_usado = "error"

        num_linhas = conteudo_arquivo.count('\n') + 1 if conteudo_arquivo else 0
        hash_arquivo = calcular_hash_arquivo(caminho_completo)

        lista_arquivos.append({
            "file_id": f"file_{idx}",
            "path": caminho_rel_str,
            "extension": Path(caminho_completo).suffix or "none",
            "lines": num_linhas,
            "size_bytes": len(conteudo_arquivo.encode('utf-8')),
            "file_hash": hash_arquivo,
            "encoding": encoding_usado,
            "content": conteudo_arquivo,
            "_how_to_use": f"Para referenciar este arquivo: use path='{caminho_rel_str}' e valide com hash='{hash_arquivo}'"
        })

    print("\n\n🔧 Montando contexto ultra-detalhado...\n")

    contexto_completo = {
        "_LEIA_ISTO_PRIMEIRO": {
            "URGENTE": "Antes de processar qualquer código, leia a seção 'ai_instructions' → 'CRITICAL_INSTRUCTIONS' COMPLETA",
            "IMPORTANTE": "A nomenclatura no campo 'content' é DEFINITIVA. NÃO modifique nomes de funções/classes/variáveis",
            "OBRIGATORIO": "Consulte 'source_files' → 'files' → 'content' antes de CADA resposta",
            "PROIBIDO": "NÃO converta entre snake_case ↔ camelCase ↔ PascalCase",
            "VALIDACAO": "Use 'file_hash' para confirmar que está no arquivo correto"
        },

        "metadata": {
            "schema_version": "3.0",
            "generated_at": datetime.now().isoformat(),
            "extraction_tool": "AI Context Extractor v3.0 - Maximum Fidelity Edition",
            "project_name": caminho_raiz.name,
            "project_root": str(caminho_raiz),
            "total_files": len(arquivos_processados),
            "files_with_errors": len(erros),
            "warning": "Este contexto contém o código EXATO do projeto. Nomenclatura aqui é DEFINITIVA."
        },

        "ai_instructions": gerar_instrucoes_ia_ultra_detalhadas(),

        "project_statistics": {
            "summary": {
                "total_files": stats['total_arquivos'],
                "total_lines_of_code": stats['total_linhas'],
                "total_characters": stats['total_caracteres'],
                "estimated_tokens": stats['total_caracteres'] // 4
            },
            "by_file_type": dict(stats['por_extensao']),
            "largest_files": stats['arquivos_maiores']
        },

        "directory_tree": {
            "description": "Estrutura hierárquica REAL do projeto (não invente caminhos)",
            "tree": "\n".join([caminho_raiz.name + "/"] + arvore_texto),
            "usage": "Consulte ESTA árvore para entender onde os arquivos estão localizados"
        },

        "source_files": {
            "description": "Conteúdo COMPLETO de todos os arquivos do projeto",
            "critical_note": "Os nomes de funções/classes/variáveis aqui são DEFINITIVOS",
            "how_to_use": {
                "step_1": "Encontre o arquivo pelo campo 'path'",
                "step_2": "Valide com 'file_hash'",
                "step_3": "Leia o campo 'content' COMPLETO",
                "step_4": "Extraia os nomes EXATOS como estão no 'content'",
                "step_5": "Use APENAS esses nomes nas respostas"
            },
            "files": lista_arquivos
        }
    }

    if erros:
        contexto_completo["errors"] = {
            "description": "Arquivos com erro de leitura",
            "errors": erros
        }

    print(f"💾 Salvando: {arquivo_saida}")

    with open(arquivo_saida, 'w', encoding='utf-8') as saida:
        json.dump(contexto_completo, saida, indent=2, ensure_ascii=False)

    tamanho_kb = os.path.getsize(arquivo_saida) / 1024
    tamanho_mb = tamanho_kb / 1024

    print(f"\n{'='*60}")
    print(f"✅ EXTRAÇÃO CONCLUÍDA!")
    print(f"{'='*60}\n")
    print(f"📄 Arquivo: {arquivo_saida}")
    print(f"📊 Tamanho: {tamanho_mb:.2f} MB")
    print(f"📁 Arquivos: {len(arquivos_processados)}")
    print(f"📝 Linhas: {stats['total_linhas']:,}")
    print(f"🎯 Tokens: ~{stats['total_caracteres'] // 4:,}")

    if erros:
        print(f"\n⚠️  Erros: {len(erros)}")

    print(f"\n{'='*60}")
    print(f"📋 PRÓXIMOS PASSOS:")
    print(f"{'='*60}")
    print(f"1. Abra '{arquivo_saida}'")
    print(f"2. Copie TODO o conteúdo")
    print(f"3. Cole na IA")
    print(f"4. USE O PROMPT_DEFINITIVO_INICIAL.md")
    print(f"5. Aguarde confirmação da IA")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    print("\n🎯 Selecione o diretório do projeto...\n")

    caminho = filedialog.askdirectory(
        title="Selecione a pasta raiz do projeto",
        mustexist=True
    )

    if not caminho:
        print("❌ Cancelado.\n")
        sys.exit(1)

    nome_projeto = Path(caminho).name
    arquivo_saida = f"contexto_ia_{nome_projeto}.json"

    try:
        extrair_conteudo_diretorio(caminho, arquivo_saida)
    except Exception as e:
        print(f"\n❌ ERRO: {str(e)}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
