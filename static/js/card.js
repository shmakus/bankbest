const scrollButton = document.querySelector('.product__button--scroll');
const scrollBlock = document.querySelector('#reviews');



const reviewsItems = document.querySelectorAll('.reviews__item');
const moreReviews = document.querySelector('.reviews__more');
const hideReviews = document.querySelector('.reviews__hide');

function toggleItems() {
  reviewsItems.forEach((item, i) => {
    if (i > 2) {
      item.classList.toggle('reviews__item--hide');
    }
  });
}

toggleItems();



