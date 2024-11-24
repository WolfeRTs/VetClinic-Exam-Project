const articleContainer = document.querySelector('.articles-container');
articleContainer.addEventListener('click', (e) => {
    let dataId = e.target.getAttribute('data-id');

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
                    const title = document.createElement('h3');
                    const description = document.createElement('p');
                    title.textContent = data[item].name;
                    description.textContent = data[item].description;

                    content.appendChild(title);
                    content.appendChild(description);
                }
                content.classList.add('article-content');
                article.appendChild(content);
            }
        })
        .catch()


})