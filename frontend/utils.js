import axios from 'axios';

export function fetchCategories(callback) {
  axios
    .get('http://localhost:8000/api/v1/categories/')
    .then(response => {
      const recipes = JSON.parse(JSON.stringify(response.data));
      callback(null, recipes);
    })
    .catch(error => {
      console.error('Error fetching categories:', error);
      callback(error);
    });
}

export function getCategoryFromUrl() {
  const pathArray = window.location.pathname.split('/');
  const categoryIndex = pathArray.indexOf('categorias');
  return pathArray[categoryIndex + 1];
}
