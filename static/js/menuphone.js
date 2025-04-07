document.addEventListener('DOMContentLoaded', function() {
    // Открытие/закрытие главного меню
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.getElementById('mobileMenu');

    mobileMenuBtn.addEventListener('click', function() {
        mobileMenu.classList.toggle('show');
    });

    // Открытие/закрытие выпадающего меню "Примеры работ"
    const dropdownBtn = document.querySelector('.mobile-dropdown-btn');
    const dropdownContent = document.querySelector('.mobile-dropdown-content');

    dropdownBtn.addEventListener('click', function() {
        dropdownContent.classList.toggle('show');

        if (dropdownContent.classList.contains('show')) {
            this.innerHTML = 'Примеры работ ▲';
        } else {
            this.innerHTML = 'Примеры работ ▼';
        }
    });

    // Закрытие меню при клике вне его области
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.mobile-navbar')) {
            mobileMenu.classList.remove('show');
            dropdownContent.classList.remove('show');
            dropdownBtn.innerHTML = 'Примеры работ ▼';
        }
    });

    document.querySelectorAll('.dropdown').forEach(dropdown => {
        dropdown.addEventListener('mouseenter', () => {
            dropdown.querySelector('.dropdown-content').style.display = 'block';
        });
        dropdown.addEventListener('mouseleave', () => {
            dropdown.querySelector('.dropdown-content').style.display = 'none';
        });
    });
});