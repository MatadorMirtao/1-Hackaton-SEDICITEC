// Filtro de busca em tempo real
const searchInput = document.getElementById('searchInput');

if (searchInput) {
    searchInput.addEventListener('input', (e) => {
        const termo = e.target.value.toLowerCase();
        const cards = document.querySelectorAll('.card');

        cards.forEach(card => {
            const nome = card.getAttribute('data-name') || '';
            const area = card.getAttribute('data-area') || '';

            if (nome.includes(termo) || area.includes(termo)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// Botão de Favoritar / Inspirador (ativa a caixinha rosa)
function destacarCard(botao) {
    const card = botao.closest('.card');
    card.classList.toggle('favorito');
    
    if (card.classList.contains('favorito')) {
        botao.textContent = 'Inspirado! 💖';
    } else {
        botao.textContent = 'Inspirador! ✨';
    }
}

// Animação de Contagem dos Números no Banner
function animarContador(idElemento, valorFinal, sufixo = '') {
    let atual = 0;
    const incremento = Math.ceil(valorFinal / 40);
    const elemento = document.getElementById(idElemento);
    
    if (!elemento) return;

    const timer = setInterval(() => {
        atual += incremento;
        if (atual >= valorFinal) {
            atual = valorFinal;
            clearInterval(timer);
        }
        elemento.textContent = atual + sufixo;
    }, 40);
}

// Inicia os contadores ao carregar a página
window.addEventListener('DOMContentLoaded', () => {
    animarContador('counterStat', 28, '%');
    
    const totalCards = document.querySelectorAll('.card').length;
    animarContador('counterCommunity', totalCards);
});