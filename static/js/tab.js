document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.tab');

    tabs.forEach(tab => {
        const title = tab.querySelector('.tab-title');
        const arrow = tab.querySelector('.tab-arrow');
        const content = tab.querySelector('.tab-content');

        content.style.maxHeight = '0';
        content.style.paddingTop = '0';
        content.style.paddingBottom = '0';

        title.addEventListener('click', function() {
            const isActive = tab.classList.contains('active');

            // Закрываем все аккордеоны
            tabs.forEach(otherTab => {
                otherTab.classList.remove('active');
                const otherContent = otherTab.querySelector('.tab-content');
                otherContent.style.maxHeight = '0';
                otherContent.style.paddingTop = '0';
                otherContent.style.paddingBottom = '0';
                otherTab.querySelector('.tab-arrow').style.color = '#62BEC2';
                otherTab.querySelector('.tab-arrow').style.transform = 'rotate(0deg)';
            });

            // Если аккордеон был закрыт - открываем его
            if (!isActive) {
                tab.classList.add('active');
                content.style.maxHeight = content.scrollHeight + 'px';
                content.style.paddingTop = '15px';
                content.style.paddingBottom = '15px';
                arrow.style.color = 'white';
                arrow.style.transform = 'rotate(180deg)';
            }
        });
    });
});