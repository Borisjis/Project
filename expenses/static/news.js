const newsData = [
    { 
      title: 'Заголовок новости 1', 
      image: 'https://via.placeholder.com/80x80', 
      link: 'https://example.com/news1' 
    },
    { 
      title: 'Заголовок новости 2', 
      image: 'https://via.placeholder.com/80x80', 
      link: 'https://example.com/news2' 
    },
    { 
      title: 'Заголовок новости 3', 
      image: 'https://via.placeholder.com/80x80', 
      link: 'https://example.com/news3' 
    }
  ];

  function displayNews() {
    const newsList = document.getElementById('newsList');

    newsData.forEach(news => {
      const listItem = document.createElement('li');
      const imageContainer = document.createElement('div');
      const image = document.createElement('img');
      const title = document.createElement('div');
      const link = document.createElement('a');

      image.src = news.image;
      title.textContent = news.title;
      link.href = news.link;
      link.classList.add('news-link');
      link.appendChild(title);
      imageContainer.classList.add('news-image');
      imageContainer.appendChild(image);

      listItem.classList.add('news-item');
      listItem.appendChild(imageContainer);
      listItem.appendChild(link);

      newsList.appendChild(listItem);
    });
  }


  displayNews();