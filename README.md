# 1-Hackaton-SEDICITEC
Projeto desenvolvido para o primeiro Hackaton da SEDICITEC, IFSP campus São Paulo

# 🔬 Ciência Delas

> **"Visibilidade, representatividade e conexões para mulheres em STEM."**

Plataforma web desenvolvida para o **I Hackathon da SEDCITEC 2026** do **IFSP – Campus São Paulo**, com o objetivo de dar visibilidade a mulheres pioneiras na ciência e tecnologia, além de conectar pesquisadoras e estudantes.

---

## 🚀 Sobre o Projeto
O **Ciência Delas** nasceu para combater a invisibilidade histórica das mulheres nas ciências exatas, computação e engenharia. A aplicação funciona como um hub interativo onde é possível explorar trajetórias inspiradoras, realizar buscas em tempo real, favoritar referências e colaborar cadastrando novas pesquisadoras e projetos.

---

## 🛠️ Tecnologias Utilizadas
Este projeto foi desenvolvido utilizando uma arquitetura limpa no padrão **MVC (Model-View-Controller)**:
* **Back-end:** Python com Flask
* **Banco de Dados:** SQLite (com SQL puro integrado)
* **Front-end:** HTML5, CSS3 e JavaScript (Vanilla)
* **Versionamento:** Git & GitHub

---

## 📂 Estrutura de Pastas
```text
projeto-ciencia-delas/
│
├── app.py                    # Inicializador do Servidor Flask
├── database.db               # Banco de dados SQL (gerado automaticamente)
│
├── models/                   # Camada de Dados e SQL
│   ├── __init__.py
│   └── cientista_model.py
│
├── controllers/              # Camada de Controle e Rotas
│   ├── __init__.py
│   └── cientista_controller.py
│
├── templates/                # Camada de Visualização (Views / HTML)
│   ├── index.html
│   └── editar.html
│
└── static/                   # Arquivos Estáticos (Estilos e Scripts)
    ├── style.css
    └── script.js
