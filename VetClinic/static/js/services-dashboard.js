const articleContainer = document.querySelector('.articles-container');
articleContainer.addEventListener('click', (e) => {
    let dataId = e.target.closest('.article-header').getAttribute('data-id');
    const icon1 = document.getElementById(`article-icon1-${dataId}`);
    const icon2 = document.getElementById(`article-icon2-${dataId}`);

    const button = e.target.closest('.article-dropdown-btn');
    if (!button) return;

    if (dataId) {
        fetch(`/services/api/services/fragment/${dataId}/`)
        .then(response => response.json())
        .then(data => {
            const article = document.querySelector(`[data-id="${dataId}"]`).parentElement;
            let content = article.querySelector('.article-content');
            if (content) {
                article.removeChild(content);
            } else {
                content = document.createElement('div');
                for (let item in Object.values(data)) {
                    const serviceItem = document.createElement('div');
                    const title = document.createElement('h3');
                    const description = document.createElement('p');
                    title.textContent = data[item].name;
                    description.textContent = data[item].description;

                    serviceItem.classList.add('article-item')
                    serviceItem.appendChild(title);
                    serviceItem.appendChild(description);
                    content.appendChild(serviceItem);
                }
                content.classList.add('article-content');
                article.appendChild(content);
            }
        })
        .catch()
    }

    icon1.classList.toggle('article-hidden');
    icon2.classList.toggle('article-hidden');

})