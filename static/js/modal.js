document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('certificateModal');
    const body = document.body;

    if (modal) {
        document.querySelector('a[href="#certificateModal"]').addEventListener('click', function(e) {
            body.classList.add('modal-open');
        });

        modal.addEventListener('click', function(e) {
            if (e.target === this || e.target.classList.contains('close')) {
                body.classList.remove('modal-open');
            }
        });

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && modal.style.display === 'block') {
                body.classList.remove('modal-open');
                window.location.hash = '#close';
            }
        });
    }
});