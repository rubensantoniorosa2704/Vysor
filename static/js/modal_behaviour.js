document.addEventListener('DOMContentLoaded', () => {
  // Funções para abrir e fechar um modal
  function abrirModal($el) {
      $el.classList.add('is-active');
  }

  function fecharModal($el) {
      // Isso impedirá que a última resposta seja mostrada se outra imagem for enviada
      document.querySelector('#description').innerText = "Processando...";

      $el.classList.remove('is-active');
  }

  function fecharTodosOsModais() {
      (document.querySelectorAll('.modal') || []).forEach(($modal) => {
          fecharModal($modal);
      });
  }

  // Adiciona um evento de clique nos botões para abrir um modal específico
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);

      $trigger.addEventListener('click', () => {
          abrirModal($target);
      });
  });

  // Adiciona um evento de clique em vários elementos filhos para fechar o modal pai
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
      const $target = $close.closest('.modal');

      $close.addEventListener('click', () => {
          fecharModal($target);
      });
  });

  // Adiciona um evento de teclado para fechar todos os modais
  document.addEventListener('keydown', (event) => {
      if (event.key === "Escape") {
          fecharTodosOsModais();
      }
  });
});
