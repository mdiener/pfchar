class Sections {
    show(id) {
        let section = document.querySelector(id + '.section');
        section.style.left = ((section.parentElement.offsetWidth / 2) - (section.offsetWidth / 2)) + 'px';
        if (section != null) {
            section.classList.add('visible');
            section.classList.remove('hidden');
        }
    }

    hideAll() {
        document.querySelectorAll('.section').forEach((section, i) => {
            section.classList.add('hidden');
            section.classList.remove('visible');
        });
    }
}

export var sections = new Sections()
