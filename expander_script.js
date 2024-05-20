function scrollToExpander() {
    var expander = document.querySelector('.streamlit-expander');
    if (expander) {
        expander.scrollIntoView({ behavior: 'smooth' });
    }
}

window.addEventListener('load', function () {
    var expanderHeader = document.querySelector('.streamlit-expanderHeader');
    if (expanderHeader) {
        expanderHeader.addEventListener('click', scrollToExpander);
    }
});