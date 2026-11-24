'use strict';
// Keep the current section when switching languages; both pages use the same IDs.
const languageLink = document.querySelector('.language-switch');
if (languageLink) {
  languageLink.addEventListener('click', () => {
    const target = new URL(languageLink.href);
    target.hash = window.location.hash;
    languageLink.href = target.href;
  });
}
