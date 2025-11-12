# Projeto GS Python — Provenn  

**Integrantes:**  
- Lucas Mesquita Massoni – RM561686  
- Felipe Balbino Murad – RM562347  

---

## 1. Descrição do Problema  

O avanço tecnológico trouxe novas formas de trabalho e de recrutamento, mas muitas **micro e pequenas empresas** ainda enfrentam dificuldades para divulgar vagas e encontrar profissionais qualificados.  
Da mesma forma, **muitos candidatos** não encontram plataformas acessíveis para se conectar com empresas que realmente precisam de mão de obra.  
Essa desconexão afeta diretamente a economia e limita o acesso a oportunidades de emprego.  

---

## 2. Proposta de Solução  

O **Provenn** é um sistema desenvolvido em Python que conecta **empresas contratantes** e **candidatos em busca de emprego**.  
A solução oferece uma plataforma simples, baseada em menus interativos no terminal, que permite:  

- Que empresas se cadastrem, façam login e acessem uma lista de candidatos.  
- Que candidatos se cadastrem, façam login e se candidatem às empresas disponíveis.  

O sistema utiliza arquivos **JSON** para armazenar dados permanentemente, dispensando bancos de dados externos e facilitando a manipulação local.  

---

## 3. Diferenciais da Solução  

- **Login seguro** com validação de e-mail e senha.  
- **Menu dinâmico**, adaptado conforme o tipo de usuário (empresa ou candidato).  
- **Validação completa** de campos e prevenção de duplicidade de e-mails.  
- **Estrutura modular**, separando funções de cadastro, login e fluxo principal.  
- **Persistência de dados** via JSON.  
- **Interface limpa e intuitiva** feita apenas com menus de texto.  

---

## 4. Estrutura do Projeto  

### Arquivos principais  
- `GS.py` → código principal do sistema.  
- `empresas.json` → lista de empresas cadastradas.  
- `candidatos.json` → lista de candidatos cadastrados.  

### Funções principais em `GS.py`  
- `tela_login()` → controla login e criação de conta.  
- `menu_principal(tipo_usuario)` → mostra opções específicas conforme o tipo de conta.  
- `cadastrar_candidato()` e `cadastrar_empresa()` → realizam cadastros com validações.  
- `verificar_login()` → autentica usuários com base nos arquivos JSON.  
- `fluxo_candidato()` → exibe empresas e permite candidatura.  
- `fluxo_empresa()` → exibe candidatos e permite envio de propostas.  
- `carregar_dados()` e `salvar_dados()` → manipulam dados dos arquivos JSON.  

---

## 5. Requisitos Atendidos  

O projeto cumpre todos os requisitos definidos no documento **GS - Python**:  
- Estrutura de **menu principal** com todas as funcionalidades do sistema.  
- **Validação** e tratamento de erros com `try/except`.  
- Uso de **funções com parâmetros e retorno**.  
- Aplicação de **estruturas de decisão e repetição** (`if`, `while`).  
- Uso de **listas e dicionários** como base de dados.  
- Manipulação de **arquivos JSON** para leitura e gravação.  
- Interface funcional e **usabilidade adequada ao usuário final**.  

---

## 6. Funcionamento  

1. O sistema inicia exibindo o **menu de login**.  
2. O usuário pode **fazer login** ou **criar uma nova conta**.  
3. Após o login, o sistema identifica o tipo de usuário e exibe apenas as opções correspondentes:  
   - **Candidato:** pode ver empresas e se candidatar.  
   - **Empresa:** pode ver candidatos e enviar propostas.  
4. O sistema salva automaticamente novos cadastros ou alterações nos arquivos `.json`.  

---

## 7. Como Executar  

1. Verifique se o **Python 3** está instalado no seu computador.  
2. Coloque os arquivos `GS.py`, `empresas.json` e `candidatos.json` na **mesma pasta**.  
3. Abra o Pycharm e selecione a mesma pasta.  
4. Execute o programa no arquivo `GS.py`


## 8. Link do Vídeo

Link: ()

## 9. Conclusão

O Provenn foi criado para facilitar a conexão entre pequenas empresas e profissionais que buscam oportunidades.
Ele demonstra, de forma prática, a aplicação de estruturas de controle, funções, manipulação de arquivos e validações em Python.
O sistema é simples, funcional e atende integralmente aos requisitos do GS de Python, unindo técnica, lógica e propósito social.
